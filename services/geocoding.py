import requests
from functools import lru_cache

# Fallback for demo cities - works even if Nominatim is down
FALLBACK = {
    "hassan": (13.0035, 76.1004, "Hassan, Karnataka, India"),
    "electronic city": (12.8452, 77.6602, "Electronic City, Bengaluru, India"),
    "mg road": (12.9757, 77.6013, "MG Road, Bengaluru, India"),
    "bengaluru": (12.9716, 77.5946, "Bengaluru, Karnataka, India"),
}

@lru_cache(maxsize=256)
def geocode(query: str):
    if not query or len(query.strip()) < 3:
        return None
    
    q_lower = query.strip().lower()
    # 1. Check fallback first
    for key, val in FALLBACK.items():
        if key in q_lower:
            return val
    
    # 2. Try Nominatim
    try:
        r = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": query + ", Karnataka, India", "format": "json", "limit": 1},
            headers={"User-Agent": "SafeRouteAI/1.0 (student project; contact: admin@example.com)"},
            timeout=15
        )
        r.raise_for_status()
        data = r.json()
        if not data: 
            return None
        return float(data[0]["lat"]), float(data[0]["lon"]), data[0]["display_name"]
    except Exception:
        return None
