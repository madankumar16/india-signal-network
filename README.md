# India Signal Network

3D map of mobile, land-line and satellite internet in India, built from TRAI, DoT and ISRO published data.

- `index.html` — the whole site (static, no build step).
- `ioda.json` — snapshot of IODA (Georgia Tech) state-level internet outage alerts, embedded into the page at deploy time. On claude.ai the page reads this live; on this static copy it is frozen at the last deploy.

Deployed on Vercel as a static site.
