from statistics import mean, median

zahlen = []
while True:
    text = input()
    if text == "ende":
        break
    zahlen.append(int(text))
print("Mittelwert:", mean(zahlen))
print("Median:", median(zahlen))
