import requests
from functools import lru_cache

_NOMINATIM = "https://nominatim.openstreetmap.org/search"

@lru_cache(maxsize=256)
def geocode(query: str):
    """Geocode via Nominatim. Returns (lat, lon, display_name) or None."""
    if not query or len(query.strip()) < 3:
        return None
    try:
        r = requests.get(_NOMINATIM, params={"q": query, "format": "json", "limit": 1},
                         headers={"User-Agent": "SafeRouteAI/1.0 (edu)"}, timeout=10)
        r.raise_for_status()
        data = r.json()
        if not data: return None
        return float(data[0]["lat"]), float(data[0]["lon"]), data[0]["display_name"]
    except Exception:
        return None
