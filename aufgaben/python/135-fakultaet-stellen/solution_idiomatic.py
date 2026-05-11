from math import factorial


def stellen_von_fakultaet(n: int) -> int:
    if n < 0:
        return 0
    return len(str(factorial(n)))
