def bier_strophe(n: int) -> str:
    if n == 0:
        return (
            "Keine Flaschen Bier auf der Wand, keine Flaschen Bier.\n"
            "Geh in den Laden, kauf neues, 99 Flaschen Bier auf der Wand."
        )
    if n == 1:
        return (
            "1 Flasche Bier auf der Wand, 1 Flasche Bier.\n"
            "Nimm sie runter, gib sie rum, keine Flaschen Bier auf der Wand."
        )
    naechste = "1 Flasche" if n - 1 == 1 else f"{n - 1} Flaschen"
    return (
        f"{n} Flaschen Bier auf der Wand, {n} Flaschen Bier.\n"
        f"Nimm eine runter, gib sie rum, {naechste} Bier auf der Wand."
    )
