"""
Naive Loesung mit Schleife und String-Konkatenation.
"""


def caesar(text: str, k: int) -> str:
    ergebnis = ""
    for c in text:
        if "A" <= c <= "Z":
            basis = ord("A")
            ergebnis += chr((ord(c) - basis + k) % 26 + basis)
        elif "a" <= c <= "z":
            basis = ord("a")
            ergebnis += chr((ord(c) - basis + k) % 26 + basis)
        else:
            ergebnis += c
    return ergebnis
