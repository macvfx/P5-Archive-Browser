# P5 Archive Browser 0.31 (Build 42)

Build 42 fixes a real bug found during restore testing against actual tape
hardware: a restore could be reported as a failed mismatch while P5 was
still legitimately working.

## What was wrong

A restore needing a tape that wasn't currently loaded caused P5 to enter a
genuine wait state — it can take a while for an operator to load the right
cartridge. But the app was only ever watching a restore job for 10 minutes.
When that window elapsed without P5 reporting a final status, the app
incorrectly treated the job as finished: it checked whatever files had
landed on disk so far and reported a mismatch, even though P5's job was
still alive and actively waiting on the tape. The job itself hadn't failed,
and hadn't even been stopped — the app had simply stopped watching and drew
the wrong conclusion from a partial, still-changing result.

## The fix

The app now clearly distinguishes "P5 reported the job is done" from "I
stopped watching." A timeout no longer produces a false mismatch — it now
says plainly that the job may still be running, e.g. waiting on a tape, and
skips file-by-file verification entirely rather than checking a moving
target. The default watch window was also raised from 10 minutes to 1 hour,
since a real tape wait can legitimately take that long. Cancel remains
available and responsive the entire time.

This testing also confirmed that a single folder can legitimately be
archived across more than one tape at once — something the restore
confirmation sheet already accounts for with a caveat, so no change was
needed there.

## What else is in this release

Everything from build 41 (wording fix), build 40 (restore progress tail,
empty-window fix), build 39 (path-resolution fix), build 38 (packaging
fix), and build 37 (restore folder, folder sizes). See
[Pre-release Notes](RELEASE_NOTES.md) for the complete current feature set.

## Compatibility

- macOS 14.6 or later.
- No catalog or settings changes from build 41.

## Safety

Same as build 37–41: the only operation that writes to the P5 server is a
folder restore the operator explicitly confirms, and it is off by default.
If you saw a false mismatch report on an earlier build for a restore that
needed a tape, please retest — see
[Testing Restore Folder](TESTER_NOTES.md#testing-restore-folder) in Tester
Notes.
