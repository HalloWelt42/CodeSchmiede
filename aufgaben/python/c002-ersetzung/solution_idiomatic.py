import math
import random
import re
from collections import Counter

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
# Punkte je Buchstabenpaar als Tabelle 27 x 27, Platz 26 ist _ (Wortanfang, Wortende)
LOG = [[math.log(PAARE.get(a + b, 0.0003)) for b in ABC] for a in ABC]


def ersetze(geheim, alphabet):
    return "".join(ABC[alphabet.index(c)] if c in alphabet else c for c in geheim)


def knacke(geheim):
    # die Paare des Geheimtexts einmal zählen, als Nummern 0 bis 26
    woerter = ["_" + w + "_" for w in re.findall("[A-Z]+", geheim)]
    zahl = Counter((ABC.index(w[i]), ABC.index(w[i + 1])) for w in woerter for i in range(len(w) - 1))
    paare = [(a, b, n) for (a, b), n in zahl.items()]

    def punkte(k):
        # k[g]: Nummer des Klarbuchstabens zum Geheimbuchstaben g
        return sum(n * LOG[k[a]][k[b]] for a, b, n in paare)

    def klettern(k):
        wert, besser = punkte(k), True
        while besser:
            besser = False
            for i in range(26):
                for j in range(i + 1, 26):
                    k[i], k[j] = k[j], k[i]
                    neu = punkte(k)
                    if neu > wert:
                        wert, besser = neu, True
                    else:
                        k[i], k[j] = k[j], k[i]
        return k, wert

    # erste Vermutung: der häufigste Geheimbuchstabe ist E, der zweithäufigste N usw.
    folge = sorted(range(26), key=lambda g: -geheim.count(ABC[g]))
    deutsch = sorted(range(26), key=lambda p: -DEUTSCH[ABC[p]])
    k = [0] * 26 + [26]
    for g, p in zip(folge, deutsch):
        k[g] = p
    beste, bester = klettern(k)

    # aus einer Sackgasse: ein paar Buchstaben durcheinanderwerfen und neu klettern
    zufall = random.Random(7)
    for _ in range(6):
        neu = list(beste)
        for _ in range(4):
            i, j = zufall.sample(range(26), 2)
            neu[i], neu[j] = neu[j], neu[i]
        neu, wert = klettern(neu)
        if wert > bester:
            beste, bester = neu, wert
    return "".join(ABC[beste[ABC.index(c)]] if c in ABC[:26] else c for c in geheim)
