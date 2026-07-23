# P5 Archive Browser Pre-release Notes

This pre-release focuses on making a large exported P5 catalog practical to
search, browse, and compare with the live P5 archive indexes.

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
- CSV and P5 API metadata provenance is visible separately from TSV inventory.
- P5 Tools lists archive indexes and archive plans.
- Read-only file verification automatically checks all discovered archive
  indexes and can show possible volume, barcode, and P5 location information.
- In-app help explains importing, searching, browsing, verification, and the
  restore handoff.

## Not included yet

- Combined CSV+TSV first-run import.
- Portable prepared-database import/export.
- Automatic TSV watch folders.
- P5 restore submission or archive submission.

See [Tester Notes](TESTER_NOTES.md) for installation limitations and the
recommended test pass.
