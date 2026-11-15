# Zen on macOS: setup and verification matrix

Use this reference for ordinary setup and audit work. Labels were checked against Zen 1.24.2b on macOS, but Zen changes labels frequently. Prefer the visible UI and verify at the end.

## 1. Preflight

1. Open Zen and check the version in `Settings → About Zen` (Chinese UI: `设置 → 关于 Zen`).
2. Run the read-only audit helper:

   ```bash
   python3 scripts/zen_profile_audit.py
   ```

3. Treat these as private: profile paths, tab titles and URLs, history, cookies, saved passwords, container names that reveal identities, and account pages.
4. Ask before restarting if the session may contain unsaved form data.

## 2. Import from Arc

Use `Settings → Account and sync → Import data` (Chinese: `设置 → 账户与同步 → 导入数据`).

- Confirm that the desired Arc profile is the source.
- Select only the data categories the user intends to import.
- Import once. Repeating an import can duplicate bookmarks, history, pinned tabs, or workspace content.
- After import, verify spaces/workspaces, pinned tabs, Essentials, bookmarks, history, and passwords.
- Do not claim a profile restriction unless the current import UI explicitly says so.

## 3. Layout and compact mode

Open `Settings → Look and Feel` (Chinese: `设置 → 界面外观`).

Available layouts may include:

- `Only Sidebar` / `仅侧边工具栏`: single toolbar integrated into the vertical sidebar.
- `Sidebar and Top Toolbar` / `侧边+顶部工具栏`: full top address bar plus vertical tabs.
- `Collapsed Sidebar` / `折叠工具栏`: mostly hidden sidebar and top toolbar.

Recommended daily default: `Only Sidebar` plus Compact Mode.

Compact Mode can be toggled from the UI or from `Settings → Keyboard Shortcuts → Compact Mode`. Verify the actual assigned keys rather than assuming a platform default.

## 4. Workspaces and containers

1. Confirm that container tabs are enabled. Search Settings for `容器标签页` or `Container Tabs`.
2. Right-click a workspace name in the sidebar.
3. Choose `Set Profile`, then an existing container or `Add new container`.
4. Give each identity-oriented workspace a distinct default container.
5. Enable `Switch to workspace where container is set as default when opening container tabs` when automatic routing matches the user's intent.

Container isolation applies to cookies and sessions, not to the browser's entire history or extension storage. Explain this limitation when identity separation is the goal.

## 5. Language and spelling

Open `Settings → Languages` (Chinese: `设置 → 语言`).

- Set the browser UI language explicitly.
- Put website languages in intended priority order. A typical Chinese-first order is `zh-CN, zh, en-US, en`.
- If the Add button does not work in a particular Zen build, use `about:config` and set `intl.accept_languages` through the UI. Do not edit `prefs.js` while Zen is running.
- Turn off `Check spelling as you type` when red dotted underlines are unwanted.
- A right-click toggle on one text field can be reset when a site re-renders. The Settings checkbox is the durable control.

Account websites such as Google can keep a separate language preference. Changing the browser locale does not necessarily override the account UI.

## 6. Tab switching and tab pinning

For most-recently-used order:

1. Search Settings for `Ctrl+Tab`.
2. Enable `Cycle through tabs in recently used order`.
3. Verify that Ctrl+Tab returns to the previous tab and Ctrl+Shift+Tab reverses direction.

To clear macOS `Command+1` through `Command+9` tab selection:

1. Open `Settings → Keyboard Shortcuts`.
2. Expand `Navigation`.
3. Clear `Go to Tab 1` through `Go to Tab 8` and `Go to Last Tab`.
4. Test one cleared key to confirm it no longer switches tabs.

The default Mac pin/unpin shortcut is usually `Shift+Command+D`; verify it in the current Keyboard Shortcuts UI. Essentials is a separate level and normally has no default add shortcut.

## 7. Shortcut collision handling

On macOS, check the full combination before assigning it:

- `Option+Command+C` commonly triggers developer inspection.
- `Option+Command+S` can already mean `Toggle Floating Sidebar`.
- `Command+S` can conflict with saving a page depending on the build.

If changing Compact Mode to `Option+Command+S`, move or clear the existing floating-sidebar assignment first. A non-conflicting choice used in the reference setup was:

- Compact Mode: `Option+Command+S`
- Floating Sidebar: `Option+Command+B`

Do not assume these are universal defaults. Read the labels from the current UI.

## 8. Media and autoplay

Search Settings for `Autoplay` (`自动播放`).

- `Block Audio` is the privacy-preserving default.
- `Allow Audio and Video` is global. Only choose it when the user explicitly accepts audible autoplay on all websites.
- If only one site should be exempt, use a site-specific exception rather than changing the global default.
- Some video sites may mute themselves when audible autoplay is blocked, producing a site message such as “started muted”.

## 9. Extensions

- Prefer a minimal extension set.
- uBlock Origin is the default content-blocking recommendation.
- Automatic tab-discarding extensions are not universal defaults. Test memory behavior with Zen's native unloading before adding one.
- If the user disables or removes an extension, do not reinstall it without a new request.
- Check `about:addons` after installation or removal; a disabled extension is not the same as an uninstalled one.

## 10. Verification and rollback

After setup:

1. Confirm layout, compact state, and sidebar invocation.
2. Switch workspaces and confirm container identity behavior.
3. Verify browser and content languages on a fresh page.
4. Verify Ctrl+Tab recent order and cleared system-conflicting shortcuts.
5. Verify spellcheck, autoplay, and extension state.
6. Restart only if the UI says a restart is required; then confirm the state survived.

Record the before/after values for each non-default choice so the user can reverse it.
