"""Anlagen der Ampelschule: aus wenigen Angaben der Level-Datei Wege, Signalgruppen, Konfliktzonen und Zeichnung.

Zwei Vorlagen:
  ueberweg   eine Straße mit zwei Richtungen und ein Fußgängerüberweg; Gruppen "auto" und "fuss"
  kreuzung   bis zu vier Zufahrten mit ein oder zwei Spuren, je Spur Bewegungen und Gruppe, Überwege je Zufahrt

Rechtsverkehr, Bildpunkte, y wächst nach unten. Die Kreuzung wird für die Zufahrt Süd gebaut (Fahrzeuge kommen von
unten) und für die anderen Zufahrten gedreht. Der Browser zeichnet nur, was hier entsteht.

Wege heißen nach Zufahrt und Bewegung ("sued_links", beim Überweg "west_gerade"), Überwege nach ihrer Zufahrt in
beiden Gehrichtungen ("ueberweg_nord_a", "ueberweg_nord_b").
"""

import json
from functools import lru_cache
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field

from . import ampel_welt

Arm = Literal["nord", "ost", "sued", "west"]
Bewegung = Literal["gerade", "rechts", "links"]
ARME: tuple[Arm, ...] = ("nord", "ost", "sued", "west")
DREHUNG: dict[str, int] = {"sued": 0, "west": 1, "nord": 2, "ost": 3}
ARM_NAME = {"nord": "Nord", "ost": "Ost", "sued": "Süd", "west": "West"}
BEWEGUNG_NAME = {"gerade": "geradeaus", "rechts": "rechts", "links": "links"}

SPUR = 22.0
GEHWEG = 14.0
WEIT = 280.0


class Spur(BaseModel):
    model_config = ConfigDict(extra="forbid")

    wege: list[Bewegung] = Field(min_length=1)
    gruppe: str


