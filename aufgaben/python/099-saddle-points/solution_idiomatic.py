def sattel_punkte(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix or not matrix[0]:
        return []
    zeilen_max = [max(zeile) for zeile in matrix]
    spalten_min = [min(spalte) for spalte in zip(*matrix)]
    ergebnisse: list[list[int]] = []
    for i, zeile in enumerate(matrix):
        for j, wert in enumerate(zeile):
            if wert == zeilen_max[i] and wert == spalten_min[j]:
                ergebnisse.append([i, j])
    return ergebnisse
