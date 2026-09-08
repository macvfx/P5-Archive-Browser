# P5 Archive Browser 0.31 (Build 44)

Build 44 is a maintenance release. There are no new features and no catalog or
settings changes from build 42; the work is an update-alert fix and a
documentation cleanup.

## The update alert can be dismissed on the first click

The "a new version is available" alert took several attempts to dismiss. It was
attached as a sheet to whichever window happened to be key, and for a transient
panel that meant it could vanish as focus moved, so the click that should have
closed it never reached the button.

Sheets are now attached only to windows that can become main, and the app
activates before presenting the alert, so the first click lands. The shared
update-checker package requirement is raised to 1.0.2 so the fix is a stated
dependency rather than whatever version happens to resolve.

This landed in build 43, which was never published; build 44 is the first
release to carry it.

## Documentation

The API investigation report is rebuilt from its Markdown source, and the probe
scripts' usage examples now name an example host rather than a literal address.

## Upgrading

- No catalog or settings changes from build 42. Existing imported volumes,
  archive groups, notes, and settings are carried over untouched.
- Restore remains off by default. If you enabled it, that setting is preserved.

## Known issues

- Restoring individual files rather than a whole folder is still unsupported: it
  needs per-entry containment behaviour verified first, and per-file selections
  are known to flatten the restored tree without it.
- Folder-size totals sum the app's own imported catalog rows and do not yet
  distinguish directory rows in the source TSV from files.
