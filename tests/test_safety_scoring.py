from services.safety_scoring import score_route

def test_insufficient_data():
    r = score_route({"lighting":(None,0)})
    assert r["score"] is None and r["label"]=="Insufficient data"

def test_weighted_score():
    ind = {k:(0.8,0.9) for k in ["lighting","incidents","road_condition","ped_infra","community","crossing"]}
    r = score_route(ind)
    assert r["score"] == 80.0

def test_missing_not_safe():
    r = score_route({"lighting":(0.9,0.9)})  # only one indicator
    assert r["score"] is None  # total weight < 0.4
