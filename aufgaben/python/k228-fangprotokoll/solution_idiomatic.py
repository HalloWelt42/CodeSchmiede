import re

faenge = {}
while True:
    zeile = input()
    if zeile == "ende":
        break
    treffer = re.fullmatch(r"([A-ZÄÖÜ]\w*) fing (\d+) \w+", zeile)
    if treffer is None:
        print("Unlesbar:", zeile)
        continue
    name = treffer.group(1)
    faenge[name] = faenge.get(name, 0) + int(treffer.group(2))
for name, summe in faenge.items():
    print(f"{name}: {summe}")
