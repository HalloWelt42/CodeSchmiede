from datetime import date

geboren = date.fromisoformat(input())
stichtag = date.fromisoformat(input())
alter = stichtag.year - geboren.year
if (stichtag.month, stichtag.day) < (geboren.month, geboren.day):
    alter -= 1
print("Alter:", alter)
