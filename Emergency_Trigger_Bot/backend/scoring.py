def calculate_triage_score(data):
    score = 0

    severity_map = {"mild": 1, "medium": 3, "severe": 5}
    duration_map = {"<1 day": 1, "1–3 days": 2, ">3 days": 3}

    score += severity_map.get(data.severity.lower(), 0)
    score += duration_map.get(data.duration.lower(), 0)

    if data.age < 5 or data.age > 65:
        score += 2

    if data.risk_factors:
        score += 2  # Fixed boost if any risk factor present

    return score
