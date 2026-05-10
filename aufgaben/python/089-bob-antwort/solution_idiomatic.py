def bob_antwort(text: str) -> str:
    bereinigt = text.strip()
    if not bereinigt:
        return "Manno, sag was."
    schreit = bereinigt.upper() == bereinigt and any(c.isalpha() for c in bereinigt)
    frage = bereinigt.endswith("?")
    if schreit and frage:
        return "Schrei mich nicht an, was willst du?!"
    if schreit:
        return "Schrei mich nicht an!"
    if frage:
        return "Klar."
    return "Naja."
