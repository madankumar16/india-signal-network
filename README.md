<h1 align="center">📡 India Signal Network</h1>

<p align="center">
  An interactive 3D map of how India gets online — mobile, landline and satellite —<br>
  with outage alerts for each state that refresh every hour.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/HTML-single%20page-E34F26?style=flat-square&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/three.js-3D-000000?style=flat-square&logo=threedotjs&logoColor=white">
  <img src="https://img.shields.io/badge/Deployed-Vercel-000000?style=flat-square&logo=vercel&logoColor=white">
  <img src="https://github.com/madankumar16/india-signal-network/actions/workflows/refresh-ioda.yml/badge.svg">
</p>

<!-- 📸 Add a screenshot of the map here, plus the live link:  **[▶ Open the live site](https://YOUR-LINK.vercel.app)** -->

---

## ✨ What you can see

- 🗺️ **A 3D map of India** built with three.js
- 📶 **Connectivity data** from official public sources — TRAI, DoT and ISRO
- 🚨 **State-level outage alerts** from IODA (Georgia Tech), covering the last 24 hours
- ⚡ **Fast and simple** — one HTML file, no build step, no server

---

## 🔄 How the outage data stays fresh

```text
 GitHub Actions (every hour)
        │
        ▼
 scripts/refresh_ioda.py ──► asks IODA for India's state outages (last 24 h)
        │
        ▼
 updates ioda.json + the data inside index.html
        │
        ▼
 commits only if something changed ──► the new commit goes live on Vercel
```

- An outage counts as **ongoing** if it ended within the last 20 minutes.
- Old state names are fixed to current ones (for example, Orissa → Odisha).
- GitHub can delay scheduled runs, so "hourly" is approximate.

---

## 🚀 Run it yourself

```bash
git clone https://github.com/madankumar16/india-signal-network.git
cd india-signal-network
python -m http.server 8000     # then open http://localhost:8000
```

Refresh the outage data by hand:

```bash
python scripts/refresh_ioda.py
```

---

## 📁 Files

| File | What it does |
|---|---|
| `index.html` | The whole site — map, data and styling |
| `ioda.json` | Latest saved outage snapshot |
| `scripts/refresh_ioda.py` | Downloads fresh outage data |
| `.github/workflows/refresh-ioda.yml` | Runs the refresh every hour |
| `vercel.json` | Hosting settings |

---

## 🙏 Data sources

- **TRAI**, **DoT**, **ISRO** — published connectivity figures
- **[IODA](https://ioda.inetintel.cc.gatech.edu/)** (Georgia Tech) — internet outage detection

The data belongs to these sources. This project only displays it.

---

<p align="center">Made by <a href="https://github.com/madankumar16">Madan Kumar S</a> · ECE, VTU '28</p>
