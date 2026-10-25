wort = input()
anzahl = 0
for b in wort.lower():
    if b in "aeiou":
        anzahl += 1
print(anzahl)
