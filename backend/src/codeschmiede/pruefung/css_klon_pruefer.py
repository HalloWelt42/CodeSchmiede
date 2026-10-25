"""Pruefer für `task_type: css_klon`.

CSS-Nachbauten kann nur ein Browser rendern. Er rastert Ziel und eigenes
Ergebnis auf derselben Bühne und meldet die Deckung: den Anteil der
Bildpunkte im Motiv, die mit dem Ziel übereinstimmen (Motiv sind alle
Punkte, die bei Ziel oder eigenem Bild nicht Grund sind). Bestehen,
Sterne und Punkte entscheidet hier der Server, die Zeichenzahl misst er
selbst.

Wertung (Regeln unten):
  Bestehen ab 95 % Deckung.
  Sterne: 95 %; 99 %; 99 % und höchstens so kurz wie die kürzeste
  Musterlösung (Zeichen ohne Leerraum).
  Punkte: bis 60 % für die Deckung, linear ab 80 %; die übrigen 40 %
  als Kürzebonus erst ab 99 % Deckung, im Verhältnis Musterlösung zu
  eigenem Code (höchstens voll).

Ziel und Markup sind von Natur aus sichtbar: wer das Ziel sieht, sieht
auch seine Stile. Einen Lauf über die Sandbox gibt es für diesen Typ
nicht.
"""

from ..models.aufgabe import Aufgabe
from ..progress.submissions import codelaenge
from ..sandbox.runner import Runner
from .ergebnis import Kennwerte, Messung, PruefErgebnis, PunkteTeil, SternKriterium, Wertung
from .registry import registriere

BESTEHEN = 0.95
GUT = 0.99
DECKUNG_AB = 0.80
ANTEIL_DECKUNG = 0.6
ANTEIL_KUERZE = 1 - ANTEIL_DECKUNG
# volle Deckung: auf eine Stelle gerundet 100,0 % (Erfolg "Pixelgenau")
VOLL = 0.9995


def prozent(wert: float) -> str:
    return f"{round(wert * 100)} %"


def punkteteile(deckung: float, zeichen: int, muster: int | None) -> list[PunkteTeil]:
    deckungsteil = ANTEIL_DECKUNG * min(1.0, max(0.0, (deckung - DECKUNG_AB) / (1 - DECKUNG_AB)))
    kuerze = 1.0 if muster is None else min(1.0, muster / max(1, zeichen))
    kuerzeteil = ANTEIL_KUERZE * kuerze if deckung >= GUT else 0.0
    return [
        PunkteTeil(text="Deckung", anteil=deckungsteil, moeglich=ANTEIL_DECKUNG),
        PunkteTeil(text="Kürze", anteil=kuerzeteil, moeglich=ANTEIL_KUERZE, bedingung=f"ab {prozent(GUT)}"),
    ]


def kriterien(deckung: float, zeichen: int, muster: int | None) -> list[SternKriterium]:
    kurz = muster is None or zeichen <= muster
    return [
        SternKriterium(text=f"mindestens {prozent(BESTEHEN)} Deckung", erreicht=deckung >= BESTEHEN),
        SternKriterium(text=f"mindestens {prozent(GUT)} Deckung", erreicht=deckung >= GUT),
        SternKriterium(
            text="dazu so kurz wie die Musterlösung" if muster is None else f"dazu höchstens {muster} Zeichen",
            erreicht=deckung >= GUT and kurz,
        ),
    ]


def werte(aufgabe: Aufgabe, code: str, messung: Messung, muster: int | None) -> PruefErgebnis:
    zeichen = codelaenge(code)
    sternkriterien = kriterien(messung.deckung, zeichen, muster)
    sterne = 0
    for k in sternkriterien:
        if not k.erreicht:
            break
        sterne += 1
    return PruefErgebnis(
        bestanden=messung.deckung >= BESTEHEN,
        sichtbar=[],
        versteckt_pass=0,
        versteckt_fail=0,
        laufzeit_ms=messung.laufzeit_ms,
        wertung=Wertung(
            sterne=sterne,
            kriterien=sternkriterien,
            kennwerte=Kennwerte(deckung=messung.deckung),
            teile=punkteteile(messung.deckung, zeichen, muster),
        ),
    )


@registriere("css_klon", abgabe="browser", werte=werte)
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    raise ValueError(f"Aufgabe {aufgabe.id} wird im Browser gemessen")
