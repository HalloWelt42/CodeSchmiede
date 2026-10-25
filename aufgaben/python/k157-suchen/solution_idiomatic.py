schlange = ["Pia", "Pit", "Paul", "Polly"]


def platz(namen, gesucht):
    for nr, name in enumerate(namen, 1):
        if name == gesucht:
            return nr
    return None


name = input()
ergebnis = platz(schlange, name)
if ergebnis is None:
    print(name, "ist nicht dabei")
else:
    print(name, "steht auf Platz", ergebnis)
