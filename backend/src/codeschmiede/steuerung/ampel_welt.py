"""Welt der Ampelschule: Wege, Fahrzeuge, Fußgänger, Unfälle und Sensoren.

Reines Python ohne Abhängigkeiten und ohne Importe aus dem Paket: dieselbe Quelle läuft in der Sandbox, wo sie dem
Programm jede Sekunde die Sensoren liefert, und im Backend, wo sie aus der Folge der Signale das Urteil rechnet
(ampel_pruefer). Aus der Sandbox kommt nur die Folge der Signale; was daraus folgt, zählt allein hier.

Eine Anlage (aus ampel_anlage) besteht aus Signalgruppen und Wegen. Ein Weg ist ein Linienzug in Bildpunkten mit
seiner Gruppe, bei Fahrbahnen mit Haltlinie und Kontaktschleife. Konfliktzonen (wo sich Wege fremder Gruppen kreuzen
oder zusammenlaufen) rechnet `konflikte` einmal im Backend aus; sie kommen fertig mit der Anlage.

Ein Ablauf nennt Dauer und Ankünfte (Zeit, Weg, Art), dazu Nachtzeiten, eine Störung und angemeldete
Einsatzfahrzeuge. Gerechnet wird in Takten zu DT Sekunden; das Programm stellt die Signale je volle Sekunde.
"""

import math

DT = 0.25
TAKTE = 4

ZUSTAENDE = {"auto": ("rot", "rotgelb", "gruen", "gelb", "gelb_blinkt"), "fuss": ("rot", "gruen", "aus")}
OFFEN = {"auto": ("gruen", "gelb", "rotgelb"), "fuss": ("gruen",)}

# Maße in Bildpunkten, Tempo in Bildpunkten je Sekunde
# "halten": bei Gelb fährt weiter, wer die Haltlinie in so vielen Sekunden erreicht (zu nah zum Halten)
ARTEN = {
    "auto": {"laenge": 26, "breite": 13, "tempo": 70, "halten": 0.45},
    "lkw": {"laenge": 54, "breite": 17, "tempo": 18, "halten": 1.6},
    "einsatz": {"laenge": 28, "breite": 14, "tempo": 80, "halten": 0.45},
    "fuss": {"laenge": 6, "breite": 6, "tempo": 28, "halten": 0},
}
ABSTAND = 7
# Wartende Fußgänger stehen am Bordstein hintereinander
FUSS_REIHE = 7
# Wer bei gelbem Blinklicht keine Vorfahrt hat, lässt Fahrzeuge vorbei, die so bald an der Konfliktzone sind
VORFAHRT_LUECKE = 2.5
# Einsatzfahrzeuge melden sich so viele Sekunden vor ihrer Ankunft
EINSATZ_VORLAUF = 12


class Melder(dict):
    """Ein Wert je Gruppe; als Wahrheitswert: ob irgendeine Gruppe meldet."""

    def __bool__(self):
        return any(self.values())


class Lage:
    """Was das Programm in takt(lage) sieht."""

    def __init__(self, sekunde, taster, schleife, wartend, frei, einsatz, nacht, stoerung):
        self.sekunde = sekunde
        self.taster = taster
        self.schleife = schleife
        self.wartend = wartend
        self.frei = frei
        self.einsatz = einsatz
        self.nacht = nacht
        self.stoerung = stoerung

    def __repr__(self):
        teile = ", ".join("%s=%r" % (k, v) for k, v in vars(self).items())
        return "Lage(%s)" % teile


