# Zen Browser macOS Setup

A Codex skill for configuring or auditing Zen Browser on macOS with a focused, Arc-like workflow.

It covers:

- safe one-time browser-data import;
- Single Toolbar, Compact Mode, and toolbar fallbacks;
- workspaces and container-backed account isolation;
- browser and website language preferences;
- recent-order tab switching and shortcut conflict cleanup;
- media autoplay and spellcheck settings;
- optional, narrowly scoped `userChrome.css` adjustments.

## Install

Clone the repository directly into the Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/xixixiaoyu/zen-browser-macos-setup.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/zen-browser-macos-setup"
```

Then invoke `$zen-browser-macos-setup` in Codex.

## Audit

The audit helper is read-only:

```bash
python3 scripts/zen_profile_audit.py
python3 scripts/zen_profile_audit.py --json
```

It does not change Zen settings and does not print browsing history, passwords, cookies, or tab URLs.
