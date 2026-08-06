# CC Switch custom Windows build (PR #5671 + #4125)

Combines:

1. [#5671](https://github.com/farion1231/cc-switch/pull/5671) — proxy stream/response fix (`395d40b`)
2. [#4125](https://github.com/farion1231/cc-switch/pull/4125) — Kiro (AWS CodeWhisperer/Q) native support including `ksk_` API key login (`8f16a29`)

## Artifacts

- MSI: `CC-Switch-v3.18.0-pr5671-4125-Windows.msi`
- Portable: `CC-Switch-v3.18.0-pr5671-4125-Windows-Portable.zip`
- Release tag: `v3.18.0-pr5671-4125-win64`

## Install (Windows 11 x64)

1. Quit CC Switch completely
2. Install MSI to overwrite existing install (`com.ccswitch.desktop`)
3. Or unzip Portable and run `cc-switch.exe`
4. SmartScreen: More info → Run anyway

## Kiro

Add/configure a Kiro provider and paste API key starting with `ksk_` in the KIRO_API_KEY login UI.
