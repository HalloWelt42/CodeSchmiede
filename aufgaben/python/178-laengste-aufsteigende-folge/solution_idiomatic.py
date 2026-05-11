from bisect import bisect_left


def lis_laenge(zahlen: list[int]) -> int:
    tails: list[int] = []
    for x in zahlen:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
