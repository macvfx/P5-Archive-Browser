# P5 Archive Browser 0.30 (Build 37)

Build 37 adds this app's first operation that writes to the P5 server:
restoring a whole tape folder directly from P5, off by default. It also adds
read-only folder-size summaries.

## Highlights

- Restores a whole tape folder's subtree from P5 in a single request — one
  directory handle restores the entire tree, confirmed against a live P5
  8.0.4 server. Off by default; turn on in **Settings ▸ Restore**.
- The confirmation sheet shows the expected file count/size from the local
  catalog (not P5's directory listing), the tape's online/offline state, and
  the exact computed destination — a restore always creates a new folder
  named after the source folder and never overwrites the destination path
  itself.
- After the job completes, the app independently verifies what landed
  against what was expected whenever the destination is readable from this
  Mac, instead of trusting a completed P5 job — P5 has been observed to
  report success while omitting files.
- Adds **Folder Info** (right-click any folder) and a **Folders** search
  scope in Search All Tapes: recursive file count and size, rolled up across
  every tape holding part of a folder.
- Adds a smoke test covering the new restore preview, folder-size queries,
  and a byte-level (not count-level) restore reconciliation check.

## Compatibility

- macOS 14.6 or later.
- Existing catalogs and imports are unaffected; the new local `restore_history`
  log is an additive database change.

## Not included yet

- Restoring an **individual file** — only whole-folder restore is supported.
  Restore the containing folder instead, or use your normal P5 workflow.
- Overwrite behavior into an already-populated destination has not been
  characterized — use an empty or dedicated destination.

## Safety

P5 Archive Browser's only write operation against the P5 server is a
folder restore the operator explicitly confirms, and it is off by default.
Every other operation — inventory import, search, browsing, Folder Info,
verification — remains local-catalog or read-only against P5, exactly as
before. Back up the catalog from Settings ▸ Catalog Data before large
production tests, and test restore itself against disposable data first —
see [Testing Restore Folder](TESTER_NOTES.md#testing-restore-folder) in
Tester Notes.
