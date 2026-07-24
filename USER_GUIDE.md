# P5 Archive Browser User Guide

## Purpose

P5 Archive Browser is a local catalog for P5 Archive volumes, usually LTO tapes.
It lets you find an archived file or project and identify the tape that should be
loaded into your normal P5 restore workflow.

## Data sources

The app keeps three sources distinct:

- **TSV file inventory** supplies archived paths. It powers File Browser, Files
  search, and Projects.
- **Volume-list CSV** supplies offline tape metadata such as volume label,
  barcode, state, media type, used size, last-used date, and P5 location.
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

Arrange an export folder like this:

```text
Client Archive Export/
  p5-volumes-list.csv
  LTO-7/
    10001_BARCODEL7.tsv
    10002_BARCODEL7.tsv
  LTO-8/
    11064.tsv
    11065.tsv
```

1. Choose **Import ▸ Import Offline Volume Metadata (CSV)…** and select the CSV.
2. Choose **Import ▸ Import File Inventory (TSV)…** and select the top-level
   `Client Archive Export` folder.
3. Wait for background search-index maintenance to reach 100%.

You do not need to import each generation separately. The importer reads TSV
files at the selected folder's top level and one subfolder level. Immediate
subfolders such as `LTO-7` and `LTO-8` become optional sidebar groups.

## Browse a tape

Select a tape in the sidebar and open **File Browser**. Large inventories load
one folder at a time from the local database. Expand a folder to load its
immediate contents.

The count beside a folder is the number of files below it. The size is the total
content size below that folder.

Use the search field above File Browser to search only the selected tape. Broad
searches report the complete match count while displaying the first 2,000 paths.
Clear the field to return to the folder hierarchy.

## Understand tape rows

- **Colored disc** — the tape's LTO generation: orange is LTO-6, blue is
  LTO-7, green is LTO-8, purple is LTO-9, and gray means the generation is
  unknown.
- **Generation badge** — shows the detected LTO generation. A trailing “~”
  means it was inferred from source-folder or size evidence rather than confirmed
  by a barcode.
- **Crossed-out tag** — the tape has no barcode, so its displayed name comes
  from its alias or P5 volume label.
- **Map pin** — the tape has a physical Location note or a location reported by
  P5.
- **Status dot at the right** — when live P5 state is available, green means
  online and gray means offline. No dot means the app has no live online/offline
  state for that tape.

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
- **P5 Tools** beside Refresh Detail to list archive indexes and archive plans.

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

## Identify and restore the tape

Use the volume label, barcode, LTO generation, P5 location, your own Location
note, and full archived path to identify the cartridge. Load and restore it using
your site's normal P5 interface and procedures.

P5 Archive Browser does not operate tape hardware or submit restore jobs.

## Local data and passwords

The local catalog is stored under:

`~/Library/Application Support/P5 Archive Browser/`

P5 passwords are stored in the macOS login Keychain and are not stored in the
catalog database.
