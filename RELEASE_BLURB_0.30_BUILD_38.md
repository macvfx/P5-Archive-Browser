# P5 Archive Browser 0.30 (Build 38)

Build 38 is a packaging fix: the app now fetches its update-checker component
from a tagged GitHub release instead of a local build-time reference. Nothing
in the app itself changed — same update-check behavior as build 37.

## What's in this release

Everything from build 37, including this pre-release's headline feature:
restoring a whole tape folder's subtree directly from P5 in a single request,
off by default. See [Pre-release Notes](RELEASE_NOTES.md) for the complete
current feature set, or
[RELEASE_BLURB_0.30_BUILD_37.md](RELEASE_BLURB_0.30_BUILD_37.md) for that
build's own notes.

## Compatibility

- macOS 14.6 or later.
- No catalog or settings changes from build 37.

## Safety

Same as build 37: the only operation that writes to the P5 server is a
folder restore the operator explicitly confirms, and it is off by default.
See [Testing Restore Folder](TESTER_NOTES.md#testing-restore-folder) in
Tester Notes before enabling it.
