def schnitt(a: list, b: list) -> list:
    return sorted(set(a) & set(b))
