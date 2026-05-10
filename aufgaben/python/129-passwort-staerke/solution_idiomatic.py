def passwort_staerke(passwort: str) -> int:
    punkte = 0
    if len(passwort) >= 8:
        punkte += 1
    if any(c.islower() for c in passwort):
        punkte += 1
    if any(c.isupper() for c in passwort):
        punkte += 1
    if any(c.isdigit() for c in passwort):
        punkte += 1
    if any(not c.isalnum() for c in passwort):
        punkte += 1
    return punkte
