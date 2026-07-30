# CC Switch custom Windows build (PR #5671)

This branch packages a **custom Windows x64 build** of [CC Switch](https://github.com/farion1231/cc-switch) that includes the still-pending fix from:

- PR: https://github.com/farion1231/cc-switch/pull/5671
- Commit: `395d40b67858f4fa5f8c3aa7522ddf5b12d611fb`
- Title: `fix(proxy): handle wrapped chat responses and repeated stops`

## What is fixed

- Unwrap non-standard OpenAI Chat Completions responses nested under `data` when top-level `choices` is absent
- Delay Anthropic content-block closure until the upstream stream actually ends (tolerate repeated `finish_reason: stop`)

## Artifacts

GitHub Actions builds on push / `workflow_dispatch`:

- MSI installer: `CC-Switch-v3.18.0-pr5671-Windows.msi`
- Portable zip: `CC-Switch-v3.18.0-pr5671-Windows-Portable.zip`

Release tag: `v3.18.0-pr5671-win64`

## Install / overwrite existing CC Switch (Windows 11 x64)

1. Fully quit CC Switch (tray icon → Quit)
2. Install the MSI (recommended) — same app id `com.ccswitch.desktop`, so it should overwrite/upgrade the existing install
3. Or unzip Portable and run `cc-switch.exe`
4. If SmartScreen blocks: More info → Run anyway

## Notes

- This is an **unsigned** custom build (no official Tauri/updater signing key)
- Auto-updater artifacts are disabled so official releases won't silently replace this custom build via updater packages generated here
- Revert to official once PR #5671 is merged and released
