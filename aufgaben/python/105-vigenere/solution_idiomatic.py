def vigenere(text: str, schluessel: str) -> str:
    if not schluessel:
        return text
    schluessel = schluessel.lower()
    out: list[str] = []
    j = 0
    for c in text:
        if c.isupper():
            shift = ord(schluessel[j % len(schluessel)]) - ord("a")
            out.append(chr((ord(c) - ord("A") + shift) % 26 + ord("A")))
            j += 1
        elif c.islower():
            shift = ord(schluessel[j % len(schluessel)]) - ord("a")
            out.append(chr((ord(c) - ord("a") + shift) % 26 + ord("a")))
            j += 1
        else:
            out.append(c)
    return "".join(out)
