def sm2_update(ease: float, intervall_tage: int, wiederholungen: int, bewertung: int) -> dict:
    if bewertung < 3:
        return {"ease": ease, "intervall_tage": 1, "wiederholungen": 0}
    diff = 5 - bewertung
    neuer_ease = max(1.3, ease + 0.1 - diff * (0.08 + diff * 0.02))
    if wiederholungen == 0:
        neues_intervall = 1
    elif wiederholungen == 1:
        neues_intervall = 6
    else:
        neues_intervall = round(intervall_tage * neuer_ease)
    return {
        "ease": round(neuer_ease, 2),
        "intervall_tage": neues_intervall,
        "wiederholungen": wiederholungen + 1,
    }
