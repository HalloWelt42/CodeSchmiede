satz = input()
anzahl = {}
for w in satz.split():
    anzahl[w] = anzahl.get(w, 0) + 1
print(anzahl)
