zaehlung = {"Pinguine": 12, "Robben": 3, "Möwen": 7}
for tier, n in zaehlung.items():
    print(f"{tier}: {n}")
print("Zusammen:", sum(zaehlung.values()))
