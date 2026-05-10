def transformiere(alt: dict) -> dict:
    return {
        b.lower(): int(p) if isinstance(p, str) else p
        for p, lst in alt.items()
        for b in lst
    }
