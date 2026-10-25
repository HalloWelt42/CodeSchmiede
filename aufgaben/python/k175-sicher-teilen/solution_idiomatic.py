try:
    a = int(input())
    b = int(input())
    print("Ergebnis:", a / b)
except ZeroDivisionError:
    print("Durch null geht nicht")
except ValueError:
    print("Bitte nur Zahlen")
