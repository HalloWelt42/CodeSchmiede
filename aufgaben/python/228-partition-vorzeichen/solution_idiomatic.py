def partition_vorzeichen(zahlen: list[int]) -> list[list[int]]:
    neg: list[int] = []
    null: list[int] = []
    pos: list[int] = []
    for x in zahlen:
        if x < 0:
            neg.append(x)
        elif x == 0:
            null.append(x)
        else:
            pos.append(x)
    return [neg, null, pos]
