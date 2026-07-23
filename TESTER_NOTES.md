# Tester Notes

Thank you for testing P5 Archive Browser. This is a pre-release application, so
use copies of exported inventory files and continue using your normal P5 tools
for archive and restore operations.

## Important limitations

- The app is Apple-silicon only and requires macOS 14.6 or later.
- Download only the DMG attached to this repository's pre-release. Check that
  release for the app's signing and notarization status.
- CSV metadata and TSV inventory are currently imported in two actions.
- TSV import scans the selected folder and one subfolder level.
- Prepared portable-database import/export is not available yet.
- Automatic watch-folder imports are not available yet.
- P5 API operations in this app are read-only. The app does not restore, archive,
  delete, or move files.
- A failed P5 file check can mean the archived path, capitalization, path mapping,
  or available archive indexes differ from the imported TSV.

## Suggested test pass

1. Use [P5 Archive Export](https://github.com/macvfx/p5ArchiveExport)'s
   **Volume Export** workflow to prepare per-volume TSV inventories and,
   optionally, the full volume-list CSV organized by LTO generation.
2. Import the volume-list CSV.
3. Import a parent folder containing generation folders such as `LTO-7` and
   `LTO-8`.
4. Wait for background search-index maintenance to finish.
5. Open a large tape and expand several folders.
6. Search within that tape and verify the complete match count and bounded result
   list.
7. Search all tapes in **Files**, reveal a result, and return to the retained
   results.
8. Search in **Projects**, browse a tape row, and return to Project results.
9. Save similarly named File and Project searches and confirm labels such as
   `Apple - Files` and `Apple - Projects`.
10. Configure a P5 connection, load P5 Tools, and inspect archive indexes and
   archive plans.
11. Click the check-shield button on a filtered file row, or right-click a file
    in the folder tree, and run the read-only P5 verification.

## Reporting a problem

Please include:

- What you were doing immediately before the problem.
- Whether the data came from CSV, TSV, or the live P5 API.
- The approximate tape file count.
- The exact text shown by the app.
- A screenshot when useful.
- macOS version and Mac model.
- A crash report if macOS generated one.

Remove server passwords, private server addresses if required by your site,
client filenames, and other confidential archive information before sharing a
report publicly.
