# P5 Archive Browser

P5 Archive Browser is a pre-release macOS application for searching and browsing
file inventories exported from Archiware P5 Archive. It helps answer:

> Which archive tape contains this file or project?

This public repository is for application testing and documentation only. It
does not contain the application source code.

## Download and install

1. Open this repository's **Releases** page and download the signed
   `P5 Archive Browser.app.zip` from the pre-release Assets section.
2. Double-click the ZIP to expand it.
3. Move **P5 Archive Browser.app** to your Applications folder.
4. Open the application.

This pre-release is for Apple-silicon Macs and requires macOS 14.6 or later.
Download only the signed application attached to a pre-release in this
repository. Signing and notarization status will be stated on that release.

## What testers can do

- Import P5 volume metadata from a volume-list CSV.
- Import searchable tape contents from P5 TSV inventory files.
- Browse large tape inventories folder by folder.
- Search files and derived projects across all imported tapes.
- Open a search result on its tape and return to retained results.
- Save and reopen recent File and Project searches.
- Connect to P5 for live volume metadata and health information.
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
