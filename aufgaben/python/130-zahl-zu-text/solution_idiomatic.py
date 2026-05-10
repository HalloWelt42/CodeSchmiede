_EINER = [
    "null", "eins", "zwei", "drei", "vier", "fuenf", "sechs", "sieben",
    "acht", "neun", "zehn", "elf", "zwoelf", "dreizehn", "vierzehn",
    "fuenfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn",
]

_ZEHNER = {
    20: "zwanzig", 30: "dreissig", 40: "vierzig", 50: "fuenfzig",
    60: "sechzig", 70: "siebzig", 80: "achtzig", 90: "neunzig",
}


def zahl_zu_wort(n: int) -> str:
    if n < 0 or n > 99:
        return ""
    if n < 20:
        return _EINER[n]
    if n % 10 == 0:
        return _ZEHNER[n]
    einer = "ein" if n % 10 == 1 else _EINER[n % 10]
    zehner = _ZEHNER[(n // 10) * 10]
    return f"{einer}und{zehner}"
