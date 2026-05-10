def behalte(liste, funktion_text):
    funktion = eval(funktion_text)
    return [x for x in liste if funktion(x)]
