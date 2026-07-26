# P5 Archive Browser 0.21 (Build 36)

Build 36 makes P5 inventory imports schema-safe and extends generation support
from LTO-5 through LTO-10.

## Highlights

- Imports both the six-column P5 Archive Export/direct `nsdchat` inventory and
  P5 Web GUI's eight-column Volume Inventory.
- Shows **Review Inventory Columns** before manual file, folder, or combined
  CSV + TSV import.
- Validates every row before changing the catalog and preserves the previous
  inventory when a replacement is unknown, mixed, malformed, or invalid.
- Reads file size from the correct schema column and preserves an empty trailing
  checksum field.
- Records detected schema and ordered field mapping as inventory-source
  provenance.
- Marks unknown watched layouts as `needs_column_mapping` instead of guessing.
- Adds cyan/teal LTO-5 and magenta LTO-10 indicators, including official LTO-10
  LA/PA media identifiers and `LTO-10` source folders.
- Documents official LTO-5 through LTO-10 native and advertised compressed
  capacities separately from content-size inference.
- Labels size-derived generation as “LTO-X or newer,” not exact media
  identification.

## Compatibility

- macOS 14.6 or later.
- Existing six-column TSV inventories remain supported.
- P5 Web GUI eight-column inventories no longer require conversion.
- Unknown custom TSV layouts are rejected safely; an unrestricted custom field
  mapper is not included in this release.

## Safety

P5 Archive Browser remains read-only toward the P5 server. Inventory imports
change only the local catalog. Back up the catalog from Settings ▸ Catalog Data
before large production tests.
