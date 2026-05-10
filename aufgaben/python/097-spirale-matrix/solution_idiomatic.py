def spirale(n: int) -> list[list[int]]:
    if n == 0:
        return []
    grid = [[0] * n for _ in range(n)]
    richtungen = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    r = c = ri = 0
    for i in range(1, n * n + 1):
        grid[r][c] = i
        dr, dc = richtungen[ri]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < n and 0 <= nc < n) or grid[nr][nc] != 0:
            ri = (ri + 1) % 4
            dr, dc = richtungen[ri]
            nr, nc = r + dr, c + dc
        r, c = nr, nc
    return grid
