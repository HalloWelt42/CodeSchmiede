"""
Pythonic mit itertools.accumulate.
"""

from itertools import accumulate


def prefix_summe(zahlen: list[int]) -> list[int]:
    return list(accumulate(zahlen))
