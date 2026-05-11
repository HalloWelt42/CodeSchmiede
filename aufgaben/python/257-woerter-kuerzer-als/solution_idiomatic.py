def kuerzer_als(text: str, n: int) -> list[str]:
    return [w for w in text.split() if len(w) < n]
