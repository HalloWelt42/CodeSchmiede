def groesstes_produkt(text: str, n: int) -> int:
    if n < 0:
        return -1
    if n == 0:
        return 1
    if not text or n > len(text) or not text.isdigit():
        return -1
    bestes = 0
    for i in range(len(text) - n + 1):
        produkt = 1
        for c in text[i:i + n]:
            produkt *= int(c)
        if produkt > bestes:
            bestes = produkt
    return bestes
