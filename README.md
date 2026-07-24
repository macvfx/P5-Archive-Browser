# P5 Archive Browser

P5 Archive Browser is a pre-release macOS application for searching and browsing
file inventories exported from Archiware P5 Archive. It helps answer:

> Which archive tape contains this file or project?

This public repository is for application testing and documentation only. It
does not contain the application source code.

The documentation covers version 0.19 (build 31). Check the Releases page for
the version number of the latest downloadable pre-release.

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
- Import searchable tape contents from P5 TSV inventory files.
- Import a complete P5 Archive Export folder in one guided CSV-first operation,
  or automatically watch its TSV inventories for later changes.
- Organize tapes into persistent, collapsible Archive Groups independently from
  their TSV source folders.
- Browse large tape inventories folder by folder.
- Read the tape-row indicators for LTO generation, a missing barcode, inferred
  generation, location, and live online/offline state.
- Search files and derived projects across all imported tapes.
- Open a search result on its tape and return to retained results.
- Save and reopen recent File and Project searches.
- Connect to P5 for live volume metadata and health information.
- Stop bulk and single-tape metadata refreshes quickly when P5 is unreachable,
  using one bounded connection preflight instead of repeated tape timeouts.
- List P5 archive indexes and archive plans.
- Perform a read-only sanity check for a cataloged file across P5 archive
  indexes.

P5 Archive Browser does not load tapes, restore files, submit archive jobs, or
change data on the P5 server.

## Start here

- [User Guide](USER_GUIDE.md)
- [Tester Notes](TESTER_NOTES.md)
- [Pre-release Notes](RELEASE_NOTES.md)

## Prepare P5 inventory exports

Use [P5 Archive Export](https://github.com/macvfx/p5ArchiveExport) as the
recommended companion app. Its **Volume Export** workflow creates the per-volume
TSV inventories that P5 Archive Browser searches. It can also include the full
volume-list CSV and organize TSV output by LTO generation.

Please do not commit client CSV files, TSV inventories, databases, server
credentials, logs, or crash reports to this public repository.
