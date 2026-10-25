import re

namen = re.findall(r"[A-ZÄÖÜ]\w*", input())
for name in namen:
    print(name)
print(len(namen), "Namen")
