# P5 Archive Browser v0.19 (build 31) Pre-release Notes

This pre-release adds durable user-managed catalog organization and prevents an
unreachable P5 server from turning one metadata refresh into repeated per-tape
timeouts.

## Highlights

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
- P5 restore submission or archive submission.

See [Tester Notes](TESTER_NOTES.md) for installation limitations and the
recommended test pass.
