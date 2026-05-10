def uhrzeit_plus(stunde: int, minute: int, zusatz_minuten: int) -> str:
    gesamt = (stunde * 60 + minute + zusatz_minuten) % (24 * 60)
    h, m = divmod(gesamt, 60)
    return f"{h:02d}:{m:02d}"
