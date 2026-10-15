# India Signal Network — handoff for Claude Code

Static single-page site. No build step. Everything is in `index.html` (~1.2 MB; most of it is embedded district/state geometry JSON).

## Files
- `index.html` — the whole site. Loads three.js r128 (cdnjs) and OrbitControls (jsdelivr). Data is embedded in `<script type="application/json">` blocks: `geo` (state boundaries), `live0` (IODA outage snapshot), plus district data.
- `ioda.json` — the same IODA snapshot as `live0` (15 Oct 2026, 19:46 IST; Madhya Pradesh and Chhattisgarh in outage).
- `README.md` — short public description.

## Live layer
On claude.ai the page subscribes to `window.claude.use("db")` → doc `live/ioda` for hourly updates. That API doesn't exist off claude.ai, so on any other host the page falls back to the embedded `live0` snapshot (the code returns early when `window.claude` is missing). To keep it fresh elsewhere, regenerate `live0`/`ioda.json` from
`https://api.ioda.inetintel.cc.gatech.edu/v2/outages/events?entityType=region&relatedTo=country/IN&from=<T-86400>&until=<T>&format=ioda`
(name mapping: Orissa→Odisha, Uttaranchal→Uttarakhand, "Jammu and Kashmir"→"Jammu & Kashmir", "Andaman and Nicobar"→"Andaman & Nicobar", Dadra/Daman→"Dadra & Nagar Haveli and Daman & Diu"; an event is ongoing if until is within 1200 s of T).

## To-do (requested by the owner)
1. `gh auth login` if needed, then `gh repo create india-signal-network --public --source=. --push`.
2. Deploy to Vercel as a static site (framework: none, no build command, output dir: root). Prefer linking the GitHub repo so pushes redeploy.
3. Open the production URL and confirm the 3D map renders with no console errors.
4. Report the GitHub and Vercel URLs.

Don't hand-edit the large JSON lines; edit them with a script.
