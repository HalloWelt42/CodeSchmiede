def dauer_text(sekunden: int) -> str:
    if sekunden <= 0:
        return "0s"
    h = sekunden // 3600
    m = (sekunden // 60) % 60
    s = sekunden % 60
    teile: list[str] = []
    if h:
        teile.append(f"{h}h")
    if m:
        teile.append(f"{m}m")
    if s:
        teile.append(f"{s}s")
    return " ".join(teile)
