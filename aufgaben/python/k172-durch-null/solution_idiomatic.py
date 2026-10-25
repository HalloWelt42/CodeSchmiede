fische = 12
pinguine = 0
try:
    print(fische / pinguine)
except ZeroDivisionError:
    print("Teilen durch null geht nicht")
