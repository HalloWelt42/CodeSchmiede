"""
Naive Lösung: Zeichen für Zeichen durchgehen, führende Leerzeichen
überspringen, dann bis zum nächsten Leerzeichen sammeln.
"""


def erstes_wort(text: str) -> str:
    ergebnis = ""
    sammeln = False
    for c in text:
        if c == " ":
            if sammeln:
                break
        else:
            ergebnis += c
            sammeln = True
    return ergebnis
