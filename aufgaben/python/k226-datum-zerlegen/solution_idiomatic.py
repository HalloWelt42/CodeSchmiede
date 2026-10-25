import re

treffer = re.fullmatch(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", input())
if treffer:
    print(f"Tag {treffer.group(1)}, Monat {treffer.group(2)}, Jahr {treffer.group(3)}")
else:
    print("Kein Datum")
