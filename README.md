# P5 Archive Browser

P5 Archive Browser is a pre-release macOS application for searching and browsing
file inventories exported from Archiware P5 Archive. It helps answer:

> Which archive tape contains this file or project?

This public repository is for application testing and documentation only. It
does not contain the application source code.

The documentation covers the upcoming version 0.31 (build 42). Check the
Releases page for the version number of the latest downloadable pre-release.

**This pre-release includes the app's first operation that writes to the P5
server:** restoring a whole tape folder's subtree directly from P5 (added in
build 37). It's off by default — see
[What testers can do](#what-testers-can-do) and the
[User Guide](USER_GUIDE.md) before enabling it. Build 38 was a packaging fix
only. Build 39 fixed a real restore failure: a folder that P5 had actually
archived could be reported as "not found" because of a path-format
mismatch. Build 40 fixed a UI bug — a restore or Folder Info window could
appear small and empty — and added a mid-run progress indicator showing a
few lines of P5's own job report while a restore runs. Build 41 was a small
wording fix. **Build 42 fixes a real bug found during tape-restore
testing:** if a restore needed a tape that wasn't loaded, the app could give
up watching too early and report a false failure while the P5 job was still
actually running. The app now waits up to an hour and, if it does give up
first, says plainly that the job may still be in progress rather than
reporting a false result. See [Pre-release Notes](RELEASE_NOTES.md).

## Download and install

1. Open this repository's **Releases** page and download
   `P5 Archive Browser.dmg` from the pre-release Assets section.
2. Open the DMG.
3. Drag **P5 Archive Browser.app** to the Applications folder.
4. Eject the DMG, then open the app from Applications.

This pre-release is for Apple-silicon Macs and requires macOS 14.6 or later.
Download only the DMG attached to a pre-release in this repository. Signing and
notarization status will be stated on that release.

## What testers can do

- Import P5 volume metadata from a volume-list CSV.
- Normalize balanced SQL-style outer quotes so CSV identities reconcile with
  their TSV tapes, with a targeted cleanup for pre-existing zero-file ghosts.
- Import searchable tape contents from P5 TSV inventory files.
- Safely recognize both six-column P5 Archive Export/direct `nsdchat`
  inventories and eight-column P5 Web GUI Volume Inventory exports.
- Review the detected inventory columns before a manual import; malformed,
  mixed, shifted, and unknown layouts stop without replacing the last good
  inventory.
- Select one TSV from a larger folder, or select a folder for a bulk import.
- Import P5-native names such as `90002_vol_inventory.tsv` without treating
  `vol` as a barcode, then resolve a missing barcode from P5 by volume ID.
- Import a complete P5 Archive Export folder in one guided CSV-first operation,
  or automatically watch its TSV inventories for later changes.
- Create a consistent standalone catalog backup, or perform a backup-gated
  catalog reset while retaining P5/project settings and the Keychain password.
- See the complete live catalog footprint and choose a persistent backup folder,
  including a folder on another mounted drive.
- Organize tapes into persistent, collapsible Archive Groups independently from
  their TSV source folders.
- Browse large tape inventories folder by folder.
- Read the tape-row indicators for LTO-5 through LTO-10, a missing barcode,
  inferred generation, location, and live online/offline state.
- Keep P5 Location visible as read-only metadata while suppressing the
  server's `<empty>` sentinel and its sidebar icon.
- Search files and derived projects across all imported tapes.
- Open a search result on its tape and return to retained results.
- Save and reopen recent File and Project searches.
- Connect to P5 for live volume metadata and health information.
- Stop bulk and single-tape metadata refreshes quickly when P5 is unreachable,
  using one bounded connection preflight instead of repeated tape timeouts.
- List P5 archive indexes and archive plans.
- Perform a read-only sanity check for a cataloged file across P5 archive
  indexes.
- **Restore a whole folder directly from P5** — right-click a folder and
  choose Restore Folder from P5 Archive… Off by default (**Settings ▸
  Restore ▸ Enable P5 Restore**). Shows the expected file count/size and
  destination before submitting, then independently verifies what actually
  landed rather than trusting a completed P5 job.
- **Folder Info and Search All Tapes ▸ Folders** — read-only recursive folder
  size, per tape and rolled up across every tape.
- Check the public GitHub releases automatically or with **Check for Updates…**.

P5 Archive Browser does not load tapes into a drive or submit archive jobs.
Restoring a whole folder from P5, off by default, is now supported — see
[Restore a folder, or use P5 directly](USER_GUIDE.md#restore-a-folder-or-use-p5-directly)
in the User Guide. Restoring an individual file is not yet supported.

## Start here

- [User Guide](USER_GUIDE.md)
- [Tester Notes](TESTER_NOTES.md)
- [Pre-release Notes](RELEASE_NOTES.md)
- [Build 42 GitHub Release Blurb](RELEASE_BLURB_0.31_BUILD_42.md)
- [Build 41 GitHub Release Blurb](RELEASE_BLURB_0.31_BUILD_41.md)
- [Build 40 GitHub Release Blurb](RELEASE_BLURB_0.31_BUILD_40.md)
- [Build 39 GitHub Release Blurb](RELEASE_BLURB_0.30_BUILD_39.md)

## Prepare P5 inventory exports

Use [P5 Archive Export](https://github.com/macvfx/p5ArchiveExport) as the
recommended companion app. Its **Volume Export** workflow creates the per-volume
TSV inventories that P5 Archive Browser searches. It can also include the full
volume-list CSV and organize TSV output by LTO generation.

Build 36 supports both the six-column inventory order `index path, ppath, size,
handle, btime, mtime` and P5 Web GUI's eight-column order `index path, ppath,
volumes, size, handle, btime, mtime, checksum`. The app detects the profile,
shows its field mapping before a manual import, validates every row, and reads
size from the correct column. Unknown custom layouts remain unsupported and are
rejected without changing the catalog.

Please do not commit client CSV files, TSV inventories, databases, server
credentials, logs, or crash reports to this public repository.
