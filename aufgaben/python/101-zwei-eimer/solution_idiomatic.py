from collections import deque


def zwei_eimer(a: int, b: int, ziel: int, start: str) -> list:
    if start == "a":
        startzustand = (a, 0)
        verbot = (0, b)
    else:
        startzustand = (0, b)
        verbot = (a, 0)

    besucht = {startzustand}
    queue: deque[tuple[tuple[int, int], int]] = deque([(startzustand, 1)])

    while queue:
        (ai, bi), zuege = queue.popleft()
        if ai == ziel:
            return [zuege, "a", bi]
        if bi == ziel:
            return [zuege, "b", ai]

        kandidaten = [
            (a, bi),  # fuelle a
            (ai, b),  # fuelle b
            (0, bi),  # leere a
            (ai, 0),  # leere b
        ]
        # kippe a -> b
        umfuell = min(ai, b - bi)
        kandidaten.append((ai - umfuell, bi + umfuell))
        # kippe b -> a
        umfuell = min(bi, a - ai)
        kandidaten.append((ai + umfuell, bi - umfuell))

        for k in kandidaten:
            if k in besucht or k == verbot:
                continue
            besucht.add(k)
            queue.append((k, zuege + 1))
    return []
