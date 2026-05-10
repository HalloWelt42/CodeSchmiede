"""SM-2 Algorithmus (Anki-Stil) für Spaced Repetition.

Ergebnis eines Wiederholungsversuchs ist die Qualitaet `q` (0-5):
  5 = perfekt erinnert
  4 = gut, kleine Unsicherheit
  3 = bestanden mit Muehe
  0-2 = nicht bestanden

Daraus werden neuer Easiness-Faktor und neues Intervall berechnet.
Mapping in der Codeschmiede:
  bestanden im ersten Versuch  -> q=4
  bestanden mit mehreren Anlaeufen  -> q=3
  nicht bestanden  -> q=1
"""

from dataclasses import dataclass


MIN_EASE = 1.3
DEFAULT_EASE = 2.5


@dataclass(frozen=True)
class SM2Schritt:
    ease: float
    intervall_tage: int


def berechne_naechsten_schritt(
    ease: float,
    intervall_tage: int,
    qualitaet: int,
) -> SM2Schritt:
    """Berechnet das nächste Wiederholungs-Intervall."""
    q = max(0, min(5, qualitaet))

    if q < 3:
        return SM2Schritt(ease=ease, intervall_tage=1)

    if intervall_tage <= 0:
        neues_intervall = 1
    elif intervall_tage == 1:
        neues_intervall = 6
    else:
        neues_intervall = round(intervall_tage * ease)

    delta = 0.1 - (5 - q) * (0.08 + (5 - q) * 0.02)
    neues_ease = max(MIN_EASE, ease + delta)

    return SM2Schritt(ease=neues_ease, intervall_tage=neues_intervall)
