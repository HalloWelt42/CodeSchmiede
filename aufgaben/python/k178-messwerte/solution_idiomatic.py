def messwert(text):
    try:
        wert = float(text)
    except ValueError:
        raise ValueError(text)
    if wert < -90:
        raise ValueError("unmöglich kalt")
    return wert


werte = []
while True:
    text = input()
    if text == "ende":
        break
    try:
        werte.append(messwert(text))
    except ValueError as fehler:
        print("Übersprungen:", fehler)
try:
    print("Durchschnitt:", round(sum(werte) / len(werte), 1))
except ZeroDivisionError:
    print("Keine Messwerte")
