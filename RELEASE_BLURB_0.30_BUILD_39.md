# P5 Archive Browser 0.30 (Build 39)

Build 39 fixes a real Restore Folder bug found during testing: a folder P5
had actually archived could be reported as "was not found in N archive
index(es) across N client(s)."

## What was wrong

Browser's own catalog paths never carry a leading slash. P5's
`GET /archive/entries` (used to resolve a folder to a restorable handle) has
been observed live to require a leading slash for some archived paths and
reject it for others. Browser only ever sent the no-slash form, so any
folder whose archive index needed the leading slash failed to resolve —
even though it was genuinely archived and Folder Info (a separate, local-only
check) could see it fine.

## The fix

Path resolution now tries both forms — as stored, and with the leading
slash toggled — before reporting not-found. Reproduced and verified against
a disposable P5 server with a synthetic nested, space-containing path shaped
like a real tester report (`Example Client/Sample Project/Footage`): the
no-slash form returned `unknown entry`, the leading-slash form resolved
correctly.

## What's in this release

Everything from build 37 (restore folder, folder sizes) and build 38
(packaging fix). See [Pre-release Notes](RELEASE_NOTES.md) for the complete
current feature set.

## Compatibility

- macOS 14.6 or later.
- No catalog or settings changes from build 38.

## Safety

Same as build 37/38: the only operation that writes to the P5 server is a
folder restore the operator explicitly confirms, and it is off by default.
If you saw the "not found" error on an earlier build, please retest — see
[Testing Restore Folder](TESTER_NOTES.md#testing-restore-folder) in Tester
Notes.
