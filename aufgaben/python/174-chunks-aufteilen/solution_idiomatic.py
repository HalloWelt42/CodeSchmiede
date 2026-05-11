def chunks(a: list, k: int) -> list[list]:
    if k <= 0:
        return []
    return [a[i:i + k] for i in range(0, len(a), k)]
