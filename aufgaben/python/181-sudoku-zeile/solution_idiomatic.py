_ZIFFERN = set(range(1, 10))


def sudoku_zeile(zeile: list[int]) -> bool:
    return len(zeile) == 9 and set(zeile) == _ZIFFERN
