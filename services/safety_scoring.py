WEIGHTS = {"lighting":0.25,"incidents":0.25,"road_condition":0.15,
           "ped_infra":0.15,"community":0.10,"crossing":0.10}

def score_route(indicators: dict):
    """
    indicators: {key: (value 0-1 or None, confidence 0-1, source, timestamp)}
    Returns dict with score, confidence, reasons, missing.
    None = missing, never treated as safe.
    """
    total_w, weighted, reasons, missing = 0, 0, [], []
    for k, w in WEIGHTS.items():
        entry = indicators.get(k)
        if not entry or entry[0] is None:
            missing.append(k); reasons.append(f"{k}: insufficient data")
            continue
        val, conf = entry[0], entry[1] if len(entry)>1 else 0.5
        weighted += val * w; total_w += w
        reasons.append(f"{k}: {val:.2f} (conf {conf:.2f})")
    if total_w < 0.4:
        return {"score": None, "label": "Insufficient data",
                "confidence": round(total_w,2), "reasons": reasons, "missing": missing}
    score = round(weighted/total_w*100, 1)
    return {"score": score, "label": "Assessment score (not safety probability)",
            "confidence": round(total_w,2), "reasons": reasons, "missing": missing,
            "weights": WEIGHTS}
