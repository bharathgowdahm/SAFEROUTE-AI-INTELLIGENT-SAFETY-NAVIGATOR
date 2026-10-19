import requests, json
from pathlib import Path

OSRM = "https://router.project-osrm.org/route/v1/driving"

def get_routes(start, end, alternatives=2):
    """start/end = (lat, lon). Returns list of route dicts or demo fallback."""
    try:
        lon1, lat1 = start[1], start[0]; lon2, lat2 = end[1], end[0]
        r = requests.get(f"{OSRM}/{lon1},{lat1};{lon2},{lat2}",
            params={"overview":"full","geometries":"geojson","alternatives":str(alternatives)},
            timeout=15)
        r.raise_for_status()
        j = r.json()
        routes = []
        for rt in j.get("routes", []):
            routes.append({"distance_m": rt["distance"], "duration_s": rt["duration"],
                "geometry": rt["geometry"]["coordinates"], "source": "OSRM"})
        if routes: return routes
    except Exception:
        pass
    # Demo fallback — Bengaluru sample
    p = Path("sample_data/demo_routes.json")
    if p.exists():
        demo = json.loads(p.read_text())
        for d in demo: d["source"] = "DEMO DATA"
        return demo
    return []
