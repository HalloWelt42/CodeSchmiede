zahlen = []
while True:
    text = input()
    if text == "ende":
        break
    zahlen.append(int(text))
for i in range(len(zahlen)):
    kleinste = i
    for j in range(i + 1, len(zahlen)):
        if zahlen[j] < zahlen[kleinste]:
            kleinste = j
    zahlen[i], zahlen[kleinste] = zahlen[kleinste], zahlen[i]
print(zahlen)
