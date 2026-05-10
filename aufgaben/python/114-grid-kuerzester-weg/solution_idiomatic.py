from collections import deque


def kuerzester_weg(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return -1
    n = len(grid)
    m = len(grid[0])
    if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
        return -1
    if n == 1 and m == 1:
        return 0
    besucht = {(0, 0)}
    queue: deque[tuple[int, int, int]] = deque([(0, 0, 0)])
    richtungen = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        r, c, schritte = queue.popleft()
        for dr, dc in richtungen:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0 and (nr, nc) not in besucht:
                if nr == n - 1 and nc == m - 1:
                    return schritte + 1
                besucht.add((nr, nc))
                queue.append((nr, nc, schritte + 1))
    return -1
