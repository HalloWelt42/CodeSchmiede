def vier_gewinnt(brett: list[list[str]]):
    if not brett or not brett[0]:
        return None
    rows, cols = len(brett), len(brett[0])
    DIR = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for i in range(rows):
        for j in range(cols):
            c = brett[i][j]
            if c == " ":
                continue
            for di, dj in DIR:
                if all(
                    0 <= i + k * di < rows
                    and 0 <= j + k * dj < cols
                    and brett[i + k * di][j + k * dj] == c
                    for k in range(4)
                ):
                    return c
    return None
