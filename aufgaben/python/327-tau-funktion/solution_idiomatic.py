def tau(n: int) -> int:
    if n < 1:
        return 0
    z = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            z += 2 if i * i != n else 1
        i += 1
    return z
