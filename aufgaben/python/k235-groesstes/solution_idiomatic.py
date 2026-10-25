zahlen = []
while True:
    text = input()
    if text == "ende":
        break
    zahlen.append(int(text))
beste = 0
for i in range(1, len(zahlen)):
    if zahlen[i] > zahlen[beste]:
        beste = i
print("Größte:", zahlen[beste], "an Stelle", beste)
