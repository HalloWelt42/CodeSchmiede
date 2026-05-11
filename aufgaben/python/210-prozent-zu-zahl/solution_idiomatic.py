def aus_prozent(s: str) -> float:
    s = s.strip().rstrip("%").replace(",", ".")
    try:
        return float(s) / 100
    except ValueError:
        return 0.0