def signale_pruefen(gruppen, wert):
    """Prüft, was takt() geliefert hat. Liefert das Signal je Gruppe oder einen Fehlertext."""
    if not isinstance(wert, dict):
        return "takt() muss ein dict liefern, etwa {%s}, nicht %s" % (
            ", ".join('"%s": "rot"' % g for g in gruppen), type(wert).__name__)
    fehlt = [g for g in gruppen if g not in wert]
    if fehlt:
        return "takt() liefert kein Signal für %s" % ", ".join(fehlt)
    fremd = [str(g) for g in wert if g not in gruppen]
    if fremd:
        return "unbekannte Gruppe %s; es gibt %s" % (", ".join(fremd), ", ".join(gruppen))
    signale = {}
    for name, gruppe in gruppen.items():
        z = wert[name]
        if z not in ZUSTAENDE[gruppe["art"]]:
            return 'Gruppe %s: "%s" gibt es nicht, erlaubt sind %s' % (
                name, z, ", ".join('"%s"' % x for x in ZUSTAENDE[gruppe["art"]]))
        signale[name] = z
    return signale


# --- Linienzüge ---------------------------------------------------------------


class Linie:
    def __init__(self, punkte):
        self.punkte = [(float(x), float(y)) for x, y in punkte]
        self.bis = [0.0]
        for (x1, y1), (x2, y2) in zip(self.punkte, self.punkte[1:]):
            self.bis.append(self.bis[-1] + math.hypot(x2 - x1, y2 - y1))
        self.laenge = self.bis[-1]

    def punkt(self, s):
        """Punkt bei Strecke s; davor und dahinter geht es geradeaus weiter."""
        p = self.punkte
        if s <= 0:
            k = 0
        elif s >= self.laenge:
            k = len(p) - 2
        else:
            k = 0
            while self.bis[k + 1] < s:
                k += 1
        (x1, y1), (x2, y2) = p[k], p[k + 1]
        stueck = self.bis[k + 1] - self.bis[k] or 1.0
        f = (s - self.bis[k]) / stueck
        return x1 + (x2 - x1) * f, y1 + (y2 - y1) * f


def konflikte(wege, eigene=False, schritt=2.0):
    """Konfliktzonen zwischen Wegen fremder Gruppen: wo sie sich näher kommen als ihre halben Breiten zusammen,
    ohne dabei schon auf derselben Spur zu liegen (nach dem Zusammenlaufen fährt man hintereinander).
    Liefert Einträge [weg_a, von_a, bis_a, weg_b, von_b, bis_b]. Mit eigene=True nur die Zonen innerhalb einer
    Gruppe zwischen verschiedenen Spuren; die darf eine Anlage nicht haben."""
    breite = {"fahrbahn": 10.0, "ueberweg": 6.0}
    linien = {w["id"]: Linie(w["punkte"]) for w in wege}
    ergebnis = []
    for i, a in enumerate(wege):
        for b in wege[i + 1:]:
            gleich = a["gruppe"] == b["gruppe"]
            if gleich != eigene or (eigene and (a.get("spur") or a["id"]) == (b.get("spur") or b["id"])):
                continue
            nah = (breite[a["art"]] + breite[b["art"]]) / 2
            la, lb = linien[a["id"]], linien[b["id"]]
            treffer = []
            for sa, (xa, ya) in _nahe_proben(la, lb, nah, schritt):
                for sb, (xb, yb) in _nahe_proben(lb, la, nah, schritt):
                    if abs(xa - xb) >= nah or abs(ya - yb) >= nah:
                        continue
                    d = math.hypot(xa - xb, ya - yb)
                    if d >= nah or (d < 3.0 and _gleichlaufend(la, sa, lb, sb)):
                        continue
                    treffer.append((sa, sb))
            for gruppe in _haufen(treffer, schritt * 3):
                ergebnis.append([a["id"], min(t[0] for t in gruppe), max(t[0] for t in gruppe),
                                 b["id"], min(t[1] for t in gruppe), max(t[1] for t in gruppe)])
    return ergebnis


