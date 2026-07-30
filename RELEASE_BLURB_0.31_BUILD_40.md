# P5 Archive Browser 0.31 (Build 40)

Build 40 fixes a UI bug reported during Restore Folder testing and adds a
mid-run progress indicator for restore jobs.

## What was wrong

After a restore completed — or when opening Folder Info — a small, wordless,
empty window could appear. It only closed by pressing Escape, after which
retrying the same action worked normally. The restore confirmation, restore
result, and Folder Info windows were all driven by a SwiftUI pattern where a
separate on/off flag and a separate piece of content data could briefly fall
out of sync, letting the window appear before its content was ready.

## The fix

All three windows now use a presentation pattern where the window and its
content are the same piece of state — there's no separate flag to
desynchronize, so an empty window can't appear.

## What else is in this release

The restore progress banner now also shows a few lines from P5's own
detailed job report underneath the status line, refreshed every few
seconds. P5's job status has no distinct state for "waiting on a tape to
load" — a blocked job just reports "running," the same as one actively
copying files — so this is the closest available signal to what a job is
doing right now. This has not yet been confirmed against a real tape-load
wait; testing so far has used a disk-based archive pool rather than tape
hardware.

Everything from build 37 (restore folder, folder sizes), build 38
(packaging fix), and build 39 (path-resolution fix) is also included. See
[Pre-release Notes](RELEASE_NOTES.md) for the complete current feature set.

## Compatibility

- macOS 14.6 or later.
- No catalog or settings changes from build 39.

## Safety

Same as build 37–39: the only operation that writes to the P5 server is a
folder restore the operator explicitly confirms, and it is off by default.
If you saw the empty-window issue on an earlier build, please retest — see
[Testing Restore Folder](TESTER_NOTES.md#testing-restore-folder) in Tester
Notes.
