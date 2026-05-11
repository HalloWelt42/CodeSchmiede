def zahl_umdrehen(n: int) -> int:
    vorzeichen = -1 if n < 0 else 1
    return vorzeichen * int(str(abs(n))[::-1])
