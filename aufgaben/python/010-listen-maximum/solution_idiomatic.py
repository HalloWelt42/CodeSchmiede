"""
Idiomatische Lösung: Built-In `max()` mit Default-Wert. `default=None`
verhindert die ValueError-Exception bei leerer Liste.
"""


def maximum(zahlen: list[int]) -> int | None:
    return max(zahlen, default=None)
