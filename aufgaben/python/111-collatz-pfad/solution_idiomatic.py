def collatz_pfad(n: int) -> list[int]:
    pfad = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        pfad.append(n)
    return pfad
