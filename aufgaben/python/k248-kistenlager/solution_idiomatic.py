lager_a = [3, [2, [1, 4]], 5, [[6]]]
lager_b = [[[[7]]], 1]


def fische(kiste):
    anzahl = 0
    for ding in kiste:
        if isinstance(ding, list):
            anzahl += fische(ding)
        else:
            anzahl += ding
    return anzahl


def tiefe(kiste):
    innen = 0
    for ding in kiste:
        if isinstance(ding, list):
            innen = max(innen, tiefe(ding))
    return 1 + innen


print(f"lager_a: {fische(lager_a)} Fische, Tiefe {tiefe(lager_a)}")
print(f"lager_b: {fische(lager_b)} Fische, Tiefe {tiefe(lager_b)}")
