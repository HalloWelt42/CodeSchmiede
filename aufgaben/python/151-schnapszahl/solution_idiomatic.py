def ist_schnapszahl(n: int) -> bool:
    s = str(abs(n))
    return len(s) >= 2 and len(set(s)) == 1
