einmal = []
while True:
    z = int(input())
    if z == 0:
        break
    if z not in einmal:
        einmal.append(z)
print(einmal)
print(sorted(einmal))
