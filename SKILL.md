---
name: zen-browser-macos-setup
description: Configure or audit Zen Browser on macOS for a focused, Arc-like workflow, including import, layout, compact mode, workspaces and containers, language, tab switching, media permissions, and optional UI tweaks.
---

# Zen Browser macOS Setup

Set up or audit Zen Browser on macOS without silently changing unrelated browser state. Preserve existing tabs, workspaces, containers, passwords, and browsing data.

## Workflow

1. Inspect Zen before changing it. Run `python3 scripts/zen_profile_audit.py` to get a read-only summary of every local profile.
2. Decide whether the task is a fresh setup, a migration from another browser, or an audit of an existing setup. Do not repeat an Arc import on a profile that already contains imported spaces or Essentials.
3. Use Zen's visible settings and Computer Use for live changes. Do not edit `prefs.js`, session files, or browser databases while Zen is running.
4. Apply only the requested choices. Configuration is preference-driven; do not treat every recommended item as mandatory.
5. Verify each change in the UI or with the audit script. If a change requires restart, warn about unsaved forms and use the normal quit/reopen flow.

## Recommended Defaults

- Use Single Toolbar with Compact Mode for a focused daily setup. Keep the full top toolbar when frequent URL copying or web debugging matters more than vertical space.
- Use Ctrl+Tab in most-recently-used order when this matches the user's habits.
- Set the browser UI language explicitly. Set website languages in the intended priority order instead of assuming the OS locale propagates.
- Use workspaces with one explicit default container per identity. Enable automatic switching when a container opens outside its workspace.
- Keep extension count small. uBlock Origin is useful; automatic tab-discarding extensions are optional, and native unloading is enough unless memory tests show a concrete need.
- Keep the Find in Settings search open while configuring because Zen frequently changes labels and setting locations.

## Required Checks

- Before import: confirm the source and ensure the import will not duplicate tabs, pinned tabs, bookmarks, history, or passwords.
- Before changing shortcut assignments: search for the same key combination because macOS and built-in Firefox actions can win over Zen actions.
- Before enabling autoplay globally: explain that the setting affects all sites; offer a site-specific exception when the request is limited to one website.
- Before adding custom CSS: prefer built-in settings, keep selectors narrowly scoped, and record how to undo the change.
- After changing language, spellcheck, shortcuts, or compact-mode behavior: reload or restart as required and verify the actual result.

## Detailed Guidance

- Read [references/macos-setup-matrix.md](references/macos-setup-matrix.md) for the settings map, verification steps, restore paths, and known macOS shortcut collisions.
- Read [references/userchrome.md](references/userchrome.md) only when a built-in setting cannot satisfy a narrowly scoped visual request.

## Helper

`scripts/zen_profile_audit.py` is read-only. It reports Zen version, profile locations, selected relevant preferences, public container count, and whether `userChrome.css` exists. Use `--json` for machine-readable output. Never copy the audit output wholesale into a skill or public repository because profile paths and browser state may be private.
