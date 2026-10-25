liste = []
while True:
    name = input()
    if name == "ende":
        break
    liste.append((name, int(input())))
for i in range(len(liste)):
    beste = i
    for j in range(i + 1, len(liste)):
        if liste[j][1] > liste[beste][1]:
            beste = j
    liste[i], liste[beste] = liste[beste], liste[i]
for platz, (name, punkte) in enumerate(liste, 1):
    print(f"{platz}. {name} {punkte}")
gesucht = input()
platz = -1
for i in range(len(liste)):
    if liste[i][0] == gesucht:
        platz = i + 1
        break
if platz == -1:
    print(gesucht, "ist nicht dabei")
else:
    print(gesucht, "ist auf Platz", platz)
