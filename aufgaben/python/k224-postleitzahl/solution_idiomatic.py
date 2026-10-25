import re

plz = input()
if re.fullmatch(r"\d{5}", plz):
    print(plz, "ist gültig")
else:
    print(plz, "ist ungültig")
