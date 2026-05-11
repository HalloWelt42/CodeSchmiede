def xor_tausch(a: int, b: int) -> list[int]:
    a ^= b
    b ^= a
    a ^= b
    return [a, b]
