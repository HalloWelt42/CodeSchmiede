def alter_pruefen(alter):
    if alter < 0 or alter > 120:
        raise ValueError("Alter muss zwischen 0 und 120 liegen")
    return alter


try:
    print("Alter:", alter_pruefen(int(input())))
except ValueError as fehler:
    print("Fehler:", fehler)
