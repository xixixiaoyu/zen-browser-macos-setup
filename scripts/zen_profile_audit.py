#!/usr/bin/env python3
"""Read-only audit of Zen Browser profiles on macOS."""

from __future__ import annotations

import argparse
import json
import plistlib
import re
from pathlib import Path
from typing import Any


PROFILE_ROOT = Path.home() / "Library/Application Support/zen/Profiles"
APP_PATHS = (Path("/Applications/Zen.app"), Path.home() / "Applications/Zen.app")

TRACKED_PREFS = {
    "zen.updates.last-version": "last_zen_version",
    "zen.view.compact.enable-at-startup": "compact_at_startup",
    "zen.glance.enabled": "glance_enabled",
    "zen.glance.activation-method": "glance_activation",
    "zen.workspaces.force-container-workspace": "container_auto_switch",
    "browser.ctrlTab.sortByRecentlyUsed": "recent_tab_cycling",
    "intl.accept_languages": "website_languages",
    "layout.spellcheckDefault": "spellcheck_default",
    "media.autoplay.default": "autoplay_policy",
    "toolkit.legacyUserProfileCustomizations.stylesheets": "userchrome_enabled",
}

PREF_RE = re.compile(r'^user_pref\("([^"]+)",\s*(.*?)\);\s*$')


def parse_pref_value(raw_value: str) -> Any:
    try:
        return json.loads(raw_value)
    except json.JSONDecodeError:
        return raw_value


def read_prefs(prefs_path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {}
    try:
        lines = prefs_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return result

    for line in lines:
        match = PREF_RE.match(line)
        if match:
            key, raw_value = match.groups()
            if key in TRACKED_PREFS:
                result[key] = parse_pref_value(raw_value)
    return result


def app_version() -> str | None:
    for app_path in APP_PATHS:
        plist_path = app_path / "Contents/Info.plist"
        if not plist_path.is_file():
            continue
        try:
            with plist_path.open("rb") as file:
                info = plistlib.load(file)
        except (OSError, plistlib.InvalidFileException):
            continue
        version = info.get("CFBundleShortVersionString") or info.get("CFBundleVersion")
        if version:
            return str(version)
    return None


def public_container_count(threads: Path) -> int:
    containers_path = threads / "containers.json"
    if not containers_path.is_file():
        return 0
    try:
        data = json.loads(containers_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return 0
    return sum(1 for item in data.get("identities", []) if item.get("public") is True)


def userchrome_state(profile: Path) -> dict[str, Any]:
    css_path = profile / "chrome/userChrome.css"
    if not css_path.is_file():
        return {"exists": False, "hides_zoom_badge": False}
    try:
        css = css_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        css = ""
    return {
        "exists": True,
        "hides_zoom_badge": bool(
            re.search(r"#urlbar-zoom-button\s*\{[^}]*display\s*:\s*none", css, re.S)
        ),
    }


def describe_profile(profile: Path) -> dict[str, Any]:
    prefs = read_prefs(profile / "prefs.js")
    selected = {
        output_name: prefs.get(pref_name)
        for pref_name, output_name in TRACKED_PREFS.items()
    }
    return {
        "profile_path": str(profile),
        "public_containers": public_container_count(profile),
        "userchrome": userchrome_state(profile),
        "preferences": selected,
    }


def collect(profile_override: Path | None) -> dict[str, Any]:
    if profile_override:
        profiles = [profile_override.expanduser().resolve()]
    else:
        profiles = sorted(
            path for path in PROFILE_ROOT.glob("*") if (path / "prefs.js").is_file()
        )

    return {
        "zen_version": app_version(),
        "profile_root": str(PROFILE_ROOT),
        "profiles": [describe_profile(path) for path in profiles],
    }


def print_text(report: dict[str, Any]) -> None:
    print(f"Zen app version: {report['zen_version'] or 'unknown'}")
    print(f"Profile root: {report['profile_root']}")
    if not report["profiles"]:
        print("No Zen profiles with prefs.js were found.")
        return

    for profile in report["profiles"]:
        print(f"\nProfile: {profile['profile_path']}")
        print(f"Public containers: {profile['public_containers']}")
        print(
            "userChrome.css: "
            f"exists={profile['userchrome']['exists']}, "
            f"hides_zoom_badge={profile['userchrome']['hides_zoom_badge']}"
        )
        print("Relevant preferences:")
        for key, value in profile["preferences"].items():
            print(f"  {key}: {value!r}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--profile",
        type=Path,
        help="Audit one profile directory instead of all detected profiles.",
    )
    parser.add_argument("--json", action="store_true", help="Print JSON output.")
    args = parser.parse_args()

    report = collect(args.profile)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_text(report)


if __name__ == "__main__":
    main()
