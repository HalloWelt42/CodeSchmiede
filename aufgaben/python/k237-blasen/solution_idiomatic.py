zahlen = []
while True:
    text = input()
    if text == "ende":
        break
    zahlen.append(int(text))
tausche = 0
getauscht = True
while getauscht:
    getauscht = False
    for i in range(len(zahlen) - 1):
        if zahlen[i] > zahlen[i + 1]:
            zahlen[i], zahlen[i + 1] = zahlen[i + 1], zahlen[i]
            tausche += 1
            getauscht = True
print(zahlen)
print("Tauschvorgänge:", tausche)
