def aufzaehlung(woerter: list[str]) -> str:
    if not woerter:
        return ""
    if len(woerter) == 1:
        return woerter[0]
    if len(woerter) == 2:
        return f"{woerter[0]} und {woerter[1]}"
    return ", ".join(woerter[:-1]) + " und " + woerter[-1]
