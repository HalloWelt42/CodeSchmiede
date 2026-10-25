while True:
    try:
        anzahl = int(input())
        break
    except ValueError:
        print("Bitte eine ganze Zahl")
print("Danke:", anzahl, "Fische")
