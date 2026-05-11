def ini_parse(s: str) -> dict:
    out: dict = {}
    aktuelle_sektion: str | None = None
    for zeile in s.splitlines():
        z = zeile.strip()
        if not z or z.startswith(";") or z.startswith("#"):
            continue
        if z.startswith("[") and z.endswith("]"):
            aktuelle_sektion = z[1:-1].strip()
            out.setdefault(aktuelle_sektion, {})
        elif "=" in z and aktuelle_sektion is not None:
            k, v = z.split("=", 1)
            out[aktuelle_sektion][k.strip()] = v.strip()
    return out
