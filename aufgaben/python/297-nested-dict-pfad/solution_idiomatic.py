def dict_pfad(d: dict, pfad: str, default):
    for teil in pfad.split("."):
        if not isinstance(d, dict) or teil not in d:
            return default
        d = d[teil]
    return d
