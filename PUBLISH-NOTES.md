# 📋 Shristi Birthday Site — Publishing Notes

*(Context file for future sessions — read this before publishing!)*

## What this is
A birthday surprise site for **Shristi** (birthday: **26 November**), duplicated from Gungun's site in this repo.

- **Site source:** `shristi/` folder (`index.html` + `media/photo1–7` — her 7 photos)
- **Shared assets (repo root):** `Music.mp3`, `gift_flowers.jpg`, `gift_chocolate.jpg`, `gift_rasmalai.jpg`, `gift_panipuri.jpg`, `gift_coffee.jpg`
- **Ready-to-upload package:** `publish-upload.zip` (site + assets, paths already fixed for standalone hosting)
- **Personalized:** name Shristi · coupons `SHRISTIPURIYAN` / `SHRISTIMALAI` / `SHRISTICOCO` / `SHRISTICOFFEE` · expiry 26th November 2027 · WhatsApp redeem: 7654339871 · mobile full-screen home page · Cheenu & Lalo message removed (replaced by the coffee coupon)

## Target repo
**https://github.com/happyhaiabhi/Happy-Birthday-Shristi** (public, branch `main`)

## Upload steps (for the next session)
1. Extract `publish-upload.zip` → upload **ALL** files to the repo root (git push, or the user via the GitHub web UI: Add file → Upload files).
2. The user adds two videos with **EXACT names** at the repo root:
   - `cake.mp4` — "Cut the Cake" page
   - `special.mp4` — the special video gift
   (Source: user's Google Drive folder `18t57-rpHLQ42iha3sEjXo9SCtpHl85Nk` — the sandbox cannot download from Drive. The pages show photo posters meanwhile, so nothing looks broken.)
3. Enable GitHub Pages: Settings → Pages → Source: **Deploy from a branch** → `main` / `(root)` → Save.
4. Live URL: **https://happyhaiabhi.github.io/Happy-Birthday-Shristi/**

## ⚠️ GitHub access
The sandbox GitHub token (Arena GitHub App) is authorized only on `happyhaiabhi/HappyBirthDayGunun` — pushing to Happy-Birthday-Shristi fails with *"Resource not accessible by integration"*. To publish **from the sandbox**, the user must reconnect GitHub in Arena and grant the app access to **Happy-Birthday-Shristi** as well. Otherwise the user can upload the zip contents via the GitHub web UI themselves.

## Preview server
`python3 _serve_preview.py` serves the repo on port 8080; `/` redirects to `/shristi/index.html`.
