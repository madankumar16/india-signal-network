"""Refresh the IODA outage snapshot: writes ioda.json and the live0 block in index.html.

Fetches the last 24 h of region-level outage events for India from IODA (Georgia Tech).
An event counts as ongoing if it ends within 1200 s of the request time.
"""
import json, re, time, urllib.request

T = int(time.time())
URL = ("https://api.ioda.inetintel.cc.gatech.edu/v2/outages/events?entityType=region"
       f"&relatedTo=country/IN&from={T - 86400}&until={T}&format=ioda")
MAP = {"Orissa": "Odisha", "Uttaranchal": "Uttarakhand", "Jammu and Kashmir": "Jammu & Kashmir",
       "Andaman and Nicobar": "Andaman & Nicobar"}


def name(n):
    if n in MAP:
        return MAP[n]
    if n.startswith("Dadra") or n.startswith("Daman"):
        return "Dadra & Nagar Haveli and Daman & Diu"
    return n


with urllib.request.urlopen(URL, timeout=60) as r:
    data = json.load(r)
if data.get("error"):
    raise SystemExit(f"IODA error: {data['error']}")

states = {}
for e in data["data"]:
    st = name(e["entity"]["name"])
    ongoing = T - e["until"] <= 1200
    states.setdefault(st, {"status": "recovered", "events": []})
    states[st]["events"].append({"src": e["datasource"], "from": e["from"],
                                 "until": None if ongoing else e["until"], "score": round(e["score"], 1)})
    if ongoing:
        states[st]["status"] = "outage"

snap = json.dumps({"source": "IODA (Georgia Tech Internet Outage Detection and Analysis)", "updatedAt": T,
                   "window": "last 24 hours", "states": states}, ensure_ascii=False)
with open("ioda.json", "w", encoding="utf-8", newline="") as f:
    f.write(snap)
with open("index.html", encoding="utf-8", newline="") as f:
    html = f.read()
html, n = re.subn(r'(<script id="live0" type="application/json">)[^<]*(</script>)',
                  lambda m: m.group(1) + snap + m.group(2), html)
if n != 1:
    raise SystemExit("live0 block not found in index.html")
with open("index.html", "w", encoding="utf-8", newline="") as f:
    f.write(html)
for k, v in states.items():
    print(k, v["status"], len(v["events"]))
