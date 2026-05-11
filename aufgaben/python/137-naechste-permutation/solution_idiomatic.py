def naechste_permutation(a: list[int]) -> list[int]:
    a = list(a)
    n = len(a)
    if n < 2:
        return a
    # 1. Pivot von rechts
    i = n - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i < 0:
        # War letzte: aufsteigend sortiert
        return sorted(a)
    # 2. Tauschpartner von rechts
    j = n - 1
    while a[j] <= a[i]:
        j -= 1
    a[i], a[j] = a[j], a[i]
    # 3. Rest umdrehen
    a[i + 1 :] = a[i + 1 :][::-1]
    return a
