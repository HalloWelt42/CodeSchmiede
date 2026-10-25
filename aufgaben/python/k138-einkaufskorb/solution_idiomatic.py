preise = {"Hering": 3, "Lachs": 5, "Eis": 2}
korb = {}
while True:
    ware = input()
    if ware == "kasse":
        break
    if ware not in preise:
        print(f"{ware}: gibt es nicht")
        continue
    korb[ware] = korb.get(ware, 0) + 1
gesamt = 0
for ware, n in korb.items():
    print(ware, "x", n)
    gesamt += preise[ware] * n
print("Gesamt:", gesamt)