def _nahe_proben(linie, andere, nah, schritt):
    """Proben von linie, aber nur auf Stücken, die einem Stück der anderen Linie nahe kommen."""
    def kasten(p, q):
        return min(p[0], q[0]) - nah, min(p[1], q[1]) - nah, max(p[0], q[0]) + nah, max(p[1], q[1]) + nah

    fremde = [kasten(p, q) for p, q in zip(andere.punkte, andere.punkte[1:])]
    proben = []
    for k, (p, q) in enumerate(zip(linie.punkte, linie.punkte[1:])):
        x1, y1, x2, y2 = kasten(p, q)
        if not any(x1 < f[2] and f[0] < x2 and y1 < f[3] and f[1] < y2 for f in fremde):
            continue
        von, bis = linie.bis[k], linie.bis[k + 1]
        anzahl = max(1, int((bis - von) / schritt))
        proben.extend((von + (bis - von) * j / anzahl, linie.punkt(von + (bis - von) * j / anzahl))
                      for j in range(anzahl + 1))
    return proben


def _gleichlaufend(la, sa, lb, sb):
    def richtung(linie, s):
        x1, y1 = linie.punkt(s - 1)
        x2, y2 = linie.punkt(s + 1)
        n = math.hypot(x2 - x1, y2 - y1) or 1.0
        return (x2 - x1) / n, (y2 - y1) / n

    (ax, ay), (bx, by) = richtung(la, sa), richtung(lb, sb)
    return ax * bx + ay * by > 0.95


def _haufen(treffer, luecke):
    """Teilt nahe Probenpaare in zusammenhängende Zonen (nach der Strecke auf dem ersten Weg)."""
    haufen = []
    for t in sorted(treffer):
        if haufen and t[0] - haufen[-1][-1][0] <= luecke:
            haufen[-1].append(t)
        else:
            haufen.append([t])
    return haufen


# --- Verkehr --------------------------------------------------------------------


class Teilnehmer:
    __slots__ = ("id", "art", "weg", "gruppe", "s", "laenge", "breite", "tempo", "ankunft", "warten",
                 "geht", "steht", "kaputt", "fertig", "vorbei")

    def __init__(self, nr, art, weg, ankunft):
        self.id = nr
        self.art = art
        self.weg = weg
        self.gruppe = weg.gruppe
        masse = ARTEN[art]
        self.laenge = masse["laenge"]
        self.breite = masse["breite"]
        self.tempo = masse["tempo"]
        self.ankunft = ankunft
        self.s = 0.0
        self.warten = 0.0
        self.geht = False
        # stand im letzten Takt (Fahrzeuge)
        self.steht = False
        self.kaputt = False
        self.fertig = False
        # über die Haltlinie (Fahrzeuge) oder losgegangen (Fußgänger)
        self.vorbei = False

    @property
    def fuss(self):
        return self.art == "fuss"

    def bereich(self):
        if self.fuss:
            return self.s - self.laenge / 2, self.s + self.laenge / 2
        return self.s - self.laenge, self.s


class Weg:
    def __init__(self, daten):
        self.id = daten["id"]
        self.art = daten["art"]
        self.gruppe = daten["gruppe"]
        self.spur = daten.get("spur") or self.id
        self.linie = Linie(daten["punkte"])
        self.halt = daten.get("halt")
        self.schleife = daten.get("schleife")
        # (meine Zone, fremder Weg, dessen Zone)
        self.zonen = []


