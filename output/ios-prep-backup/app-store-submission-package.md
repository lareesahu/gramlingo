# GramLingo — App Store Submission Package

**Prepared:** 2026-08-12
**Status:** Code + assets ready; requires macOS build/sign + Apple Developer account to submit.

---

## 1. App Store Connect Metadata (draft — confirm before submit)

| Field | Value |
|---|---|
| **App Name** | GramLingo — Grammar Quest |
| **Subtitle** | Learn English grammar by playing |
| **Primary Category** | Education |
| **Secondary Category** | Games > Word |
| **Age Rating** | 4+ (no objectionable content; review App Store questionnaire) |
| **Price** | Free (no IAPs currently) |
| **Languages** | English (primary), Simplified Chinese, Spanish |
| **Bundle ID** | com.gramlingo.app |
| **SKU** | gramlingo-ios-0001 |

### Keywords (comma-separated, ≤100 chars)
`grammar,english,learn english,grammar game,esl,language,vocabulary,flashcards,quiz,practice`

### Description (draft)

> Master English grammar the fun way. GramLingo turns grammar rules into
> bite-sized quests with a friendly mascot, Gramlin, guiding you through 12
> grammar worlds — from relative clauses to advanced expressions.
>
> Each lesson gives instant feedback and clear explanations, so you learn *why*
> an answer is right, not just whether it is. Track your progress, collect
> stars, and watch your mistakes turn into your strongest points with the
> built-in Wrong Book.
>
> • 280+ hand-crafted grammar questions across 12 modules
> • Flashcards for vocabulary families and irregular verbs
> • Trilingual support (English, 中文, Español)
> • Offline progress — your place saves automatically
> • The Wrong Book: revisit and master your mistakes
>
> Perfect for exam prep, professional polish, or daily practice.

### App Review Notes (draft — tell reviewers how to test)

> GramLingo requires an account to access lessons. Use these demo credentials:
> **Email:** reviewer@gramlingo.test
> **Password:** Gramlin2026!
>
> Or create a free account in-app (email confirmation may be required — check
> inbox). The core experience is the Grammar panel (Relative Clauses is the
> first module) and the Flashcards panel.

---

## 2. Privacy / Compliance Checklist

- [x] Privacy policy URL: `https://lareesahu.github.io/gramlingo/privacy.html`
- [x] In-app privacy policy link (AuthScreen footer)
- [x] No third-party analytics / ads / tracking SDKs
- [x] No camera / mic / location / contacts permissions
- [ ] **Confirm privacy policy contact email** — currently `support@gramlingo.app` (placeholder — verify the real support inbox)
- [ ] App Privacy "Data Collection" declarations in App Store Connect:
  - Account email + password (Account Info)
  - Learning progress (Usage Data) — only if cloud sync is on; local mode stores on-device only

---

## 3. What still needs a Mac (NOT doable on Windows)

1. **Build the iOS app** — `npx cap sync ios` then open in Xcode, set signing
   team, archive.
2. **Code signing** — Apple Developer account ($99/yr), certificates &
   provisioning profiles.
3. **TestFlight** — upload build, internal testing.
4. **Submit** — App Store Connect upload + review.

### Command sequence (run on a Mac with Xcode installed)

```bash
cd gramlingo
npm install
npm run build:mobile        # vite build --base=./
npx cap sync ios            # copies dist + plugins into ios/
npx cap open ios            # opens Xcode
# In Xcode: select "App" target → Signing & Capabilities → select team
# Product → Archive → Distribute App → App Store Connect
```

---

## 4. Screenshots (App Store requires specific sizes)

Required sizes (iPhone):
| Device | Resolution (px) |
|---|---|
| 6.9" (iPhone 15 Pro Max / 16 Pro Max) | 1290 × 2796 |
| 6.7" (iPhone 14 Pro Max) | 1290 × 2796 |
| 6.5" (iPhone 14 Plus) | 1284 × 2778 |
| 6.1" (iPhone 14 Pro) | 1179 × 2556 |
| 5.5" (iPhone 8 Plus) | 1242 × 2208 |

Recommended screenshot set (capture on device/simulator):
1. Welcome / landing (hero with Gramlin)
2. Learning path (module gallery)
3. Lesson question (multiple choice)
4. Answer feedback (correct + explanation)
5. Flashcards (word family lesson)
6. Wrong Book (error log)

**TODO:** capture these on a simulator (or use the existing web build rendered
at these viewports). Screenshots must NOT be pre-generated mockups with fake
device frames — Apple prefers real captures.

---

## 5. Open items before first submit

| # | Item | Owner | Blocker? |
|---|---|---|---|
| 1 | Confirm privacy policy contact email | Lareesa | No (soft) |
| 2 | Curriculum Category A/D fixes | Lareesa (approve plan) | No (content quality, not rejection) |
| 3 | Apple Developer account + signing | Lareesa | **YES** — cannot build/sign without |
| 4 | Mac for Xcode build | Lareesa | **YES** |
| 5 | App Store screenshots | Lareesa / Mac | No (can reuse web captures) |
| 6 | Demo/reviewer account provisioned in Supabase | Lareesa | Soft — reviewers need access |

---

## 6. iOS-specific config already applied

- [x] Safe-area insets (`viewport-fit=cover`, `env(safe-area-inset-*)`) in tokens + shell
- [x] `ios.contentInset: automatic` in capacitor.config.ts
- [x] Portrait + landscape orientations in Info.plist
- [x] App icon (1024×1024, no alpha) — real GramLingo mascot
- [x] Splash screens (2732×2732 ×3 scales) — real branding
- [x] Loading-screen hang fixed (falls back to welcome if Supabase unreachable)
- [x] Service worker + PWA manifest (offline support)
- [x] Privacy policy linked in-app

---

## 7. Recommended pre-submit QA (real browser, not headless)

Run once on a real iPhone/Simulator:
1. Cold launch → welcome screen (not stuck loading)
2. Create account → email confirmation → login
3. Complete one lesson → progress persists after relaunch
4. Switch language (EN/中文/ES) → question text + UI update
5. Airplane mode → app still opens (offline PWA/local mode)
6. Notch devices → no content under the Dynamic Island / home indicator
