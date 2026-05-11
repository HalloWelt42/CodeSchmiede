def wiederhole(muster: str, laenge: int) -> str:
    if not muster or laenge <= 0:
        return ""
    anzahl = laenge // len(muster) + 1
    return (muster * anzahl)[:laenge]
