# P5 Archive Browser v0.19 (Build 33)

Build 33 adds safer catalog maintenance and fixes metadata reconciliation
problems found while testing P5 exports.

## What changed

- **Catalog backup:** Settings ▸ Catalog Data can create a consistent,
  standalone SQLite backup while the app remains open.
- **Guarded catalog reset:** Back Up and Reset Catalog stops the Watch Folder
  and requires an automatic dated backup to succeed before imported tapes,
  inventories, Archive Groups, and watch history are cleared. P5/project
  settings and the Keychain password are preserved.
- **Quoted CSV repair:** Balanced SQL-style outer single quotes are removed
  before matching volume IDs, labels, and barcodes. Settings can also remove
  narrowly identified quote-polluted CSV records when they contain no imported
  files.
- **Location display:** P5 Location remains visible and read-only. P5's
  `<empty>` sentinel displays as a dash and no longer creates a sidebar map pin;
  genuine shelf, slot, drive, or note values still display and remain
  searchable.
- **Import guidance:** The documentation now distinguishes the supported
  six-column P5 Archive Export/direct `nsdchat` TSV layout from Archiware's
  currently unsupported eight-column Web UI layout.

Build 33 also includes the v0.19 Archive Groups, durable Watch Folder history,
single-file TSV selection, P5-native `vol_inventory` filename handling,
barcode resolution by P5 volume ID, and bounded P5 connection preflights.

## Important TSV compatibility note

Use the six-column order:

```text
index path, ppath, size, handle, btime, mtime
```

Do not import the eight-column P5 Web UI order yet. It moves file size from
column 3 to column 4 and requires the schema-aware importer planned for a later
build.

This remains a read-only archive-catalog application. It does not load tapes,
restore files, submit archive jobs, or modify data on the P5 server.

See the
[Tester Notes](https://github.com/macvfx/P5-Archive-Browser/blob/main/TESTER_NOTES.md)
for the recommended test pass and the
[full pre-release notes](https://github.com/macvfx/P5-Archive-Browser/blob/main/RELEASE_NOTES.md)
for the complete feature list.
