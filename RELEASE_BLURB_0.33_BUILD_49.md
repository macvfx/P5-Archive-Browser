# P5 Archive Browser 0.33 (Build 49)

Build 49 fixes the Projects search. A project folder could be missing from
**Projects** while **Files** and **Folders** search found the same name
instantly — and a project archived to several tapes was listed as several
unrelated projects.

## What was wrong

**One folder depth cannot describe every storage.** A project is derived from
the folder path, and the app asked for a single depth to apply everywhere. On an
archive where one storage keeps projects under a `Clients` folder and another
keeps them directly under the share, no single number is right for both. Where
the number was one level too shallow, the derived "project" was the container
folder itself, so every project on that storage collapsed into one bucket and
none of their names ever appeared in the Projects list. Files and Folders search
were unaffected, because neither uses this rule — which is exactly why the two
disagreed.

**P5's restore-index prefix broke cross-tape grouping.** When an inventory comes
from a restore index, P5 puts a component of its own in front of every path, and
that component differs on every tape. The Projects list grouped on the derived
path, which carried it. One folder spanning several tapes therefore appeared
once per tape, and every "which tapes hold this project" answer was wrong.

## What changed

- **Detect Roots…** in **Settings ▸ Projects** scans the imported catalog and
  proposes the folder levels whose children look like projects, each with a
  folder count and sample names. Tick the ones that are yours. A project is then
  the folder directly under a root, so each storage can nest differently.
- **Folder depth is counted past P5's restore-index prefix**, so one depth means
  the same thing whether an inventory was imported through a restore index or
  not.
- **A project archived to several tapes is listed once**, with each tape shown
  under it.
- **Why these results?** above the Projects list explains the rule in effect,
  how many files it left without a project, and what it produced per storage —
  flagging any storage that collapsed into a single bucket.

## Also in this release

- **Restore This Folder…** appears when you open a Projects or Folders result,
  running the same preview, confirmation and post-restore reconciliation as the
  folder tree's own restore action. **Browse** now opens the project in the
  folder tree rather than a flat list of matching paths, which had no restore
  action at all.
- The banner says when a project also lives on other tapes, and that a restore
  from there covers the tape you are on. A folder split across tapes needs one
  restore per tape.
- **P5 Location** reads "Not in a library slot" instead of a dash. P5 reports a
  location only while a tape is in a library; for a shelved tape it returns an
  empty value, which was indistinguishable from the app never having asked.
- The search field is pinned to the top of the pane instead of sitting
  mid-window before the first search.

## After upgrading

Project folders are rebuilt once in the background across the whole catalog. The
Projects list fills in as it runs; **Why these results?** shows a rebuilding
indicator while it does. If you then change the rule with Detect Roots, that
starts a second rebuild.

## Known issues

- Restoring individual files rather than a whole folder is not supported yet.
- Folder-size totals do not yet distinguish directory rows in the source TSV
  from files.
