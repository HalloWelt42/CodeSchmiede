def ist_isogramm(text: str) -> bool:
    buchstaben = [c.lower() for c in text if c.isalpha()]
    return len(buchstaben) == len(set(buchstaben))
