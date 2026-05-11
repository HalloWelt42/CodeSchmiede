def bon_summe(posten: list[list]) -> float:
    return round(sum(z[1] * z[2] for z in posten), 2)
