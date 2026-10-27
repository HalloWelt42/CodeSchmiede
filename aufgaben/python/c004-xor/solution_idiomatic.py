from collections import Counter


def zurueck(geheim, wort):
    schluessel = wort.encode() if isinstance(wort, str) else bytes(wort)
    daten = bytes.fromhex(geheim)
    return bytes(b ^ schluessel[i % len(schluessel)] for i, b in enumerate(daten)).decode(errors="replace")


def punkte(b):
    # wie sehr sieht ein Byte nach Text aus?
    if b == 32 or 97 <= b <= 122:
        return 2
    if 65 <= b <= 90 or b in b".,!?:-'0123456789\n" or b >= 0xC3:
        return 1
    return -4


PUNKTE = [punkte(b) for b in range(256)]


def spalte_knacken(spalte):
    # jedes Byte nur einmal bewerten, mal wie oft es vorkommt
    zahl = Counter(spalte)
    return max((sum(n * PUNKTE[b ^ k] for b, n in zahl.items()), k) for k in range(256))


def knacke(geheim):
    daten = bytes.fromhex(geheim)
    versuche = []
    for laenge in range(1, 9):
        ergebnisse = [spalte_knacken(daten[i::laenge]) for i in range(laenge)]
        schluessel = bytes(k for _, k in ergebnisse)
        versuche.append((sum(p for p, _ in ergebnisse) / len(daten), schluessel))
    bester = max(p for p, _ in versuche)
    # ein Vielfaches der richtigen Länge passt genauso gut: die kürzeste, die fast mithält
    _, schluessel = next(v for v in versuche if v[0] >= bester - 0.02)
    return zurueck(geheim, schluessel)
