liste = [("Pit", 17), ("Pia", 42), ("Paul", 8)]
bester, beste_punkte = liste[0]
for name, punkte in liste:
    if punkte > beste_punkte:
        bester, beste_punkte = name, punkte
print(f"{bester} hat gewonnen mit {beste_punkte} Punkten")
