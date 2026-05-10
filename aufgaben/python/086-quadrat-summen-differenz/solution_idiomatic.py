def differenz(n: int) -> int:
    summe = n * (n + 1) // 2
    summe_quadrate = n * (n + 1) * (2 * n + 1) // 6
    return summe * summe - summe_quadrate
