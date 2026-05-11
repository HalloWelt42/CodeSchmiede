def erstes_positiv(zahlen: list):
    return next((x for x in zahlen if x > 0), None)
