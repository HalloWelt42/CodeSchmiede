"""Serie: Tage am Stück mit mindestens einer bestandenen Abgabe.

Je `schild_alle_tage` geübte Tage gibt es einen Schutzschild (höchstens
`schilde_max`); ein verpasster Tag verbraucht einen, ohne Schild reißt
die Serie. Ein aufgefangener Tag hält die Serie, zählt aber nicht mit.
Der heutige Tag kann noch kommen und reißt nichts.
"""

from collections.abc import Iterable
from datetime import date, timedelta

from ..models.konfig import SpielRegeln
from ..models.spiel import SerienStand


def serie_aus_tagen(tage: Iterable[date], heute: date, regeln: SpielRegeln) -> SerienStand:
    geuebt = {t for t in tage if t <= heute}
    lauf = laengste = schilde = seit_schild = 0
    if geuebt:
        tag = min(geuebt)
        while tag <= heute:
            if tag in geuebt:
                lauf += 1
                seit_schild += 1
                if seit_schild >= regeln.schild_alle_tage:
                    seit_schild = 0
                    schilde = min(regeln.schilde_max, schilde + 1)
                laengste = max(laengste, lauf)
            elif tag < heute:
                if schilde > 0:
                    schilde -= 1
                else:
                    lauf = seit_schild = 0
            tag += timedelta(days=1)
    voll = schilde >= regeln.schilde_max
    return SerienStand(
        aktuell=lauf,
        laengste=laengste,
        heute_geuebt=heute in geuebt,
        schilde=schilde,
        schilde_max=regeln.schilde_max,
        naechster_schild_in=None if voll else regeln.schild_alle_tage - seit_schild,
    )
