# GramLingo — App Store Deployment Runbook

Pipeline: **fully automated CI on GitHub Actions (free)**. Push a `v*` tag → both platform workflows build, sign, and upload.

- Android: Ubuntu runner → signed AAB → Google Play (internal track by default)
- iOS: macOS runner (free because this repo is **public**) → IPA → TestFlight

## Status (2026-08-21)

| Item | State |
|---|---|
| Android signing keystore | ✅ Generated (30-yr RSA 2048), backed up |
| Android CI workflow | ✅ Verified — signed AAB builds (JDK 21) |
| iOS CI workflow | ✅ Committed (dormant) |
| iOS icon set | ✅ Generated (full 18-entry AppIcon set) |
| Google Play Console | ⏳ **You need to register** ($25 one-time) |
| Apple Developer | ⏳ **You need to register** ($99/yr) |

---

## 1. Secrets (Settings → Secrets and variables → Actions)

| Secret | Value | Platform |
|---|---|---|
| `ANDROID_KEYSTORE_B64` | `android/keystore/gramlingo-upload.jks` base64-encoded | Android |
| `ANDROID_KEYSTORE_PASSWORD` | value from `android/keystore.properties` → `storePassword` | Android |
| `ANDROID_KEY_ALIAS` | `gramlingo` | Android |
| `PLAY_SERVICE_ACCOUNT_JSON` | Google Play service account JSON (see §2) | Android |
| `VITE_SUPABASE_URL` | from `.env.local` | both |
| `VITE_SUPABASE_PUBLISHABLE_KEY` | from `.env.local` | both |
| `IOS_TEAM_ID` | Apple Team ID | iOS |
| `ASC_API_KEY_B64` | App Store Connect API key `.p8`, base64-encoded | iOS |
| `ASC_API_KEY_ID` | App Store Connect API key ID | iOS |
| `ASC_API_ISSUER_ID` | App Store Connect issuer ID | iOS |

**⚠️ Keystore = your app's identity on Google Play. Losing it = can never update the app.**
Backups live at `C:\Users\hunin\gramlingo-deploy\keystore-backup\`. Keep a copy in a password manager too.

---

## 2. Google Play Console (Android) — you do this

1. Register at https://play.google.com/console → $25 one-time fee.
2. **Create app**: name `GramLingo`, default language, app or game, free. Fill the data safety / privacy (there's already `public/privacy.html`).
3. **App signing**: choose "Google Play App Signing" (default). Upload the **upload key certificate**:
   - Export cert: `keytool -export -rfc -keystore android/keystore/gramlingo-upload.jks -alias gramlingo -file upload_cert.pem`
   - Upload `upload_cert.pem` in Play Console → Setup → App signing.
4. **Service account** (needed for CI auto-upload): Play Console → Setup → API access → Create new service account → link the Google Cloud project → create a service account key (JSON) → grant it **"Release Manager"** role in Play Console.
5. Paste the JSON into the `PLAY_SERVICE_ACCOUNT_JSON` secret.
6. Create the app **releases track** (Internal testing) and add yourself as a tester, or let CI create it via `internal` track upload.

## 3. Apple Developer (iOS) — you do this, later

1. Register at https://developer.apple.com/programs/ → $99/yr.
2. App Store Connect → **My Apps → + → New App**: name `GramLingo`, primary language, bundle ID `com.gramlingo.app` (create the bundle ID in the Developer portal first: Identifiers → register).
3. **App Store Connect API key** (for CI): App Store Connect → Users and Access → Integrations → App Store Connect API → generate key (Admin role) → download `.p8` + note Key ID + Issuer ID.
4. Fill the App Store listing (description, screenshots, privacy policy URL — reuse `gramlingo.online/privacy.html`).
5. Add secrets `IOS_TEAM_ID`, `ASC_API_KEY_B64`, `ASC_API_KEY_ID`, `ASC_API_ISSUER_ID`, then run the iOS workflow.

---

## 4. Release process

```bash
# 1. Build locally first (optional sanity check)
npm run build:mobile

# 2. Tag + push
git tag v1.0.0
git push origin v4 --tags
```

- Android workflow: builds signed AAB → artifact + auto-upload to Play (internal) when service account is set.
- iOS workflow: builds IPA → artifact + TestFlight upload when API key is set.

Version rule: `vMAJOR.MINOR.PATCH` → Android versionCode = `MAJOR*10000 + MINOR*100 + PATCH` (v1.2.3 → 10203).

---

## 5. Local toolchain (this Windows box)

- JDK 21 (Capacitor 8 / AGP 8.13 requires it): `C:\Users\hunin\.workbuddy\toolchain\jdk-21.0.9+10`
- Android SDK: `C:\Users\hunin\.workbuddy\toolchain\android-sdk` (platform 36, build-tools 36, platform-tools)
- Keystore: `android\keystore\gramlingo-upload.jks` + `android\keystore.properties` (both gitignored)
- Backups: `C:\Users\hunin\gramlingo-deploy\keystore-backup\`

iOS cannot be built on Windows (Xcode is macOS-only) — CI is the build machine.
