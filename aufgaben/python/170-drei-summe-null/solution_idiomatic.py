def drei_summe(zahlen: list[int]) -> list[list[int]]:
    z = sorted(zahlen)
    n = len(z)
    out: list[list[int]] = []
    for i in range(n - 2):
        if i > 0 and z[i] == z[i - 1]:
            continue
        j, k = i + 1, n - 1
        while j < k:
            s = z[i] + z[j] + z[k]
            if s == 0:
                out.append([z[i], z[j], z[k]])
                j += 1
                k -= 1
                while j < k and z[j] == z[j - 1]:
                    j += 1
                while j < k and z[k] == z[k + 1]:
                    k -= 1
            elif s < 0:
                j += 1
            else:
                k -= 1
    return out