class Welt:
    def __init__(self, anlage, ablauf, aufzeichnen=False):
        self.gruppen = {g["name"]: g for g in anlage["gruppen"]}
        self.wege = {w["id"]: Weg(w) for w in anlage["wege"]}
        self.feindlich = {g: set() for g in self.gruppen}
        for a, von_a, bis_a, b, von_b, bis_b in anlage["konflikte"]:
            wa, wb = self.wege[a], self.wege[b]
            wa.zonen.append(((von_a, bis_a), wb, (von_b, bis_b)))
            wb.zonen.append(((von_b, bis_b), wa, (von_a, bis_a)))
            self.feindlich[wa.gruppe].add(wb.gruppe)
            self.feindlich[wb.gruppe].add(wa.gruppe)
        self.dauer = ablauf["dauer"]
        self.ankuenfte = sorted(ablauf["ankuenfte"], key=lambda a: (a["t"], a["weg"]))
        self.nachtzeiten = ablauf.get("nacht") or []
        self.stoerung = ablauf.get("stoerung")
        self.einsaetze = [a for a in self.ankuenfte if a["art"] == "einsatz"]
        self.naechste = 0
        self.wartend_vor_eintritt = []
        self.takt = 0
        self.signale = {g: "rot" for g in self.gruppen}
        self.unterwegs = []
        self.alle = []
        self.unfaelle = []
        self.paare = set()
        self.aufzeichnen = aufzeichnen
        self.bilder = []

    @property
    def zeit(self):
        return self.takt * DT

    # --- Sensoren ---------------------------------------------------------------

    def nacht(self, sekunde):
        return any(von <= sekunde < bis for von, bis in self.nachtzeiten)

    def gestoert(self, sekunde):
        if self.stoerung and sekunde >= self.stoerung["ab"]:
            return self.stoerung["gruppe"]
        return None

    def angemeldet(self, sekunde):
        """Gruppe eines angemeldeten Einsatzfahrzeugs, bis es über die Haltlinie ist."""
        for a in self.einsaetze:
            if a["t"] - EINSATZ_VORLAUF <= sekunde:
                t = self._teilnehmer_zu(a)
                if t is None or not t.vorbei:
                    return self.wege[a["weg"]].gruppe
        return None

    def _teilnehmer_zu(self, ankunft):
        for t in self.alle:
            if t.art == ankunft["art"] and t.weg.id == ankunft["weg"] and t.ankunft == ankunft["t"]:
                return t
        return None

    def bedarf(self):
        """Wer gerade auf Grün wartet, je Gruppe: Fußgänger am Taster, Fahrzeuge auf der Schleife oder im Stau."""
        sekunde = int(self.zeit)
        gestoert = self.gestoert(sekunde)
        wartend = {g: 0 for g in self.gruppen}
        schleife = {g: False for g in self.gruppen if self.gruppen[g]["art"] == "auto"}
        for t in self.unterwegs:
            if t.kaputt:
                continue
            if t.fuss:
                if not t.geht:
                    wartend[t.gruppe] += 1
                continue
            if not t.vorbei and t.steht:
                wartend[t.gruppe] += 1
            sch = t.weg.schleife
            if sch and t.gruppe != gestoert:
                von, bis = t.bereich()
                if von < sch[1] and bis > sch[0]:
                    schleife[t.gruppe] = True
        for a in self.wartend_vor_eintritt:
            wartend[self.wege[a["weg"]].gruppe] += 1
        return wartend, schleife

    def frei(self):
        """Je Gruppe: keine fremden Teilnehmer in den Konfliktzonen ihrer Wege."""
        belegt = {g: False for g in self.gruppen}
        for t in self.unterwegs:
            if t.fuss and not t.geht:
                continue
            von, bis = t.bereich()
            for (z_von, z_bis), fremd, _ in t.weg.zonen:
                if von < z_bis and bis > z_von:
                    belegt[fremd.gruppe] = True
        return {g: not b for g, b in belegt.items()}

    def lage(self):
        sekunde = int(round(self.zeit))
        wartend, schleife = self.bedarf()
        taster = {g: wartend[g] > 0 for g in self.gruppen if self.gruppen[g]["art"] == "fuss"}
        return Lage(
            sekunde=sekunde,
            taster=Melder(taster),
            schleife=Melder(schleife),
            wartend=wartend,
            frei=self.frei(),
            einsatz=self.angemeldet(sekunde),
            nacht=self.nacht(sekunde),
            stoerung=self.gestoert(sekunde),
        )

    # --- Ablauf -----------------------------------------------------------------

    def sekunde(self, signale):
        """Stellt die Signale und rechnet eine Sekunde weiter."""
        self.signale = dict(signale)
        for _ in range(TAKTE):
            self._schritt()

    def _schritt(self):
        jetzt = self.zeit
        self._ankommen(jetzt)
        self._fussgaenger()
        self._fahrzeuge()
        self._unfaelle(jetzt)
        for t in self.unterwegs:
            if not t.fertig and t.s - t.laenge > t.weg.linie.laenge + 12:
                t.fertig = True
        self.unterwegs = [t for t in self.unterwegs if not t.fertig]
        for a in self.wartend_vor_eintritt:
            a["warten"] = a.get("warten", 0.0) + DT
        self.takt += 1
        if self.aufzeichnen:
            self.bilder.append([round(self.zeit, 2), [[t.id, round(t.s, 1)] for t in self.unterwegs]])

    def _ankommen(self, jetzt):
        while self.naechste < len(self.ankuenfte) and self.ankuenfte[self.naechste]["t"] <= jetzt + 1e-9:
            self.wartend_vor_eintritt.append(dict(self.ankuenfte[self.naechste]))
            self.naechste += 1
        bleiben = []
        for a in self.wartend_vor_eintritt:
            weg = self.wege[a["weg"]]
            if a["art"] == "fuss":
                vor = sum(1 for t in self.unterwegs if t.weg is weg and not t.geht)
                t = Teilnehmer(len(self.alle), "fuss", weg, a["t"])
                t.s = -ARTEN["fuss"]["laenge"] / 2 - vor * FUSS_REIHE
                self._eintreten(t, a)
                continue
            letzter = min((t.s - t.laenge for t in self.unterwegs if t.weg.spur == weg.spur and not t.fuss),
                          default=None)
            if letzter is not None and letzter < ABSTAND:
                bleiben.append(a)
                continue
            self._eintreten(Teilnehmer(len(self.alle), a["art"], weg, a["t"]), a)
        self.wartend_vor_eintritt = bleiben

    def _eintreten(self, t, ankunft):
        t.warten = ankunft.get("warten", 0.0)
        self.alle.append(t)
        self.unterwegs.append(t)

    def _fussgaenger(self):
        for t in self.unterwegs:
            if not t.fuss or t.fertig:
                continue
            if not t.geht:
                if self.signale[t.gruppe] == "gruen":
                    t.geht = True
                    t.vorbei = True
                else:
                    t.warten += DT
                    continue
            t.s += t.tempo * DT
            if t.s > t.weg.linie.laenge + t.laenge:
                t.fertig = True

    def _fahrzeuge(self):
        fahrzeuge = [t for t in self.unterwegs if not t.fuss]
        for t in sorted(fahrzeuge, key=lambda t: -t.s):
            weg = t.weg
            soll = t.tempo * DT
            if t.kaputt:
                t.steht = True
                continue
            erlaubt = soll
            if weg.halt is not None and not t.vorbei:
                bis_halt = weg.halt - t.s
                if not self._darf_fahren(t, bis_halt):
                    erlaubt = min(erlaubt, max(0.0, bis_halt))
            vorne = self._vordermann(t, fahrzeuge)
            if vorne is not None:
                erlaubt = min(erlaubt, max(0.0, vorne.s - vorne.laenge - ABSTAND - t.s))
            # Warten heißt: vor der Haltlinie stehen (hinter einem langsamen Lkw herzufahren zählt nicht)
            t.steht = erlaubt < soll * 0.1
            if t.steht and not t.vorbei:
                t.warten += DT
            t.s += erlaubt
            if weg.halt is not None and t.s > weg.halt:
                t.vorbei = True

    def _darf_fahren(self, t, bis_halt):
        zustand = self.signale[t.gruppe]
        if zustand == "gruen":
            return True
        if zustand == "gelb":
            return bis_halt < t.tempo * ARTEN[t.art]["halten"]
        if zustand == "gelb_blinkt":
            if self.gruppen[t.gruppe].get("vorfahrt"):
                return True
            return not self._kommt_jemand(t)
        return False

    def _kommt_jemand(self, t):
        """Ob ein fremder Teilnehmer in einer Konfliktzone von t ist oder bald dort ankommt."""
        for _, fremd, (z_von, z_bis) in t.weg.zonen:
            for a in self.unterwegs:
                if a.weg is not fremd or a.fertig or (a.fuss and not a.geht):
                    continue
                von, bis = a.bereich()
                if von < z_bis and bis + a.tempo * VORFAHRT_LUECKE > z_von:
                    return True
        return False

    def _vordermann(self, t, fahrzeuge):
        bester = None
        for a in fahrzeuge:
            if a is t or a.s <= t.s:
                continue
            gleich = a.weg is t.weg or (a.weg.spur == t.weg.spur and not t.vorbei and not a.vorbei)
            if gleich and (bester is None or a.s < bester.s):
                bester = a
        return bester

    def _unfaelle(self, jetzt):
        for t in list(self.unterwegs):
            if t.fertig or (t.fuss and not t.geht):
                continue
            von, bis = t.bereich()
            for (z_von, z_bis), fremd, (f_von, f_bis) in t.weg.zonen:
                if not (von < z_bis and bis > z_von):
                    continue
                for a in self.unterwegs:
                    if a.weg is not fremd or a.fertig or (a.fuss and not a.geht) or a.id < t.id:
                        continue
                    a_von, a_bis = a.bereich()
                    if a_von < f_bis and a_bis > f_von and (t.id, a.id) not in self.paare:
                        self._unfall(jetzt, t, a)

    def _unfall(self, jetzt, a, b):
        if a.fuss and b.fuss:
            return
        # wer zu Fuß an ein stehendes Fahrzeug stößt, geht drumherum
        if (a.fuss and b.steht) or (b.fuss and a.steht):
            return
        self.paare.add((a.id, b.id))
        fuss = a if a.fuss else (b if b.fuss else None)
        if fuss is not None:
            fahrzeug = b if fuss is a else a
            x, y = fuss.weg.linie.punkt(fuss.s)
            fuss.fertig = True
            fahrzeug.kaputt = True
            art = "fuss"
        else:
            if a.kaputt and b.kaputt:
                return
            x1, y1 = a.weg.linie.punkt(a.s - a.laenge / 2)
            x2, y2 = b.weg.linie.punkt(b.s - b.laenge / 2)
            x, y = (x1 + x2) / 2, (y1 + y2) / 2
            a.kaputt = b.kaputt = True
            art = "blech"
        self.unfaelle.append({"t": round(jetzt + DT, 2), "art": art, "ids": [a.id, b.id],
                              "gruppen": [a.gruppe, b.gruppe], "x": round(x, 1), "y": round(y, 1)})

    # --- Auswertung -------------------------------------------------------------

    def bilanz(self):
        """Wartezeiten aller Teilnehmer, auch derer, die noch vor dem Rand stehen."""
        teilnehmer = [{"id": t.id, "art": t.art, "weg": t.weg.id, "gruppe": t.gruppe, "ankunft": t.ankunft,
                       "warten": round(t.warten, 2), "vorbei": t.vorbei}
                      for t in self.alle]
        for a in self.wartend_vor_eintritt:
            teilnehmer.append({"id": None, "art": a["art"], "weg": a["weg"], "gruppe": self.wege[a["weg"]].gruppe,
                               "ankunft": a["t"], "warten": round(a.get("warten", 0.0), 2), "vorbei": False})
        return teilnehmer


def nachspielen(anlage, ablauf, signale, aufzeichnen=True):
    """Spielt eine Folge von Signalen nach (eine je Sekunde). Liefert die Welt danach und je Sekunde den Bedarf,
    mit dem das Programm entschieden hat."""
    welt = Welt(anlage, ablauf, aufzeichnen=aufzeichnen)
    verlauf = []
    for s in signale:
        lage = welt.lage()
        bedarf = {g: lage.wartend[g] > 0 or bool(lage.schleife.get(g)) or lage.einsatz == g for g in welt.gruppen}
        verlauf.append({"bedarf": bedarf,
                        "nacht": lage.nacht, "einsatz": lage.einsatz, "stoerung": lage.stoerung})
        welt.sekunde(s)
    return welt, verlauf
