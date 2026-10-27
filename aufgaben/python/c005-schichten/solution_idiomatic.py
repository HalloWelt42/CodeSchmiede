import base64
import re

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def schale(text):
    if re.fullmatch(r"([0-9a-f]{2})+", text):
        return bytes.fromhex(text).decode()
    if re.fullmatch(r"([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?", text) and text:
        return base64.b64decode(text).decode()
    return None


def schiebe(text, n):
    return "".join(ABC[(ABC.index(c) + n) % 26] if c in ABC else c for c in text)


def knacke(geheim):
    while (innen := schale(geheim)) is not None:
        geheim = innen
    return max((schiebe(geheim, -n) for n in range(26)), key=lambda t: sum(DEUTSCH.get(c, 0) for c in t))
