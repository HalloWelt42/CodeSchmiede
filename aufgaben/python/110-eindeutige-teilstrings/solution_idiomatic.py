def anzahl_teilstrings(text: str) -> int:
    return len({text[i:j] for i in range(len(text)) for j in range(i + 1, len(text) + 1)})
