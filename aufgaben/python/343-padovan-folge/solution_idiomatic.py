def padovan(n: int) -> list[int]:
    if n <= 0:
        return []
    folge = [1, 1, 1]
    while len(folge) < n:
        folge.append(folge[-2] + folge[-3])
    return folge[:n]
