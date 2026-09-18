# P5 Archive Browser 0.37 (build 56)

Two changes: the app can now reach P5 over TLS, and the things you *do* have moved
out of Settings into a Tools menu.

## HTTP or HTTPS

P5 serves the same REST API in the clear on port 8000 and over TLS on port 8443.
Measured against a live server, the TLS port answers with the same paths and bodies
as the plain one. Which one a server offers is decided when P5 is installed, so this
is a setting rather than an assumption — of three servers checked, 8443 answered on
one and not on another.

An existing configuration is untouched and stays on HTTP. Choosing HTTPS moves the
port to 8443 unless you typed one yourself.

## Certificate checking

P5 ships a self-signed certificate whose subject identifies nothing, and macOS will
not accept it. Choosing HTTPS without settling that would not give a secure
connection — it would give no connection.

- **Check Certificate** shows the SHA-256 fingerprint and subject of the certificate
  the server actually presents, and whether macOS trusts it.
- Trusting it once records that exact certificate. If the server later presents a
  **different** one, the connection is refused rather than quietly accepted, and the
  sheet says so before you can accept the new one.
- A server whose administrator installed a real certificate needs no trusting at all.

The setting applies to everything the app asks P5 — volume syncs, archive lookups,
restores and job status — not only to Test Connection.

## A Tools menu

Settings had grown to seven sections holding both what you configure and what you do.
The actions have moved to a new Tools menu, and Settings is back to preferences.

- **Tools ▸ Server Info…** — the archive indexes and plans the server is configured
  with. Read-only, and the quickest way to confirm a server, its port, protocol,
  certificate and password all work. Plans that delete the source after archiving are
  flagged. The **Server Info** button on a tape header opens the same sheet; it was
  previously called *P5 Tools* and showed the same thing under a second name.
- **Tools ▸ Discover New Volumes from P5** — the same action as the Sync button in the
  toolbar. Both are offered because only a menu item can be found by searching the
  Help menu.
- **Tools ▸ Catalog Tools…** — back up, remove records left behind by a malformed CSV,
  or back up and reset. Where backups are written stays in Settings.

## Fixed

- A certificate that did not match the one trusted reported itself as "cancelled",
  which read as though you had stopped the request yourself.
- An error from an earlier attempt could still be shown after a later one succeeded —
  a certificate warning, for instance, surviving the certificate being trusted.

---

Requires macOS 14.6 or later. Universal, signed and notarized.
