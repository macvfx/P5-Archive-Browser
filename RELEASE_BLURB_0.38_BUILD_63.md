# P5 Archive Browser 0.38 (build 63)

This release is about looking after the catalog: compacting it, backing it up without
stopping work, and a record of what was done to it. Settings also gains a sidebar.

## Compact the catalog

Removing tapes or Archive Groups leaves empty space inside the catalog database, and the
file does not shrink on its own.

- **Settings ▸ Catalog Data** shows the **Reclaimable space**, and the tapes and files
  each Archive Group holds.
- **Tools ▸ Catalog Tools… ▸ Compact Catalog** gives that space back to the disk. It
  removes nothing. It rewrites the whole catalog, so it can take several minutes on a
  large one, and it tells you first if the disk lacks the room it needs.

Reclaimable space usually reads **None**, and that is normal: re-importing a tape reuses
the space it held, and new imports fill any empty space before the file grows. Compact
becomes available once there is at least 16 MB to recover — typically after removing a
number of tapes or resetting the catalog.

## Back up without stopping

- **Catalog Tools is now a window of its own**, so the main window stays usable while a
  backup runs. Close Catalog Tools and reopen it to see the progress or the result.
- A backup shows a **progress bar** and can be **cancelled**, which removes the partial
  file. It checks first that the destination has room.
- Tapes imported while a backup runs are included in it.

## Catalog History

**Tools ▸ Catalog History…** lists every backup, compact, reset and invalid-record
removal: when it started, how long it took, the catalog size before and after, where a
backup went, and how it ended. An operation cut short by quitting the app is marked
interrupted at the next launch. **Export CSV…** saves the list. Recording starts with
this release; earlier backups are not listed.

## Settings has a sidebar

One long form had grown past the window. Settings is now six panes chosen from a list
down the side — **P5 Server**, **Watch Folder**, **Restore**, **Catalog Data**,
**Projects** and **About** — and reopens on the pane last used. Nothing inside them was
renamed, so every "Settings ▸ …" reference in the guide still holds.

## Fixed

- **A rejected certificate gave no way forward.** Tools ▸ Server Info… said the server's
  certificate was not trusted and stopped there. It now offers **Check Certificate…**
  and reloads once the certificate is trusted, and every certificate message says where
  to check it.
- Trusting a certificate from Server Info while Settings was open could be undone by the
  next Save Settings.
- **Open Settings** from a P5 failure now lands on the P5 Server pane.

---

Requires macOS 14.6 or later. Universal, signed and notarized.
