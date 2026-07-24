# Tester Notes

Thank you for testing P5 Archive Browser. This is a pre-release application, so
use copies of exported inventory files and continue using your normal P5 tools
for archive and restore operations.

## Important limitations

- The app is Apple-silicon only and requires macOS 14.6 or later.
- Download only the DMG attached to this repository's pre-release. Check that
  release for the app's signing and notarization status.
- TSV import scans the selected folder and one subfolder level.
- Prepared portable-database import/export is not available yet.
- Watch Folder automatically imports TSV only; volume-list CSV watching is not
  available yet.
- Archive Groups are not yet bound to named multiple P5 servers.
- P5 API operations in this app are read-only. The app does not restore, archive,
  delete, or move files.
- A failed P5 file check can mean the archived path, capitalization, path mapping,
  or available archive indexes differ from the imported TSV.

## Suggested test pass

1. Use [P5 Archive Export](https://github.com/macvfx/p5ArchiveExport)'s
   **Volume Export** workflow to prepare per-volume TSV inventories and,
   optionally, the full volume-list CSV organized by LTO generation.
2. Use **Import Archive Folder (CSV + TSV)…** on the parent folder containing the
   volume-list CSV and generation folders such as `LTO-7` and `LTO-8`.
3. Confirm the completion summary reports metadata and inventory separately.
4. Wait for background search-index maintenance to finish.
5. Create Archive Groups, bulk-move tapes from Unassigned, reorder groups, and
   confirm disclosure triangles keep the sidebar compact.
6. Quit and reopen the app; confirm group names, order, and assignments persist.
7. Open a large tape and expand several folders.
8. Check the tape-row legend: orange/blue/green/purple discs mean LTO-6/7/8/9,
   gray means unknown, “~” means inferred generation, a crossed-out tag means no
   barcode, the map pin means location, and a right-side green/gray dot means
   live P5 online/offline state.
9. Search within that tape and verify the complete match count and bounded result
   list.
10. Search all tapes in **Files**, reveal a result, and return to the retained
   results.
11. Search in **Projects**, browse a tape row, and return to Project results.
12. Save similarly named File and Project searches and confirm labels such as
   `Apple - Files` and `Apple - Projects`.
13. Configure a P5 connection, load P5 Tools, and inspect archive indexes and
   archive plans.
14. With P5 unavailable, run bulk and single-tape metadata refreshes and confirm
    each stops after one bounded connection test with a visible message.
15. Click the check-shield button on a filtered file row, or right-click a file
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
