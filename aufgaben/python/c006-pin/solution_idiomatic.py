import hashlib


def pruefwert(pin):
    return hashlib.sha256(pin.encode()).hexdigest()


def knacke(geheim):
    return next(pin for pin in (f"{z:04d}" for z in range(10_000)) if pruefwert(pin) == geheim)
