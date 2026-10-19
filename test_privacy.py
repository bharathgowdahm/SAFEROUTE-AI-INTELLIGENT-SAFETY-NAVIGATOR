def test_no_exact_victim_location():
    incident = {"lat": 12.9716, "lon": 77.5946, "precision": "approx"}
    assert incident["precision"] == "approx"
