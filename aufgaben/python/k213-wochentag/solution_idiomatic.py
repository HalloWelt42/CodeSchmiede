from datetime import date

WOCHENTAGE = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

tag = date.fromisoformat(input())
print(WOCHENTAGE[tag.weekday()])
