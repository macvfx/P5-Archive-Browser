# P5 Archive Browser v0.21 (build 36) Pre-release Notes

This pre-release makes P5 inventory imports schema-safe, supports P5 Web GUI
Volume Inventory exports directly, and extends generation recognition and
operator colors from LTO-5 through LTO-10. It also includes the recent Archive
Groups, catalog backup, update checking, and bounded P5 connection work.

## Highlights

- **Review Inventory Columns** identifies the known six-column P5 Archive
  Export/direct `nsdchat` profile and P5 Web GUI's eight-column Volume Inventory
  profile before a manual file, folder, or combined CSV + TSV import.
- The complete TSV is validated before any catalog change. Unsupported, mixed,
  shifted, malformed, nonnumeric-size, and invalid-UTF-8 replacements preserve
  the last good tape inventory.
- The eight-column profile reads size from column 4 rather than mistaking its
  volume identifier for bytes. Empty trailing checksums remain column 8.
- Detected schema, ordered field mapping, source, row count, and imported total
  are retained as inventory provenance.
- Watch folders automatically accept both known profiles. Unknown layouts are
  recorded as needing column review instead of being guessed.
- LTO-5 uses a cyan/teal disc and LTO-10 uses magenta. Filters, sorting,
  details, source-folder recognition, and official LTO-10 LA/PA identifiers
  cover LTO-5 through LTO-10.
- Documentation separates official native and advertised compressed cartridge
  capacities from content-size inference. A size estimate is labeled **LTO-X or
  newer**, never as exact media identification.
- Fast indexed file search across imported tape inventories.
- Files and Projects search modes with Recent and Saved searches.
- Search labels use query-first wording such as `Apple - Files` and
  `Apple - Projects`.
- File results open the matching tape and return to retained search results.
- Project tape rows open the selected project path and return to Project results.
- Large tape inventories load folder by folder instead of constructing the
  complete tree in memory.
- Tape-local searches retain the complete match count and display a bounded
  result list.
- Tape rows identify LTO generation by disc color and show visible indicators
  for a missing barcode, inferred generation, location, and live online/offline
  state. The User Guide includes the complete legend.
- Persistent Archive Groups organize tapes independently from TSV source-folder
  provenance.
- Archive Groups support create, rename, reorder, merge, safe deletion, search,
  multi-selection, and bulk tape moves.
- Collapsed disclosure groups and tape counts keep large sidebars compact.
- Reimports preserve manual Archive Group assignments.
- Combined Archive Folder import loads one top-level volume-list CSV before its
  root and generation-folder TSV inventories.
- Balanced SQL-style outer single quotes are removed from CSV values before
  identity matching. A synthetic `'90010'` CSV volume now reconciles with TSV
  volume `90010`; apostrophes inside legitimate values remain unchanged.
- Settings ▸ **Catalog Data** can remove only quote-polluted CSV-origin records
  with zero imported files. Inventory-bearing tapes are never candidates.
- **Back Up Catalog…** creates a transactionally consistent standalone SQLite
  file while Browser remains open.
- **Back Up and Reset Catalog…** stops the watch folder and requires an
  automatic dated backup before clearing imported tapes, inventories, Archive
  Groups, and watch history. P5/project settings and the Keychain password are
  preserved.
- Catalog Data reports the main database plus active SQLite WAL/shared-memory
  sidecars so operators can see the complete live footprint.
- **Preferred Backup Folder** can target another mounted drive. Manual backup
  panels open there and automatic pre-reset backups use it.
- Manual catalog backup filenames end in exactly one `.sqlite`.
- If that preferred folder is unavailable or not writable, reset stops without
  changing the catalog.
- The app checks public GitHub releases at most once per day and alerts only
  when a newer version/build is available. **Check for Updates…** performs an
  immediate check; downloads remain operator initiated.
- Import File Inventory (TSV)… accepts either one selected TSV from a larger
  folder or the existing folder-based bulk import.
- P5-native Volume Inventory filenames such as the synthetic example
  `90002_vol_inventory.tsv` retain the numeric P5 volume ID and correctly leave
  Barcode empty; `vol_inventory` is a description, not a barcode.
- Build 31's narrowly known mistaken `vol` barcode repairs automatically without
  broadly clearing real, unusual, CSV, P5, or user-entered values.
- Barcode-less tapes with a P5 volume ID offer **Resolve from P5** in Info &
  Notes. The lookup matches P5's volume list by label or numeric ID, then checks
  the individual volume detail.
- When P5 supplies a real label for a numeric TSV stub, the app merges the tape
  identity while preserving searchable inventory and Archive Group placement.
- P5 Location remains a visible, read-only field. `<empty>` displays as a dash
  and does not create a sidebar map pin; genuine shelf, slot, drive, or note
  values still display and remain searchable.
- Durable Watch Folder history records source state, successful fingerprints,
  runs, attempts, interruption recovery, and inventory provenance.
- Bulk and single-tape P5 metadata refreshes run a bounded preflight and display
  a clear stopping message when P5 is unavailable.
- CSV and P5 API metadata provenance is visible separately from TSV inventory.
- P5 Tools lists archive indexes and archive plans.
- Read-only file verification automatically checks all discovered archive
  indexes and can show possible volume, barcode, and P5 location information.
- In-app help explains importing, searching, browsing, verification, and the
  restore handoff.
- Documentation recommends
  [P5 Archive Export](https://github.com/macvfx/p5ArchiveExport)'s Volume Export
  workflow for generating compatible per-volume TSV inventories, the optional
  volume-list CSV, and LTO-generation folders.

## Not included yet

- Portable prepared-database import/export.
- Named multiple P5 servers and server-scoped tape identity.
- Archive Group-bound manual/watch imports and server-routed verification.
- Automatic volume-list CSV watching.
- A user-owned manual barcode override with reported-versus-override provenance.
- An unrestricted custom inventory-column mapper. Unknown layouts stop safely;
  the two validated P5 profiles require no manual mapping.
- A complete operator-facing manual/watch Import History and persistent rotating
  diagnostic logs. Durable watch attempts remain stored internally; these
  operator views are deferred beyond Build 36.
- P5 restore submission or archive submission.
- Moving the active catalog database to another drive.

See [Tester Notes](TESTER_NOTES.md) for installation limitations and the
recommended test pass.
