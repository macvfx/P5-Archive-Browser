# P5 Archive Browser User Guide

Applies to **P5 Archive Browser v0.30 build 37**.

## Purpose

P5 Archive Browser is a local catalog for P5 Archive volumes, usually LTO
tapes. It lets you find an archived file or project, identify the tape, and —
for a whole folder, once turned on in Settings — restore it directly from P5.

## Data sources

The app keeps three sources distinct:

- **TSV file inventory** supplies archived paths. It powers File Browser, Files
  search, and Projects. Build 36 supports the six-column P5 Archive
  Export/direct `nsdchat` order and P5 Web GUI's eight-column Volume Inventory
  order.
- **Volume-list CSV** supplies offline tape metadata such as volume label,
  barcode, state, media type, used size, last-used date, and P5 location.
  Balanced SQL-style outer single quotes are removed before identity matching.
- **P5 REST API** supplies live volume metadata and health, archive indexes,
  archive plans, and read-only file verification.

The app is useful from CSV and TSV imports without a live P5 connection.

## Recommended first import

Generate the source files with
[P5 Archive Export](https://github.com/macvfx/p5ArchiveExport). Choose its
**Volume Export** workflow—not SQL Export or Backup Export—to create one
`volumeID[_BARCODE].tsv` inventory per P5 volume. Enable its full volume-list CSV
option when you also want offline labels, barcodes, state, size, and location
metadata. Its LTO-generation organization option produces a folder layout that
P5 Archive Browser can use directly.

P5's own Volume Inventory UI may instead create a name such as the synthetic
`90002_vol_inventory.tsv`. Here, `90002` is the P5 volume ID and
`vol_inventory` is a description, not a barcode. The app leaves Barcode empty
unless the filename contains a valid LTO barcode or metadata later supplies one.

The supported profiles are:

- Six-column P5 Archive Export/direct `nsdchat`: `index path, ppath, size,
  handle, btime, mtime`.
- Eight-column P5 Web GUI Volume Inventory: `index path, ppath, volumes, size,
  handle, btime, mtime, checksum`.

Before a manual file, folder, or combined CSV + TSV import, **Review Inventory
Columns** shows every detected profile and its ordered field mapping. Every
non-empty row must keep that layout and contain a nonnegative size in the mapped
column. Mixed, shifted, malformed, and unknown layouts stop without creating a
new tape or replacing the last good inventory. An unrestricted custom field
mapper is not included in Build 36.

Arrange an export folder like this:

```text
Client Archive Export/
  p5-volumes-list.csv
  LTO-7/
    90001_DEMO01L7.tsv
    90002_DEMO02L7.tsv
  LTO-8/
    90003.tsv
    90004.tsv
```

1. Choose **Import ▸ Import Archive Folder (CSV + TSV)…**.
2. Select the top-level `Client Archive Export` folder. The app recognizes one
   top-level volume-list CSV, imports it first, and then imports TSV inventories
   from the root and one generation-folder level.
3. Review the detected TSV columns, then review the completion summary, which
   reports metadata and inventory results separately.
4. Wait for background search-index maintenance to reach 100%.

You do not need to import each generation separately. The importer reads TSV
files at the selected folder's top level and one subfolder level. Immediate
subfolders such as `LTO-7` and `LTO-8` remain source provenance and generation
evidence; use Archive Groups for your own sidebar organization.

To import only one inventory from a larger folder, choose **Import ▸ Import File
Inventory (TSV)…** and select that `.tsv` directly. Selecting a folder keeps the
bulk root-plus-one-subfolder behavior.

## Automatically import later TSV exports

Open **Settings ▸ Watch Folder**, select the P5 Archive Export folder, and enable
watching. New or modified TSVs wait until they are old and stable before import;
unchanged successful files are skipped. **Check Now** scans immediately, while
**Clear History** makes the next scan reconsider every TSV.

Malformed replacements, interrupted imports, and conflicting sources do not
replace the last successful tape inventory. Watch state, fingerprints, runs,
attempts, and inventory provenance remain durable across restarts. Volume-list
CSV watching is not included yet. A watched unknown layout is recorded as
needing column review instead of being guessed or opening a background dialog.

## Back up, repair, or reset the catalog

Open **Settings ▸ Catalog Data**:

- **Storage used** reports the main SQLite database plus active WAL and
  shared-memory sidecars.
- **Preferred Backup Folder** chooses where manual backup panels start and
  automatic pre-reset backups are written. It may be on another mounted drive.
- **Back Up Catalog…** creates a consistent standalone SQLite copy while the
  app remains open.
- **Remove Invalid CSV Records…** is available only when the app finds
  CSV-origin, zero-file records whose identity still has balanced outer single
  quotes. Inventory-bearing tapes are never selected.
- **Back Up and Reset Catalog…** stops the watch folder and must create a dated
  backup before clearing imported tapes, inventories, Archive Groups, and watch
  history. P5/project settings and the Keychain password are preserved.

If the preferred backup folder is unavailable or not writable, reset stops
without changing the catalog. Moving the active database itself is not yet
supported.

## Check for app updates

Browser checks the public GitHub releases at most once per day and stays silent
when no newer version exists. Choose **P5 Archive Browser ▸ Check for Updates…**
for an immediate check. **Download** opens the public release page; Browser does
not download or install updates automatically.

## Browse a tape

Select a tape in the sidebar and open **File Browser**. Large inventories load
one folder at a time from the local database. Expand a folder to load its
immediate contents.

The count beside a folder is the number of files below it. The size is the total
content size below that folder.

Use the search field above File Browser to search only the selected tape. Broad
searches report the complete match count while displaying the first 2,000 paths.
Clear the field to return to the folder hierarchy.

## Folder sizes

- **Folder Info** — right-click any folder in File Browser for a read-only
  summary: this tape's recursive file count and size, plus a roll-up across
  every other tape holding part of the same folder. No P5 connection is
  needed; this reads only the local catalog.
- **Search All Tapes ▸ Folders** — a third search scope alongside Files and
  Projects. Enter at least three characters of a folder name; each result
  shows its rolled-up size and every tape it spans. Double-click a tape row,
  or use **Browse**, to open that tape at the matching folder.

Both totals sum the file sizes imported from TSV inventories. They don't yet
distinguish a directory row in the source TSV from a file, and don't account
for duplicate or versioned entries across tapes.

## Understand tape rows

- **Colored disc** — the tape's LTO generation: cyan/teal is LTO-5, orange is
  LTO-6, blue is LTO-7, green is LTO-8, purple is LTO-9, magenta is LTO-10,
  and gray means the generation is unknown.
- **Generation badge** — shows the detected LTO generation. A trailing “~”
  means it was inferred from source-folder or size evidence rather than confirmed
  by a barcode.
- **Crossed-out tag** — the tape has no barcode, so its displayed name comes
  from its alias or P5 volume label.
- **Map pin** — the tape has a physical Location note or a location reported by
  P5. The P5 `<empty>` sentinel never creates this icon.
- **Status dot at the right** — when live P5 state is available, green means
  online and gray means offline. No dot means the app has no live online/offline
  state for that tape.

### LTO capacity and inferred generation

Official cartridge specifications and an estimate from imported file totals are
different evidence:

| Generation | Official native capacity | Advertised compressed capacity |
|---|---:|---:|
| LTO-5 | 1.5 TB | 3 TB |
| LTO-6 | 2.5 TB | 6.25 TB |
| LTO-7 | 6 TB | 15 TB |
| LTO-8 | 12 TB | 30 TB |
| LTO-9 | 18 TB | 45 TB |
| LTO-10 | 30 TB or 40 TB, by cartridge variant | 75 TB or 100 TB |

Compressed figures are marketing specifications based on an assumed
compression ratio, not guaranteed usable space. A partial newer tape can have
the same imported total as a full older tape, and logical file totals can differ
from physical media use. Therefore a size-derived label is shown as **LTO-X or
newer** with an inference marker; it is not official media identification.
Barcode, P5 media metadata, and declared source folder remain stronger evidence.

## Organize tapes with Archive Groups

Archive Groups are persistent, user-managed sidebar folders. They are separate
from TSV source folders such as `LTO-7`.

- Each group has a disclosure triangle and tape count and starts collapsed.
- Click **Organize…** to create, rename, reorder, merge, or safely delete groups
  and to move multiple tapes at once.
- Right-click a tape and choose **Move to Archive Group** for a single move.
- **Unassigned** contains tapes not yet placed in a group.
- Deleting a group moves its tapes to Unassigned and never deletes catalog
  inventory.
- Reimporting a TSV updates its source provenance without undoing its Archive
  Group assignment.

## Search all tapes

Select **Search All Tapes** in the sidebar.

### Files

1. Select **Files**.
2. Enter at least three characters from a filename or archived path.
3. Press Return or click **Search**.
4. Review matches grouped by tape.
5. Double-click a result or click **Reveal** to open the tape and reveal the
   matching file.
6. Click **Back to Search Results** to return to the retained result set.

### Projects

1. Select **Projects**.
2. Leave the query blank and click **List**, or enter a project-name fragment.
3. Review each project and the tapes that contain it.
4. Double-click a tape row or click **Browse** to open that tape filtered to the
   complete project path.
5. Click **Back to Project Results** to return.

Project detection is configured in **Settings ▸ Projects** using archive root
paths, an optional naming pattern, and a folder-depth fallback.

## Recent and saved searches

The app keeps recent searches automatically. Use the star to save a useful
search. Labels put the query first and scope last, for example:

- `Apple - Files`
- `Apple - Projects`

This keeps similar File and Project searches together.

## P5 connection

Open Settings using the gear beside **Refresh Detail** or the standard macOS
Settings command. Enter the P5 server address, port, username, API version, and
fallback archive index. Save the password in the macOS login Keychain, then test
the connection.

Use:

- **Discover New Volumes from P5** to add newly discovered server volumes.
- **Refresh Live Metadata for All Volumes** to refresh existing volume details.
- **Refresh Detail** to refresh the currently selected tape.
- **Resolve from P5** beside an empty Barcode to match the P5 volume list by
  label or numeric ID, then fall back to the individual volume detail. If P5
  reports no barcode, the value remains empty.
- **P5 Tools** beside Refresh Detail to list archive indexes and archive plans.

**P5 Location** remains visible in Info & Notes as read-only metadata. Change it
in P5, then use **Refresh Detail**. When P5 reports `<empty>`, the field shows a
dash and no sidebar map pin; genuine shelf, slot, drive, or note values display
and remain searchable.

Bulk and single-tape metadata refreshes run a bounded P5 connection test before
requesting tape details. If P5 is unavailable, the app stops and offers Settings
instead of timing out against every tape. If connectivity drops during a bulk
refresh, the app performs one short recheck, stops, and reports how many tapes
completed. A failed single-tape refresh leaves its existing metadata unchanged.

## Verify a file in P5

For a filtered file result, click the check-shield button at the end of the row.
For a file in the folder tree, right-click and choose **Verify File in P5
Archive**. A file opened from Search All Tapes also has a **Verify in P5**
button.

Verification:

- Is read-only.
- Checks the configured fallback index first.
- Automatically checks every other archive index discovered from P5.
- Reports the indexes checked and where the path was found.
- Shows a possible volume label, barcode, or P5 location when the server returns
  enough information.

The imported local catalog remains the primary tape-identification source. Live
P5 inventory responses do not always include a physical tape or barcode.

## Restore a folder, or use P5 directly

Right-click a folder in **File Browser** and choose **Restore Folder from P5
Archive…** to restore its whole subtree in a single step — one directory
handle restores the entire tree, confirmed against a live P5 8.0.4 server.
This is off by default: turn on **Enable P5 Restore** in **Settings ▸
Restore** first, and set a default destination client and path.

The confirmation sheet shows the expected file count and size from the local
catalog (not from P5's own directory listing), the tape's online/offline
state, and the exact destination path — a restore always creates a new
folder named after the source folder; it never overwrites the destination
path itself. After the job completes, the app verifies what actually landed
against what was expected whenever the destination is readable from this
Mac, and reports any difference rather than trusting a completed P5 job — P5
has been observed to report success while omitting files. If the
destination isn't readable from this Mac, the app shows P5's own job report
instead, with a note that job success alone doesn't guarantee completeness.

Restoring an **individual file**, rather than a whole folder, isn't
supported yet. For an individual file, or if restore is left off, use the
volume label, barcode, LTO generation, P5 location, your own Location note,
and full archived path to identify the cartridge, then restore through your
normal P5 interface. P5 Archive Browser still doesn't operate tape hardware
directly; P5 handles loading the cartridge and running the job.

## Local data and passwords

The local catalog is stored under:

`~/Library/Application Support/P5 Archive Browser/`

P5 passwords are stored in the macOS login Keychain and are not stored in the
catalog database.
