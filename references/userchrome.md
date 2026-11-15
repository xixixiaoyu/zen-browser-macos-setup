# Narrow `userChrome.css` adjustments

Use custom CSS only when Zen exposes no suitable built-in setting and the user accepts that future Zen updates may require maintenance.

## Location and activation

1. Find the active profile by opening `about:support` and using the profile-folder action.
2. Create `chrome/userChrome.css` inside that profile.
3. In `about:config`, set `toolkit.legacyUserProfileCustomizations.stylesheets` to `true`.
4. Restart Zen once.

Do not edit `prefs.js` directly while Zen is running.

## Hide the URL-bar zoom badge

Use this exact rule when the user wants the `110%`-style badge hidden but wants the page zoom itself preserved:

```css
/* Hide the URL bar zoom-level badge while preserving page zoom. */
#urlbar-zoom-button {
  display: none !important;
}
```

Verify that page zoom still works with the browser zoom commands and that only the badge disappeared.

## Rollback

- Remove the rule from `userChrome.css`, or remove the file if it contains no other customizations.
- Restart Zen.
- Optionally reset `toolkit.legacyUserProfileCustomizations.stylesheets` to `false` when no other custom styles are in use.

Keep custom CSS limited to the requested selector. Do not bundle unrelated visual overrides.
