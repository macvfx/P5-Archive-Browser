# P5 Archive Browser v0.20 (Build 35)

Build 35 makes large local catalogs easier to manage and adds the same public
GitHub update-check workflow used by the other P5 apps.

## What changed

- **Catalog storage total:** Settings ▸ Catalog Data reports the main SQLite
  database plus active WAL and shared-memory sidecars.
- **Preferred Backup Folder:** Manual backup panels start in the chosen folder,
  and automatic pre-reset backups use it. The destination can be on another
  mounted drive.
- **Unavailable-drive protection:** If the preferred backup folder is missing
  or not writable, reset stops before changing the catalog.
- **Clean backup names:** Manual backups end in exactly one `.sqlite`.
- **Public update checks:** Browser checks
  `macvfx/P5-Archive-Browser` at most once per day and alerts only when a newer
  version/build exists. **P5 Archive Browser ▸ Check for Updates…** performs an
  immediate check.

Update checks read public GitHub release metadata only. Browser never downloads
or installs an update automatically; **Download** opens the public release page.

Moving the active catalog database to another drive remains planned. That will
require a guarded backup, database close, verified copy, relaunch, and rollback
workflow rather than moving an open SQLite file.

This remains a read-only archive-catalog application. It does not load tapes,
restore files, submit archive jobs, or modify data on the P5 server.

See the
[Tester Notes](https://github.com/macvfx/P5-Archive-Browser/blob/main/TESTER_NOTES.md)
for the recommended test pass and the
[full pre-release notes](https://github.com/macvfx/P5-Archive-Browser/blob/main/RELEASE_NOTES.md)
for the complete feature list.
