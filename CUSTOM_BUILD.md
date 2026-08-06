# CC Switch custom Windows build (PR #5671 + #4125 + ksk_ login fix)

Combines:

1. [#5671](https://github.com/farion1231/cc-switch/pull/5671) — proxy stream/response fix
2. [#4125](https://github.com/farion1231/cc-switch/pull/4125) — Kiro native support including `ksk_` API key login
3. **Local fix**: `ksk_` login no longer hard-fails when `GetProfile` returns AccessDenied; validates via `ListAvailableModels` instead and allows empty `profileArn`

## Artifacts

- MSI: `CC-Switch-v3.18.0-pr5671-4125-fix1-Windows.msi`
- Portable: `CC-Switch-v3.18.0-pr5671-4125-fix1-Windows-Portable.zip`
- Release tag: `v3.18.0-pr5671-4125-fix1-win64`
