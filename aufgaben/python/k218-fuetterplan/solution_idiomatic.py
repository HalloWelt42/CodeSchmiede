from datetime import datetime, timedelta

KURZ = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

tag = datetime.strptime(input(), "%d.%m.%Y").date()
abstand = int(input())
anzahl = int(input())
for i in range(anzahl):
    print(KURZ[tag.weekday()], tag.strftime("%d.%m.%Y"))
    tag += timedelta(days=abstand)
