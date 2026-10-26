"""Welt der Aufzugsteuerung: Haus, Kabinen, Türen, Fahrgäste.

Reines Python ohne Abhängigkeiten, dieselbe Quelle läuft in der Sandbox und im Backend (Schnittstelle in
sandbox_lauf). Jede Kabine fragt das Programm, sobald sie mit ihrem Befehl fertig ist:

  "hoch", "runter"   eine Etage weiter (TEMPO Sekunden), nur mit geschlossener Tür
  "auf"              Tür öffnen (eine Sekunde); bei offener Tür steigen erst alle aus, dann ein, je eine Sekunde
  "zu"               Tür schließen (eine Sekunde); nicht, solange jemand in der Tür ist oder die Kabine überladen ist
  "warten"           eine Sekunde nichts tun (bei offener Tür geht das Aus- und Einsteigen weiter)

Ein Fahrgast kommt zu seiner Zeit an seiner Etage an und drückt den Ruf in seine Richtung. Er steigt ein, sobald
dort die Tür offen ist und Platz ist, und drückt dann sein Ziel; wo die Kabine hält, entscheidet das Programm. Ist die Kabine zu
schwer, wird zwei Sekunden verhandelt (UEBERLAST_PAUSE), dann steigt wieder aus, wer zuletzt kam, und wartet auf die
nächste. Bei Feueralarm steigt niemand mehr ein, im
Erdgeschoss steigen alle aus. Was gegen die Regeln geht, wird nicht ausgeführt, sondern als Verstoß vermerkt
(fahren mit offener Tür, Tür zu auf jemandem, überladen schließen, über das Haus hinaus).
"""

DT = 0.25
TAKTE = 4
# Sekunden je Etage, je Tür auf oder zu, je Person durch die Tür
TEMPO = 2.0
TUER = 1.0
SCHRITT = 1.0
# so lange steht eine überladene Kabine offen, bis der Letzte wieder aussteigt
UEBERLAST_PAUSE = 2.0
BEFEHLE = ("hoch", "runter", "auf", "zu", "warten")
GEWICHT = 75


class Kabine:
    """Was das Programm von einer Kabine sieht (auch von den anderen)."""

    def __init__(self, etage, richtung, tuer, ziele, drin):
        self.etage = etage
        self.richtung = richtung
        self.tuer = tuer
        self.ziele = ziele
        self.drin = drin

    def __repr__(self):
        return "Kabine(etage=%r, richtung=%r, tuer=%r, ziele=%r, drin=%r)" % (
            self.etage, self.richtung, self.tuer, self.ziele, self.drin)


class Lage:
    """Was das Programm in takt(lage) sieht, für die Kabine, die gerade fragt."""

    def __init__(self, **werte):
        self.__dict__.update(werte)

    def __repr__(self):
        return "Lage(%s)" % ", ".join("%s=%r" % kv for kv in vars(self).items())


class Fahrgast:
    __slots__ = ("id", "von", "nach", "ankunft", "gewicht", "eingestiegen", "angekommen", "abgewiesen")

    def __init__(self, nr, daten):
        self.id = nr
        self.von = daten["von"]
        self.nach = daten["nach"]
        self.ankunft = daten["t"]
        self.gewicht = daten.get("gewicht", GEWICHT)
        self.eingestiegen = None
        self.angekommen = None
        # Name der Kabine, aus der er wegen Überlast wieder ausstieg, bis sie weiterfährt
        self.abgewiesen = None

    @property
    def richtung(self):
        return 1 if self.nach > self.von else -1


class Aufzug:
    def __init__(self, name, etage):
        self.name = name
        self.pos = float(etage)
        self.etage = etage
        self.richtung = 0
        # "zu", "oeffnet", "offen", "schliesst"
        self.tuer = "zu"
        self.tuer_anteil = 0.0
        self.befehl = None
        self.rest = 0.0
        self.fahrgaeste = []
        self.ziele = set()
        # wer gerade durch die Tür geht: (Fahrgast, +1 rein oder -1 raus, Rest in Sekunden)
        self.laeufer = None
        # Sekunden, die die Tür offen stand, ohne dass jemand kam oder ging
        self.leer_offen = 0.0
        # wann die Kabine an ihrer Etage ankam
        self.da_seit = 0.0
        # seit wann sie überladen ist (bei offener Tür)
        self.ueberlast_seit = None


