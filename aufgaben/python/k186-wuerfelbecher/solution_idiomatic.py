import random

augen = set()
for i in range(600):
    augen.add(random.randint(1, 6))
print(sorted(augen))
