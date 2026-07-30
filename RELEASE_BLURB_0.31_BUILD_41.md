# P5 Archive Browser 0.31 (Build 41)

A small wording fix, no functional change.

## What changed

Folder Info's loading message said "Summing catalog rows…" — internal
implementation terminology, not something a tester needs to parse. It now
says "Counting files and adding up sizes…", matching the plain, action-first
wording already used elsewhere in the app (the restore progress banner's
"Resolving path in P5 archive…", "Verifying restored files…", etc).

## What else is in this release

Everything from build 40 (restore progress tail, empty-window fix), build
39 (path-resolution fix), build 38 (packaging fix), and build 37 (restore
folder, folder sizes). See [Pre-release Notes](RELEASE_NOTES.md) for the
complete current feature set.

## Compatibility

- macOS 14.6 or later.
- No catalog or settings changes from build 40.
