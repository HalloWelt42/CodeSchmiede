def fibonacci_folge(n: int) -> list[int]:
    folge: list[int] = []
    a, b = 0, 1
    for _ in range(n):
        folge.append(a)
        a, b = b, a + b
    return folge
