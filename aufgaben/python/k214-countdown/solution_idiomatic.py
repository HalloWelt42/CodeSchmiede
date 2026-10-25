from datetime import date

heute = date.fromisoformat(input())
ziel = date.fromisoformat(input())
print("Noch", (ziel - heute).days, "Tage")
