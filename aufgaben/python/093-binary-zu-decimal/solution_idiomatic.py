def binaer_zu_dezimal(text: str) -> int:
    if not text or any(c not in "01" for c in text):
        return -1
    summe = 0
    for i, c in enumerate(reversed(text)):
        if c == "1":
            summe += 1 << i
    return summe
