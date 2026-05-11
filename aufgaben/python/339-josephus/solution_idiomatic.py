def josephus(n: int, k: int) -> int:
    if n <= 0 or k <= 0:
        return -1
    j = 0
    for i in range(2, n + 1):
        j = (j + k) % i
    return j
