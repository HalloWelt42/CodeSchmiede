zahlen = []
while True:
    z = int(input())
    if z == 0:
        break
    zahlen = zahlen + [z]
summe = 0
for z in zahlen:
    summe += z
schnitt = summe / len(zahlen)
print("Durchschnitt:", schnitt)
for z in zahlen:
    if z > schnitt:
        print(z)
