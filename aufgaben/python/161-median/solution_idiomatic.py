def median(zahlen: list):
    if not zahlen:
        return None
    s = sorted(zahlen)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2
