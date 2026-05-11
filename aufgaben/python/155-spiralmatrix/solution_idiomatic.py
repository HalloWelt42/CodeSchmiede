def spirale_lesen(matrix: list[list[int]]) -> list[int]:
    if not matrix or not matrix[0]:
        return []
    out: list[int] = []
    oben, unten = 0, len(matrix) - 1
    links, rechts = 0, len(matrix[0]) - 1
    while oben <= unten and links <= rechts:
        for j in range(links, rechts + 1):
            out.append(matrix[oben][j])
        oben += 1
        for i in range(oben, unten + 1):
            out.append(matrix[i][rechts])
        rechts -= 1
        if oben <= unten:
            for j in range(rechts, links - 1, -1):
                out.append(matrix[unten][j])
            unten -= 1
        if links <= rechts:
            for i in range(unten, oben - 1, -1):
                out.append(matrix[i][links])
            links += 1
    return out