class Welt:
    def __init__(self, anlage, ablauf, aufzeichnen=False):
        self.etagen = anlage["etagen"]
        self.plaetze = anlage["plaetze"]
        self.last = anlage["last"]
        self.aufzuege = [Aufzug(name, anlage["start"]) for name in anlage["aufzuege"]]
        self.dauer = ablauf["dauer"]
        self.ankuenfte = sorted(ablauf["fahrgaeste"], key=lambda f: (f["t"], f["von"], f["nach"]))
        self.feuer_ab = ablauf.get("feuer")
        self.naechste = 0
        self.wartend = []
        self.alle = []
        self.takt = 0
        self.aufzeichnen = aufzeichnen
        self.bilder = []
        # Ereignisse mit Zeit: Verstöße, Türen, Fahrten, Ankünfte, Wenden (für Regeln, Diagramm und Klänge)
        self.ereignisse = []
        # je Sekunde: wartende Fahrgäste und je Kabine Etage und Zahl der Ziele
        self.protokoll = []

    @property
    def zeit(self):
        return self.takt * DT

    def _aufzug(self, name):
        for a in self.aufzuege:
            if a.name == name:
                return a
        return self.aufzuege[0]

    def feuer(self):
        return self.feuer_ab is not None and self.zeit >= self.feuer_ab

    # --- Sensoren ---------------------------------------------------------------

    def rufe(self):
        """Gedrückte Rufe. Wer wegen Überlast wieder ausstieg, drückt erst wieder, wenn die Kabine weiterfährt."""
        rufe = {1: set(), -1: set()}
        for f in self.wartend:
            if f.abgewiesen is None:
                rufe[f.richtung].add(f.von)
        return rufe

    def _gewicht(self, a):
        return sum(f.gewicht for f in a.fahrgaeste)

    def _kabine(self, a):
        return Kabine(a.etage, a.richtung, "offen" if a.tuer == "offen" else "zu", set(a.ziele), len(a.fahrgaeste))

    def lage(self, wer=None):
        a = self._aufzug(wer)
        wartend = {}
        for f in self.wartend:
            if f.abgewiesen is None:
                wartend[f.von] = wartend.get(f.von, 0) + 1
        return Lage(
            sekunde=int(self.zeit),
            aufzug=a.name,
            etage=a.etage,
            etagen=self.etagen,
            richtung=a.richtung,
            tuer="offen" if a.tuer == "offen" else "zu",
            ziele=set(a.ziele),
            rufe=self.rufe(),
            wartend=wartend,
            drin=len(a.fahrgaeste),
            voll=len(a.fahrgaeste) >= self.plaetze,
            lichtschranke=a.laeufer is not None,
            ueberlast=self._gewicht(a) > self.last,
            feuer=self.feuer(),
            aufzuege={b.name: self._kabine(b) for b in self.aufzuege},
        )

    # --- Steuerung: Schnittstelle aller Welten (sandbox_lauf) -------------------

    def laeuft(self):
        return self.takt < self.dauer * TAKTE

    def bereit(self):
        return [a.name for a in self.aufzuege if a.befehl is None]

    def befehl_pruefen(self, wert):
        if wert not in BEFEHLE:
            return None, "takt() muss einen Befehl liefern: %s, nicht %r" % (
                ", ".join('"%s"' % b for b in BEFEHLE), wert)
        return wert, None

    def befehl(self, wer, befehl):
        a = self._aufzug(wer)
        if befehl in ("hoch", "runter") and self._fahren(a, 1 if befehl == "hoch" else -1):
            return
        if befehl == "auf" and a.tuer == "zu":
            self._ereignis("auf", a)
            a.tuer, a.befehl, a.rest = "oeffnet", "auf", TUER
            return
        if befehl == "zu" and a.tuer == "offen" and self._schliessen(a):
            return
        a.befehl, a.rest = "warten", 1.0

    def _fahren(self, a, schritt):
        if a.tuer != "zu":
            self._ereignis("verstoss", a, text="will fahren, aber die Tür ist offen", grund="offen_fahren")
            return False
        if not 0 <= a.etage + schritt < self.etagen:
            self._ereignis("verstoss", a, text="will %s, da ist keine Etage mehr" % ("hoch" if schritt > 0 else "runter"),
                           grund="haus")
            return False
        if a.richtung and schritt != a.richtung:
            # wer schon vor der Ankunft hier in der alten Richtung ein Ziel hatte oder wartete
            frueher = {f.nach for f in a.fahrgaeste if f.eingestiegen is not None and f.eingestiegen < a.da_seit}
            frueher |= {f.von for f in self.wartend if f.ankunft < a.da_seit and f.abgewiesen is None}
            weiter = sorted(e for e in frueher if (e - a.etage) * a.richtung > 0)
            self._ereignis("wende", a, von=a.richtung, weiter=weiter)
        a.richtung = schritt
        for f in self.wartend:
            if f.abgewiesen == a.name:
                f.abgewiesen = None
        self._ereignis("fahrt", a, nach=a.etage + schritt)
        a.befehl, a.rest = ("hoch" if schritt > 0 else "runter"), TEMPO
        return True

    def _schliessen(self, a):
        if a.laeufer is not None:
            self._ereignis("verstoss", a, text="Tür geht zu, obwohl jemand in der Tür steht: eingeklemmt",
                           grund="einklemmen")
            return False
        if self._gewicht(a) > self.last:
            self._ereignis("verstoss", a, text="Tür geht zu, obwohl die Kabine überladen ist", grund="ueberlast")
            return False
        self._ereignis("zu", a, leer=round(a.leer_offen, 2))
        a.tuer, a.befehl, a.rest = "schliesst", "zu", TUER
        return True

    def _ereignis(self, art, a, **mehr):
        self.ereignisse.append(dict(t=round(self.zeit, 2), art=art, aufzug=a.name, etage=a.etage, **mehr))

    def schritt(self):
        jetzt = self.zeit
        while self.naechste < len(self.ankuenfte) and self.ankuenfte[self.naechste]["t"] <= jetzt + 1e-9:
            f = Fahrgast(len(self.alle), self.ankuenfte[self.naechste])
            self.alle.append(f)
            self.wartend.append(f)
            self.naechste += 1
        if self.aufzeichnen and self.takt % TAKTE == 0:
            self.protokoll.append([len(self.wartend), [[a.etage, len(a.ziele), a.tuer] for a in self.aufzuege]])
        for a in self.aufzuege:
            self._bewegen(a)
            self._umsteigen(a)
        self.takt += 1
        if self.aufzeichnen:
            self.bilder.append([
                round(self.zeit, 2),
                [[round(a.pos, 3), round(a.tuer_anteil, 2), len(a.fahrgaeste)] for a in self.aufzuege],
                [[f.id, f.von, f.richtung] for f in self.wartend],
                [[a.laeufer[0].id, i, a.laeufer[1], round(1 - a.laeufer[2] / SCHRITT, 2)]
                 for i, a in enumerate(self.aufzuege) if a.laeufer],
            ])

    def _bewegen(self, a):
        if a.befehl is None:
            return
        a.rest -= DT
        fertig = a.rest <= 1e-9
        if a.befehl in ("hoch", "runter"):
            schritt = 1 if a.befehl == "hoch" else -1
            a.pos = a.etage + schritt * (1 - max(0.0, a.rest) / TEMPO)
            if fertig:
                a.etage += schritt
                a.pos = float(a.etage)
                a.da_seit = self.zeit
                mit = [f.id for f in self.wartend if f.von == a.etage and f.richtung == a.richtung]
                self._ereignis("ankunft", a, wartend=mit, voll=len(a.fahrgaeste) >= self.plaetze)
        elif a.befehl == "auf":
            a.tuer_anteil = 1 - max(0.0, a.rest) / TUER
            if fertig:
                a.tuer, a.tuer_anteil, a.leer_offen = "offen", 1.0, 0.0
                self._ereignis("offen", a)
        elif a.befehl == "zu":
            a.tuer_anteil = max(0.0, a.rest) / TUER
            if fertig:
                a.tuer, a.tuer_anteil = "zu", 0.0
        if fertig:
            a.befehl = None

    def _umsteigen(self, a):
        """Bei offener Tür: erst aussteigen, dann einsteigen, je einer nach dem anderen."""
        if a.tuer != "offen":
            return
        if a.laeufer is not None:
            self._durch_die_tuer(a)
            if a.laeufer is not None:
                return
            # ohne Lücke zum Nächsten: die Lichtschranke bleibt belegt, solange jemand kommt oder geht
        # bei Feueralarm steigen im Erdgeschoss alle aus
        raus = [f for f in a.fahrgaeste if f.nach == a.etage or (self.feuer() and a.etage == 0)]
        if not raus and self._gewicht(a) > self.last:
            # zu schwer: erst wird verhandelt, dann steigt aus, wer zuletzt kam
            if a.ueberlast_seit is None:
                a.ueberlast_seit = self.zeit
            if self.zeit - a.ueberlast_seit < UEBERLAST_PAUSE - 1e-9:
                return
            raus = a.fahrgaeste[-1:]
        a.ueberlast_seit = None
        if raus:
            f = raus[0]
            a.fahrgaeste.remove(f)
            a.ziele = {g.nach for g in a.fahrgaeste}
            a.laeufer = (f, -1, SCHRITT)
            a.leer_offen = 0.0
            return
        if len(a.fahrgaeste) < self.plaetze and not self.feuer():
            for f in self.wartend:
                if f.von == a.etage and f.abgewiesen != a.name:
                    self.wartend.remove(f)
                    if f.eingestiegen is None:
                        f.eingestiegen = round(self.zeit, 2)
                    a.laeufer = (f, 1, SCHRITT)
                    a.leer_offen = 0.0
                    return
        a.leer_offen += DT

    def _durch_die_tuer(self, a):
        f, weg, rest = a.laeufer
        rest -= DT
        if rest > 1e-9:
            a.laeufer = (f, weg, rest)
            return
        a.laeufer = None
        if weg > 0:
            a.fahrgaeste.append(f)
            a.ziele.add(f.nach)
        elif f.nach == a.etage:
            f.angekommen = round(self.zeit, 2)
        elif not self.feuer():
            f.eingestiegen = None
            f.abgewiesen = a.name
            self.wartend.append(f)

    # --- Auswertung -------------------------------------------------------------

    def bilanz(self):
        """Je Fahrgast Wartezeit bis zum Einsteigen und ob er ankam; wer noch wartet, wartet bis zum Ende."""
        ende = self.zeit
        return [{"id": f.id, "von": f.von, "nach": f.nach, "ankunft": f.ankunft,
                 "warten": round((f.eingestiegen if f.eingestiegen is not None else ende) - f.ankunft, 2),
                 "angekommen": f.angekommen} for f in self.alle]
