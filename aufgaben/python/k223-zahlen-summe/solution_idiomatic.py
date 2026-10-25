import re

summe = 0
for zahl in re.findall(r"\d+", input()):
    summe += int(zahl)
print("Summe:", summe)
