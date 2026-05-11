def zeit_format(sekunden: int) -> str:
    if sekunden < 0:
        return "00:00:00"
    h = sekunden // 3600
    m = (sekunden // 60) % 60
    s = sekunden % 60
    return f"{h:02}:{m:02}:{s:02}"
