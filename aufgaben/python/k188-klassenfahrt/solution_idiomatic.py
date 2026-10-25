import math
from statistics import mean, median

plaetze = int(input())
alter = []
while True:
    text = input()
    if text == "ende":
        break
    alter.append(int(text))
print("Busse:", math.ceil(len(alter) / plaetze))
print("Mittleres Alter:", round(mean(alter), 1))
print("Median:", median(alter))
