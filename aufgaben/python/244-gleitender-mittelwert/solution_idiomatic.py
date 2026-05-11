def gleitend(zahlen: list[float], k: int) -> list[float]:
    n = len(zahlen)
    if k <= 0 or k > n:
        return []
    return [round(sum(zahlen[i:i + k]) / k, 4) for i in range(n - k + 1)]
