# P5 Archive Browser

P5 Archive Browser is a pre-release macOS application for searching and browsing
file inventories exported from Archiware P5 Archive. It helps answer:

> Which archive tape contains this file or project?

This public repository is for application testing and documentation only. It
does not contain the application source code.

## Download and install

1. Download `P5 Archive Browser.app.zip` from the top level of this repository.
2. Double-click the ZIP to expand it.
3. Move **P5 Archive Browser.app** to your Applications folder.
4. Open the application.

This pre-release is for Apple-silicon Macs and requires macOS 14.6 or later. It
is not notarized. If macOS blocks the first launch, right-click the app and
choose **Open**, or use **System Settings ▸ Privacy & Security ▸ Open Anyway**.
Only do this if you obtained the app directly from this repository.

ZIP SHA-256:

`98a73eac5457eecd4ba2a546f40f60b73136e39ecff16c165cebda7f63aed4a2`

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

Please do not commit client CSV files, TSV inventories, databases, server
credentials, logs, or crash reports to this public repository.