class Zufahrt(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # von innen (an der Mitte) nach außen
    spuren: list[Spur] = Field(min_length=1, max_length=2)


class UeberwegVorgabe(BaseModel):
    model_config = ConfigDict(extra="forbid")

    vorlage: Literal["ueberweg"]
    schleifen: bool = False


class KreuzungVorgabe(BaseModel):
    model_config = ConfigDict(extra="forbid")

    vorlage: Literal["kreuzung"]
    zufahrten: dict[Arm, Zufahrt] = Field(min_length=2)
    # je Zufahrt die Gruppe ihres Überwegs
    ueberwege: dict[Arm, str] = Field(default_factory=dict)
    # Gruppen mit Vorfahrt, wenn gelb geblinkt wird
    vorfahrt: list[str] = Field(default_factory=list)
    schleifen: bool = False


AnlageVorgabe = Annotated[UeberwegVorgabe | KreuzungVorgabe, Field(discriminator="vorlage")]

Punkt = tuple[float, float]


class Gruppe(BaseModel):
    name: str
    art: Literal["auto", "fuss"]
    text: str
    vorfahrt: bool = False


class Weg(BaseModel):
    id: str
    art: Literal["fahrbahn", "ueberweg"]
    gruppe: str
    zufahrt: str
    spur: str
    punkte: list[Punkt]
    # Strecke bis zur Haltlinie und Bereich der Kontaktschleife (Fahrbahnen)
    halt: float | None = None
    schleife: tuple[float, float] | None = None


class Flaeche(BaseModel):
    klasse: Literal["gehweg", "strasse", "zebra", "schleife"]
    punkte: list[Punkt]


class Strich(BaseModel):
    klasse: Literal["mittellinie", "spurlinie", "haltlinie"]
    punkte: list[Punkt]


class Signalkopf(BaseModel):
    gruppe: str
    art: Literal["auto", "fuss"]
    x: float
    y: float
    # Drehung in Grad im Uhrzeigersinn, damit der Kopf zu seiner Zufahrt schaut
    drehung: int = 0


class Tasterbild(BaseModel):
    gruppe: str
    x: float
    y: float


class Pfeil(BaseModel):
    x: float
    y: float
    # Fahrtrichtung in Grad im Uhrzeigersinn, 0 heißt nach oben
    drehung: int
    richtungen: list[Bewegung]


class Zeichnung(BaseModel):
    flaechen: list[Flaeche] = Field(default_factory=list)
    striche: list[Strich] = Field(default_factory=list)
    signale: list[Signalkopf] = Field(default_factory=list)
    taster: list[Tasterbild] = Field(default_factory=list)
    pfeile: list[Pfeil] = Field(default_factory=list)


class Anlage(BaseModel):
    breite: int
    hoehe: int
    gruppen: list[Gruppe]
    wege: list[Weg]
    # [weg_a, von_a, bis_a, weg_b, von_b, bis_b]
    konflikte: list[tuple[str, float, float, str, float, float]]
    zeichnung: Zeichnung

    def fuer_welt(self) -> dict:
        """Was die Welt braucht (ohne Zeichnung); geht so auch in die Sandbox."""
        return {
            "gruppen": [g.model_dump(include={"name", "art", "vorfahrt"}) for g in self.gruppen],
            "wege": [w.model_dump(exclude={"zufahrt"}) for w in self.wege],
            "konflikte": [list(k) for k in self.konflikte],
        }

    def zufahrt_wege(self, zufahrt: str) -> list[str]:
        return [w.id for w in self.wege if w.zufahrt == zufahrt and w.art == "fahrbahn"]

    def ueberweg_wege(self, zufahrt: str) -> list[str]:
        return [w.id for w in self.wege if w.zufahrt == zufahrt and w.art == "ueberweg"]


def baue(vorgabe: UeberwegVorgabe | KreuzungVorgabe) -> Anlage:
    return _baue_gespeichert(vorgabe.model_dump_json())


@lru_cache(maxsize=64)
def _baue_gespeichert(vorgabe_json: str) -> Anlage:
    daten = json.loads(vorgabe_json)
    if daten["vorlage"] == "ueberweg":
        anlage = _ueberweg(UeberwegVorgabe.model_validate(daten))
    else:
        anlage = _kreuzung(KreuzungVorgabe.model_validate(daten))
    wege = [w.model_dump() for w in anlage.wege]
    anlage.konflikte = [tuple(k) for k in ampel_welt.konflikte(wege)]
    return anlage


def befunde(vorgabe: UeberwegVorgabe | KreuzungVorgabe) -> list[str]:
    """Was an einer Anlage nicht stimmt: Gruppen mit Autos und Fußgängern zugleich, Wege einer Gruppe, die sich
    kreuzen (sie würden bei Grün zusammenstoßen), Vorfahrt für unbekannte Gruppen."""
    if isinstance(vorgabe, KreuzungVorgabe):
        autos = {s.gruppe for z in vorgabe.zufahrten.values() for s in z.spuren}
        fuss = set(vorgabe.ueberwege.values())
        meldungen = [f"Gruppe {g} hat Autos und Fußgänger" for g in sorted(autos & fuss)]
        meldungen += [f"Vorfahrt für unbekannte Gruppe {g}" for g in vorgabe.vorfahrt if g not in autos]
        if meldungen:
            return meldungen
    anlage = baue(vorgabe)
    wege = [w.model_dump() for w in anlage.wege]
    return [f"Wege {a} und {b} derselben Gruppe kreuzen sich" for a, _, _, b, _, _ in ampel_welt.konflikte(wege, eigene=True)]


# --- Überweg --------------------------------------------------------------------


def _rechteck(x1: float, y1: float, x2: float, y2: float) -> list[Punkt]:
    return [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]


def _ueberweg(vorgabe: UeberwegVorgabe) -> Anlage:
    breite, hoehe = 400, 220
    mitte = hoehe / 2
    oben, unten = mitte - SPUR, mitte + SPUR
    zebra_l, zebra_r = 186.0, 214.0
    halt_ost, halt_west = zebra_l - 6, zebra_r + 6
    rand = 40.0

    def schleife(halt: float) -> tuple[float, float] | None:
        return (halt - 30, halt) if vorgabe.schleifen else None

    wege = [
        Weg(id="west_gerade", art="fahrbahn", gruppe="auto", zufahrt="west", spur="west_0",
            punkte=[(-rand, mitte + SPUR / 2), (breite + rand, mitte + SPUR / 2)],
            halt=halt_ost + rand, schleife=schleife(halt_ost + rand)),
        Weg(id="ost_gerade", art="fahrbahn", gruppe="auto", zufahrt="ost", spur="ost_0",
            punkte=[(breite + rand, mitte - SPUR / 2), (-rand, mitte - SPUR / 2)],
            halt=breite + rand - halt_west, schleife=schleife(breite + rand - halt_west)),
        Weg(id="ueberweg_mitte_a", art="ueberweg", gruppe="fuss", zufahrt="mitte", spur="ueberweg_mitte",
            punkte=[(200.0, oben - 7), (200.0, unten + 7)]),
        Weg(id="ueberweg_mitte_b", art="ueberweg", gruppe="fuss", zufahrt="mitte", spur="ueberweg_mitte",
            punkte=[(200.0, unten + 7), (200.0, oben - 7)]),
    ]
    z = Zeichnung()
    z.flaechen.append(Flaeche(klasse="gehweg", punkte=_rechteck(0, oben - GEHWEG - 2, breite, unten + GEHWEG + 2)))
    z.flaechen.append(Flaeche(klasse="strasse", punkte=_rechteck(0, oben, breite, unten)))
    y = oben + 3
    while y < unten - 3:
        z.flaechen.append(Flaeche(klasse="zebra", punkte=_rechteck(zebra_l, y, zebra_r, y + 4)))
        y += 7
    if vorgabe.schleifen:
        z.flaechen.append(Flaeche(klasse="schleife", punkte=_rechteck(halt_ost - 30, mitte + 4, halt_ost, unten - 4)))
        z.flaechen.append(Flaeche(klasse="schleife", punkte=_rechteck(halt_west, oben + 4, halt_west + 30, mitte - 4)))
    z.striche += [
        Strich(klasse="mittellinie", punkte=[(0, mitte), (halt_ost, mitte)]),
        Strich(klasse="mittellinie", punkte=[(halt_west, mitte), (breite, mitte)]),
        Strich(klasse="haltlinie", punkte=[(halt_ost, mitte), (halt_ost, unten)]),
        Strich(klasse="haltlinie", punkte=[(halt_west, oben), (halt_west, mitte)]),
    ]
    z.signale += [
        Signalkopf(gruppe="auto", art="auto", x=halt_ost - 26, y=unten + 34),
        Signalkopf(gruppe="auto", art="auto", x=halt_west + 26, y=oben - 34),
        Signalkopf(gruppe="fuss", art="fuss", x=zebra_l - 12, y=oben - 30),
        Signalkopf(gruppe="fuss", art="fuss", x=zebra_r + 12, y=unten + 30),
    ]
    z.taster += [Tasterbild(gruppe="fuss", x=zebra_l - 26, y=oben - 24), Tasterbild(gruppe="fuss", x=zebra_r + 26, y=unten + 24)]
    gruppen = [
        Gruppe(name="auto", art="auto", text="Autos in beiden Richtungen"),
        Gruppe(name="fuss", art="fuss", text="Fußgänger am Überweg"),
    ]
    return Anlage(breite=breite, hoehe=hoehe, gruppen=gruppen, wege=wege, konflikte=[], zeichnung=z)


# --- Kreuzung -------------------------------------------------------------------


def _dreh(p: Punkt, k: int, mitte: float) -> Punkt:
    x, y = p
    for _ in range(k):
        x, y = -y, x
    return round(x + mitte, 2), round(y + mitte, 2)


def _bogen(p0: Punkt, steuer: Punkt, p2: Punkt, teile: int = 10) -> list[Punkt]:
    punkte = []
    for i in range(1, teile + 1):
        t = i / teile
        punkte.append((
            (1 - t) ** 2 * p0[0] + 2 * t * (1 - t) * steuer[0] + t * t * p2[0],
            (1 - t) ** 2 * p0[1] + 2 * t * (1 - t) * steuer[1] + t * t * p2[1],
        ))
    return punkte


def _kreuzung(vorgabe: KreuzungVorgabe) -> Anlage:
    groesse = 400
    mitte = groesse / 2
    kasten = max(len(z.spuren) for z in vorgabe.zufahrten.values()) * SPUR + 12
    wege: list[Weg] = []
    z = Zeichnung()
    def mittig(punkte: list[Punkt]) -> list[Punkt]:
        return [_dreh(p, 0, mitte) for p in punkte]

    gehwege = [Flaeche(klasse="gehweg", punkte=mittig(_rechteck(-kasten - GEHWEG, -kasten - GEHWEG, kasten + GEHWEG, kasten + GEHWEG)))]
    strassen = [Flaeche(klasse="strasse", punkte=mittig(_rechteck(-kasten, -kasten, kasten, kasten)))]
    flaechen: list[Flaeche] = []
    texte: dict[str, list[str]] = {}

    for arm in ARME:
        if arm not in vorgabe.zufahrten:
            continue
        zufahrt = vorgabe.zufahrten[arm]
        k = DREHUNG[arm]

        def d(p: Punkt, k: int = k) -> Punkt:
            return _dreh(p, k, mitte)

        def dl(punkte: list[Punkt]) -> list[Punkt]:
            return [d(p) for p in punkte]

        n = len(zufahrt.spuren)
        mit_ueberweg = arm in vorgabe.ueberwege
        y_halt = kasten + (20 if mit_ueberweg else 4)
        gehwege.append(Flaeche(klasse="gehweg", punkte=dl(_rechteck(-SPUR - GEHWEG, kasten, n * SPUR + GEHWEG, WEIT))))
        strassen.append(Flaeche(klasse="strasse", punkte=dl(_rechteck(-SPUR, kasten, n * SPUR, WEIT))))
        z.striche.append(Strich(klasse="mittellinie", punkte=dl([(0, y_halt), (0, WEIT)])))
        z.striche.append(Strich(klasse="haltlinie", punkte=dl([(0, y_halt), (n * SPUR, y_halt)])))
        for i in range(1, n):
            z.striche.append(Strich(klasse="spurlinie", punkte=dl([(i * SPUR, y_halt), (i * SPUR, WEIT)])))

        for i, spur in enumerate(zufahrt.spuren):
            x = SPUR / 2 + i * SPUR
            halt = WEIT - y_halt
            schleife = (halt - 30, halt) if vorgabe.schleifen else None
            for bewegung in spur.wege:
                if bewegung == "gerade":
                    rest = [(SPUR / 2, -kasten), (SPUR / 2, -WEIT)]
                elif bewegung == "rechts":
                    rest = [*_bogen((x, kasten), (x, SPUR / 2), (kasten, SPUR / 2)), (WEIT, SPUR / 2)]
                else:
                    rest = [*_bogen((x, kasten), (x, -SPUR / 2), (-kasten, -SPUR / 2)), (-WEIT, -SPUR / 2)]
                wege.append(Weg(
                    id=f"{arm}_{bewegung}", art="fahrbahn", gruppe=spur.gruppe, zufahrt=arm, spur=f"{arm}_{i}",
                    punkte=dl([(x, WEIT), (x, kasten), *rest]), halt=halt, schleife=schleife,
                ))
            texte.setdefault(spur.gruppe, []).append(f"{ARM_NAME[arm]} {', '.join(BEWEGUNG_NAME[b] for b in spur.wege)}")
            if vorgabe.schleifen:
                flaechen.append(Flaeche(klasse="schleife", punkte=dl(_rechteck(x - 6, y_halt + 2, x + 6, y_halt + 30))))
            px, py = d((x, y_halt + 46))
            z.pfeile.append(Pfeil(x=px, y=py, drehung=k * 90, richtungen=spur.wege))
            sx, sy = d((n * SPUR + 10 + (n - 1 - i) * 14, y_halt + 18))
            z.signale.append(Signalkopf(gruppe=spur.gruppe, art="auto", x=sx, y=sy, drehung=k * 90))

        if mit_ueberweg:
            gruppe = vorgabe.ueberwege[arm]
            y = kasten + 10
            links, rechts = (-SPUR - 7, y), (n * SPUR + 7, y)
            for name, (a, b) in (("a", (links, rechts)), ("b", (rechts, links))):
                wege.append(Weg(id=f"ueberweg_{arm}_{name}", art="ueberweg", gruppe=gruppe, zufahrt=arm,
                                spur=f"ueberweg_{arm}", punkte=dl([a, b])))
            streifen = -SPUR + 1
            while streifen < n * SPUR - 2:
                flaechen.append(Flaeche(klasse="zebra", punkte=dl(_rechteck(streifen, kasten + 4, streifen + 3.5, kasten + 16))))
                streifen += 6
            for sx, sy in ((n * SPUR + 9, kasten - 12), (-SPUR - 9, kasten - 12)):
                x, y2 = d((sx, sy))
                z.signale.append(Signalkopf(gruppe=gruppe, art="fuss", x=x, y=y2, drehung=k * 90))
            tx, ty = d((n * SPUR + 20, kasten - 4))
            z.taster.append(Tasterbild(gruppe=gruppe, x=tx, y=ty))
            texte.setdefault(gruppe, []).append(f"Überweg {ARM_NAME[arm]}")

    z.flaechen = gehwege + strassen + flaechen
    autos = {s.gruppe for zf in vorgabe.zufahrten.values() for s in zf.spuren}
    gruppen = [
        Gruppe(name=g, art="auto" if g in autos else "fuss", text="; ".join(t), vorfahrt=g in vorgabe.vorfahrt)
        for g, t in texte.items()
    ]
    return Anlage(breite=groesse, hoehe=groesse, gruppen=gruppen, wege=wege, konflikte=[], zeichnung=z)
