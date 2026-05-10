"""
Rekursive Lösung -- direkte Umsetzung der mathematischen Definition.
"""


def fakultaet(n: int) -> int:
    if n <= 1:
        return 1
    return n * fakultaet(n - 1)
