def bmi_klasse(gewicht_kg: float, groesse_m: float) -> str:
    if gewicht_kg <= 0 or groesse_m <= 0:
        return "ungueltig"
    bmi = gewicht_kg / (groesse_m ** 2)
    if bmi < 18.5:
        return "untergewicht"
    if bmi < 25:
        return "normal"
    if bmi < 30:
        return "uebergewicht"
    return "adipositas"
