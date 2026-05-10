def finde_anagramme(wort: str, kandidaten: list[str]) -> list[str]:
    schluessel = sorted(wort.lower())
    return [
        k for k in kandidaten
        if k.lower() != wort.lower() and sorted(k.lower()) == schluessel
    ]
