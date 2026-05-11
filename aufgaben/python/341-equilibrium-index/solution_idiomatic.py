def gleichgewicht(liste: list[int]) -> list[int]:
    gesamt = sum(liste)
    links = 0
    out: list[int] = []
    for i, x in enumerate(liste):
        rechts = gesamt - links - x
        if links == rechts:
            out.append(i)
        links += x
    return out
