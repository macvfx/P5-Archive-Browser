# Tester Notes

These notes apply to **P5 Archive Browser v0.30 build 37**.

Thank you for testing P5 Archive Browser. This is a pre-release application, so
use copies of exported inventory files. **Build 37 introduces this app's
first operation that writes to the P5 server** — restoring a whole tape
folder directly from P5 — and it is off by default. Please read
[Testing Restore Folder](#testing-restore-folder) below before turning it on,
and continue using your normal P5 tools for individual-file restore and
archive operations, since those aren't supported by this app yet.

## Important limitations

- The app is Apple-silicon only and requires macOS 14.6 or later.
- Download only the DMG attached to this repository's pre-release. Check that
  release for the app's signing and notarization status.
- TSV import accepts one selected `.tsv`; selecting a folder scans that folder
  and one subfolder level.
- Build 36 supports the six-column order `index path, ppath, size, handle,
  btime, mtime` and P5 Web GUI's eight-column order `index path, ppath, volumes,
  size, handle, btime, mtime, checksum`. Unknown custom layouts remain
  unsupported and are rejected safely.
- Prepared portable-database import/export is not available yet.
- Watch Folder automatically imports TSV only; volume-list CSV watching is not
  available yet.
- Archive Groups are not yet bound to named multiple P5 servers.
- **Restoring a whole folder from P5 is supported and off by default.**
  Restoring an **individual file** is not — restore the containing folder
  instead, or use your normal P5 workflow. The app never archives, deletes,
  or moves files.
- Folder restore always creates a new folder named after the source folder
  under your chosen destination. It never overwrites the destination path
  itself, but overwrite behavior *within* a populated destination (e.g.
  restoring the same folder twice) has not been characterized — use an
  empty or dedicated destination.
- Folder-size totals (Folder Info, Search ▸ Folders) sum imported TSV file
  sizes. They don't yet distinguish a directory row in the source TSV from a
  file, and don't account for duplicate or versioned entries across tapes.
- A failed P5 file check can mean the archived path, capitalization, path mapping,
  or available archive indexes differ from the imported TSV.

## Suggested test pass

1. Use [P5 Archive Export](https://github.com/macvfx/p5ArchiveExport)'s
   **Volume Export** workflow to prepare per-volume TSV inventories and,
   optionally, the full volume-list CSV organized by LTO generation.
2. Use **Import Archive Folder (CSV + TSV)…** on the parent folder containing the
   volume-list CSV and generation folders such as `LTO-7` and `LTO-8`.
3. From a larger folder such as Downloads, use **Import File Inventory
   (TSV)…** to select one TSV and confirm no neighboring TSV is imported.
4. Import a synthetic P5-native example such as
   `90002_vol_inventory.tsv`. Confirm its P5 volume ID is `90002` and Barcode is
   empty rather than `vol`.
5. If the configured P5 server knows a barcode for that volume ID, use
   **Resolve from P5** beside Barcode and confirm the tape reconciles without
   losing its inventory or Archive Group. If P5 reports no barcode, confirm the
   app leaves it empty and explains that result.
6. Confirm the completion summary reports metadata and inventory separately.
7. Wait for background search-index maintenance to finish.
8. Create Archive Groups, bulk-move tapes from Unassigned, reorder groups, and
   confirm disclosure triangles keep the sidebar compact.
9. Quit and reopen the app; confirm group names, order, and assignments persist.
10. Open a large tape and expand several folders.
11. Check the tape-row legend: cyan/teal, orange, blue, green, purple, and
   magenta discs mean LTO-5/6/7/8/9/10; gray means unknown, “~” means inferred
   generation, a crossed-out tag means no barcode, the map pin means location,
   and a right-side green/gray dot means live P5 online/offline state.
12. Search within that tape and verify the complete match count and bounded result
   list.
13. Search all tapes in **Files**, reveal a result, and return to the retained
   results.
14. Search in **Projects**, browse a tape row, and return to Project results.
15. Save similarly named File and Project searches and confirm labels such as
   `Apple - Files` and `Apple - Projects`.
16. Configure a P5 connection, load P5 Tools, and inspect archive indexes and
   archive plans.
17. With P5 unavailable, run bulk and single-tape metadata refreshes and confirm
    each stops after one bounded connection test with a visible message.
18. Click the check-shield button on a filtered file row, or right-click a file
    in the folder tree, and run the read-only P5 verification.
19. Import a copy of a volume-list CSV with balanced outer single quotes around
    its fields. Confirm its synthetic volume `90010` reconciles with TSV volume
    `90010` instead of creating a second zero-file tape.
20. In Settings ▸ **Catalog Data**, confirm invalid CSV cleanup counts and
    removes only quote-polluted CSV records with zero files.
21. Use **Back Up Catalog…** and confirm the resulting SQLite file exists
    without required `-wal` or `-shm` companions. Test reset only with disposable
    data and confirm its automatic backup succeeds first.
22. For a tape whose P5 Location is `<empty>`, confirm Info & Notes shows a dash
    and the sidebar has no map pin. A real shelf, slot, drive, or note should
    display and remain searchable.
23. In Settings ▸ **Catalog Data**, confirm Storage used reports a non-zero
    database total and includes a separate live journal amount when WAL/SHM
    sidecars are present.
24. Choose a Preferred Backup Folder on another mounted drive. Confirm manual
    backup starts there and a disposable catalog reset writes its automatic
    backup there.
25. Disconnect or rename that preferred destination and confirm reset stops
    without changing the catalog.
26. Choose **P5 Archive Browser ▸ Check for Updates…**. Confirm Build 36 checks
    the public GitHub release and does not offer an older build.
27. Create a manual catalog backup and confirm its filename ends in one
    `.sqlite`, not `.sqlite.sqlite`.
28. Import one known six-column TSV and one P5 Web GUI eight-column TSV.
    Confirm **Review Inventory Columns** identifies each profile and that the
    imported file count and total size match the source.
29. Test an eight-column row with an empty trailing checksum. Confirm it remains
    eight columns and imports normally.
30. With disposable test data, try a shifted, mixed, malformed, or unknown TSV
    replacement. Confirm the import stops and the previously imported inventory
    remains searchable.
31. If LTO-5 or LTO-10 samples are available, confirm their sidebar colors,
    filters, sorting, and detail labels. For a size-only estimate, confirm the
    wording says **LTO-X or newer** rather than claiming an exact generation.

## Testing Restore Folder

This is the app's first operation that writes to the P5 server, so please
test it deliberately, on disposable data, before relying on it.

1. In **Settings ▸ Restore**, turn on **Enable P5 Restore**. Confirm the
   context-menu item is absent on folders before you do this, and appears
   immediately afterward — no relaunch required.
2. Set a default destination client (often `localhost`, the P5 server itself)
   and a default destination path, e.g. a scratch `Restore` folder.
3. Right-click a small, disposable folder in **File Browser** and choose
   **Restore Folder from P5 Archive…**.
4. Confirm the sheet shows the expected file count/size, the tape's
   online/offline state, and a computed destination that matches
   `<destination path>/<folder name>/…` — **not** the destination path alone.
5. Confirm, then watch the job run. If the destination path happens to be
   readable from the Mac running Browser, confirm the result screen reports
   an exact match against what was expected.
6. Deliberately test a folder you know is **also archived on a different
   tape**, if one is available. Confirm the result screen reports any extra
   restored files rather than silently absorbing them into "success."
7. Point the destination at a path this Mac cannot read (a different client,
   no shared mount) and confirm the result screen says so plainly, showing
   only P5's own job report with a caveat, rather than a false "success."
8. Check **Settings ▸ Restore** afterward for the "Last restore" summary line.
9. Try **Folder Info** (right-click any folder) and **Search All Tapes ▸
   Folders** — both are read-only and available regardless of the restore
   setting. Confirm a folder's Folder Info total matches what its Folders
   search result shows for the same path.

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
