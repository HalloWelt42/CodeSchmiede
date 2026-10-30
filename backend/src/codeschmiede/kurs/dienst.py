"""Kursdienst: Inhalte, Stand je Kapitel, Antworten prüfen, Beispiele ausführen, Merkblatt.

Der Stand folgt aus den Ereignissen (kurs/fortschritt.py) und den gelösten Aufgaben: ein Kapitel ist fertig, wenn alle
Abschnitte der Einführung fertig und alle Übungen und Projektstücke gelöst sind, übersprungen nach bestandenem
Kurztest. Das erste Kapitel ist offen, jedes weitere nach dem vorigen. Übungen öffnen sich nach der Einführung.
Was die Oberfläche versteckt, erzwingt der Server: Ausführen erst nach der Vorhersage, ein Abschnitt erst nach allen
richtig beantworteten Fragen.
"""

from __future__ import annotations

import hashlib
import re
from collections.abc import Callable
from pathlib import Path

from ..aufgaben.bestandspruefung import Befund
from ..models.aufgabe import Aufgabe
from ..sandbox.result import RunLimits
from ..sandbox.runner import Runner
from ..aufzeichnung import Aufzeichnung, aufzeichnen
from ..steuerung import kv
from .begriffe import erkenne
from .css_lauf import CssLauf
from .einlesen import Kursinhalt, lade
from .fortschritt import KursBeitrag, KursfortschrittRepository, Stand
from .modelle import (Alltag, Augenzwinkern, Auswahlfrage, Beispiel, Diagramm, Einfuehrung, Falle,
                      Fehlerstellenfrage, FrageTeil, Kapitel, KvFormel, KvTeil, Lueckenfrage, Merke, Option,
                      Ordnungsfrage, Text, Vorhersage, Zeichnung)
from .pruefung import pruefe_kurs
from .sql_ablauf import SqlLauf, sql_lauf
from .weiter import Erledigt, kapitel_fertig, offener_schritt
from .sicht import (AbschnittSicht, AlltagSicht, Antwort, AugenzwinkernSicht, BeispielSicht, BildVerweis,
                    BlockSicht, DiagrammSicht, EinfuehrungSicht, FalleSicht, FrageSicht, FrageTeilSicht, KapitelSicht,
                    KursSicht, KurztestSicht, KvFormelSicht, KvSicht, MerkBeispiel, MerkblattSicht, MerkeSicht, TextSicht, UebungSicht, Urteil,
                    VorhersageSicht, ZeichnungSicht)

BILDSATZ = "kurs"
"""Satz des Medienpools, dessen Export die Kurszeichnungen liefert (kurs/bilder/<satz>/<schluessel>.webp)."""
LAUF = RunLimits(timeout_sekunden=10)
VERTIEFUNG_HOECHSTENS = 5
VERTIEFUNG_ARTEN = {"code_schreiben", "sql_abfrage", "sql_aenderung"}
"""Aufgabenarten, aus denen die Vertiefung am Kapitelende kommt."""

Frage = Auswahlfrage | Lueckenfrage | Ordnungsfrage | Fehlerstellenfrage
Lauf = Aufzeichnung | SqlLauf | CssLauf
MIT_ABLAUF = {"python", "sql", "javascript"}
"""Sprachen, deren Beispiele die Codeschmiede in der Sandbox ausführt und abspielt."""
AUSFUEHRBAR = MIT_ABLAUF | {"css"}
"""Sprachen, deren Beispiele sich ausführen lassen; CSS rendert der Browser auf der Bühne."""


class NichtGefunden(LookupError):
    pass


class NichtErlaubt(PermissionError):
    pass


def normalisiert(ausgabe: str) -> str:
    return "\n".join(z.rstrip() for z in ausgabe.rstrip().split("\n"))


def zeilenzahl(ausgabe: str) -> int:
    """Zeilen der Ausgabe (bei SQL: Ergebniszeilen); eine leere Ausgabe hat keine."""
    text = normalisiert(ausgabe)
    return len(text.split("\n")) if text else 0


def vorhersage_stimmt(vergleich: str, antwort: str, ausgabe: str) -> bool:
    """Ob eine Antwort zur echten Ausgabe passt, je nach Vergleich der Vorhersage (siehe Vorhersage.vergleich)."""
    if vergleich == "zeilen":
        zahl = re.search(r"\d+", antwort)
        return zahl is not None and int(zahl.group()) == zeilenzahl(ausgabe)
    if vergleich == "anfang":
        anfang = normalisiert(antwort).split("\n")
        return bool(anfang[0]) and normalisiert(ausgabe).split("\n")[:len(anfang)] == anfang
    return normalisiert(antwort) == normalisiert(ausgabe)


class Kursdienst:
    def __init__(self, wurzel: Path, datensaetze: Path, fortschritt: KursfortschrittRepository, runner: Callable[[], Runner]):
        self.wurzel = wurzel
        self.datensaetze = datensaetze
        """Ordner der SQL-Datensätze (aufgaben/sql/datasets), auf denen SQL-Beispiele laufen."""
        self.fortschritt = fortschritt
        self._runner = runner
        self.inhalt = Kursinhalt()
        self.befunde: list[Befund] = []
        self._vertiefung: dict[str, list[str]] = {}
        self._laeufe: dict[str, Lauf] = {}

    # ---------- Einlesen ----------

    def neu_einlesen(self, aufgaben: dict[str, Aufgabe], musterloesungen: Callable[[str], list[dict[str, str]]]) -> None:
        self.inhalt = lade(self.wurzel)
        self.befunde = pruefe_kurs(self.inhalt, aufgaben, musterloesungen, self.wurzel, self.datensaetze)
        self._vertiefung = self._vertiefung_suchen(aufgaben, musterloesungen)
        self._laeufe.clear()

    def _vertiefung_suchen(self, aufgaben: dict[str, Aufgabe], musterloesungen: Callable[[str], list[dict[str, str]]]) -> dict[str, list[str]]:
        """Je Kapitel Aufgaben aus dem Bestand, die nur Eingeführtes brauchen und das Neue des Kapitels üben."""
        im_kurs = {aid for k in self.inhalt.kurse.values() for kap in k.kapitel() for aid in (*kap.uebungen, *kap.projekt)}
        ergebnis: dict[str, list[str]] = {}
        for sprache, kurs in self.inhalt.kurse.items():
            katalog = self.inhalt.begriffe.get(sprache)
            if katalog is None:
                continue
            benutzt: dict[str, set[str]] = {}
            for a in aufgaben.values():
                if a.sprache != sprache or a.id in im_kurs or a.task_type not in VERTIEFUNG_ARTEN:
                    continue
                loesungen = musterloesungen(a.id)
                erkannt = [erkenne(katalog, m["code"]) for m in loesungen[:1]]
                if erkannt and erkannt[0] is not None:
                    benutzt[a.id] = erkannt[0]
            eingefuehrt: set[str] = set()
            for kap in kurs.kapitel():
                e = self.inhalt.einfuehrungen.get(kap.einfuehrung)
                if e is None:
                    continue
                neu = set(e.kopf.fuehrt_ein)
                eingefuehrt |= neu
                passend = sorted((aufgaben[aid].schwierigkeit_score, aid) for aid, b in benutzt.items() if b <= eingefuehrt and b & neu)
                ergebnis[e.id] = [aid for _, aid in passend[:VERTIEFUNG_HOECHSTENS]]
        return ergebnis

    # ---------- Hilfen ----------

    def _einfuehrung(self, eid: str) -> Einfuehrung:
        e = self.inhalt.einfuehrungen.get(eid)
        if e is None:
            raise NichtGefunden(f"Einführung {eid} gibt es nicht")
        return e

    def _kapitelnummer(self, eid: str) -> tuple[str, int, Kapitel] | None:
        for sprache, kurs in self.inhalt.kurse.items():
            for nr, kap in enumerate(kurs.kapitel(), 1):
                if kap.einfuehrung == eid:
                    return sprache, nr, kap
        return None

    def bild(self, e: Einfuehrung, schluessel: str | None) -> BildVerweis | None:
        if not schluessel:
            return None
        auftrag = next((b for b in e.kopf.bilder if b.schluessel == schluessel), None)
        datei = self.wurzel / "bilder" / BILDSATZ / f"{schluessel}.webp"
        return BildVerweis(schluessel=schluessel, url=f"/api/kurs/bilder/{schluessel}.webp" if datei.exists() else None,
                           motiv=auftrag.motiv if auftrag else "")

    def bilddatei(self, schluessel: str) -> Path | None:
        datei = self.wurzel / "bilder" / BILDSATZ / f"{schluessel}.webp"
        return datei if datei.is_file() and datei.parent == self.wurzel / "bilder" / BILDSATZ else None

    @staticmethod
    def _zeichnung_url(e: Einfuehrung, name: str) -> str:
        return f"/api/kurs/zeichnungen/{e.id}/{name}.svg"

    def zeichnungsdatei(self, eid: str, name: str) -> Path | None:
        e = self.inhalt.einfuehrungen.get(eid)
        if e is None or not name.replace("-", "").isalnum():
            return None
        datei = self.wurzel / e.pfad / "zeichnungen" / f"{name}.svg"
        return datei if datei.is_file() else None

    def diagrammdatei(self, pruefsumme: str) -> Path | None:
        if not pruefsumme.isalnum():
            return None
        datei = self.wurzel / "diagramme" / f"{pruefsumme}.svg"
        return datei if datei.is_file() else None

    def _karte(self, e: Einfuehrung) -> BildVerweis | None:
        karte = next((b for b in e.kopf.bilder if b.art == "sammelkarte"), None)
        return self.bild(e, karte.schluessel) if karte else None

    # ---------- Übersicht ----------

    def erledigt(self, geloest: set[str]) -> Erledigt:
        """Erledigtes für die Regel in weiter.py: gelöste Aufgaben, fertige Einführungen, per Kurztest Übersprungenes."""
        stand = Stand(self.fortschritt.alle())
        einfuehrungen = self.inhalt.einfuehrungen.values()
        return Erledigt(
            aufgaben=frozenset(geloest),
            einfuehrungen=frozenset(e.id for e in einfuehrungen
                                    if {a.nummer for a in e.abschnitte} <= stand.abschnitte_fertig(e.id)),
            uebersprungen=frozenset(e.id for e in einfuehrungen if stand.kurztest_bestanden(e.id)),
        )

    def uebersicht(self, aufgaben: dict[str, Aufgabe], geloest: set[str]) -> list[KursSicht]:
        stand = Stand(self.fortschritt.alle())
        erledigt = self.erledigt(geloest)
        kurse = []
        for sprache, kurs in self.inhalt.kurse.items():
            vorige_erledigt = True
            erstes_offen = True
            bloecke = []
            nr = 0
            for block in kurs.bloecke:
                kapitel = []
                for kap in block.kapitel:
                    nr += 1
                    e = self.inhalt.einfuehrungen.get(kap.einfuehrung)
                    if e is None:
                        continue
                    sicht = self._kapitel(nr, kap, e, stand, erledigt, aufgaben, vorige_erledigt, erstes_offen)
                    if sicht.stand in ("aktuell", "offen"):
                        erstes_offen = False
                    vorige_erledigt = sicht.stand in ("fertig", "uebersprungen")
                    kapitel.append(sicht)
                bloecke.append(BlockSicht(titel=block.titel, kapitel=kapitel))
            kurse.append(KursSicht(sprache=sprache, titel=kurs.titel, bloecke=bloecke))
        return kurse

    def _kapitel(self, nr: int, kap: Kapitel, e: Einfuehrung, stand: Stand, erledigt: Erledigt, aufgaben: dict[str, Aufgabe],
                 vorige_erledigt: bool, erstes_offen: bool) -> KapitelSicht:
        def uebung(aid: str) -> UebungSicht:
            a = aufgaben.get(aid)
            return UebungSicht(id=aid, titel=a.titel if a else aid, geloest=aid in erledigt.aufgaben)

        fertig_abschnitte = stand.abschnitte_fertig(e.id) & {a.nummer for a in e.abschnitte}
        einfuehrung_fertig = e.id in erledigt.einfuehrungen
        if kapitel_fertig(kap, erledigt):
            zustand = "fertig"
        elif e.id in erledigt.uebersprungen:
            zustand = "uebersprungen"
        elif not vorige_erledigt:
            zustand = "zu"
        else:
            zustand = "aktuell" if erstes_offen else "offen"
        return KapitelSicht(
            nr=nr, einfuehrung=e.id, titel=e.kopf.titel, kurz=e.kopf.kurz, lernziele=e.kopf.lernziele, karte=e.kopf.karte,
            bild=self._karte(e), stand=zustand, abschnitte=len(e.abschnitte), abschnitte_fertig=len(fertig_abschnitte),
            uebungen=[uebung(a) for a in kap.uebungen], projekt=[uebung(a) for a in kap.projekt],
            uebungen_offen=einfuehrung_fertig or zustand in ("fertig", "uebersprungen"),
            kurztest=e.id in self.inhalt.kurztests,
            vertiefung=[uebung(a) for a in self._vertiefung.get(e.id, [])],
            offen=offener_schritt(kap, erledigt) if zustand != "zu" else None,
        )

    def beitrag(self, aufgaben: dict[str, Aufgabe], geloest: set[str]) -> KursBeitrag:
        """Für Stufe, Serie und Erfolge: fertige Abschnitte (je einmal), geschaffte Kapitel, Tage mit Kursarbeit."""
        ereignisse = self.fortschritt.alle()
        abschnitte = {(e.einfuehrung, e.element) for e in ereignisse if e.art == "abschnitt"}
        kapitel = sum(1 for k in self.uebersicht(aufgaben, geloest) for b in k.bloecke for x in b.kapitel
                      if x.stand in ("fertig", "uebersprungen"))
        tage = frozenset(e.tag for e in ereignisse if e.art in ("abschnitt", "kurztest") or (e.art in ("frage", "kurztest_frage") and e.richtig))
        return KursBeitrag(abschnitte=len(abschnitte), kapitel=kapitel, tage=tage)

    def pruefe_offen(self, eid: str, aufgaben: dict[str, Aufgabe], geloest: set[str]) -> None:
        """Ein Kapitel, das noch zu ist, lässt sich nur per Kurztest betreten; die Oberfläche versteckt es, der Server
        erzwingt es."""
        for kurs in self.uebersicht(aufgaben, geloest):
            for block in kurs.bloecke:
                for k in block.kapitel:
                    if k.einfuehrung == eid and k.stand == "zu":
                        raise NichtErlaubt(f"Kapitel {k.nr} ist noch zu; es öffnet sich nach Kapitel {k.nr - 1} oder per Kurztest")

    # ---------- Einführung ----------

    def einfuehrung(self, eid: str) -> EinfuehrungSicht:
        e = self._einfuehrung(eid)
        stand = Stand(self.fortschritt.alle())
        fertig = stand.abschnitte_fertig(eid)
        abschnitte = [AbschnittSicht(nummer=a.nummer, titel=a.titel, teile=[self._teil(e, t, stand) for t in a.teile],
                                     fertig=a.nummer in fertig) for a in e.abschnitte]
        kapitel = self._kapitelnummer(eid)
        return EinfuehrungSicht(id=e.id, sprache=e.kopf.sprache, titel=e.kopf.titel, kurz=e.kopf.kurz, lernziele=e.kopf.lernziele,
                                karte=e.kopf.karte, kapitel=kapitel[1] if kapitel else None, datensatz=e.kopf.datensatz,
                                abschnitte=abschnitte)

    @staticmethod
    def _kv_formel(t: KvTeil, f: KvFormel) -> KvFormelSicht:
        plan, bausteine, _ = kv.schaltplan(kv.lies(f"f = {f.formel}", t.eingaenge, ["f"]), t.eingaenge, ["f"])
        return KvFormelSicht(titel=f.titel, formel=f.formel, bausteine=bausteine, plan=plan)

    def _teil(self, e: Einfuehrung, t, stand: Stand):
        if isinstance(t, Text):
            return TextSicht(markdown=t.markdown)
        if isinstance(t, Alltag):
            return AlltagSicht(text=t.text, zeichnung=self._zeichnung_url(e, t.zeichnung) if t.zeichnung else None)
        if isinstance(t, Merke):
            return MerkeSicht(text=t.text)
        if isinstance(t, Falle):
            return FalleSicht(titel=t.titel, text=t.text)
        if isinstance(t, Augenzwinkern):
            return AugenzwinkernSicht(text=t.text)
        if isinstance(t, Zeichnung):
            return ZeichnungSicht(url=self._zeichnung_url(e, t.datei), unterschrift=t.unterschrift)
        if isinstance(t, Diagramm):
            datei = self.diagrammdatei(t.pruefsumme)
            return DiagrammSicht(url=f"/api/kurs/diagramme/{t.pruefsumme}.svg" if datei else None, titel=t.titel)
        if isinstance(t, Beispiel):
            v = t.vorhersage
            return BeispielSicht(id=t.id, code=t.code, html=t.html, eingabe=t.eingabe, ablauf=t.ablauf and e.kopf.sprache in MIT_ABLAUF, vorhersage=None if v is None else VorhersageSicht(
                art=v.art, frage=v.frage, optionen=[o.text for o in v.optionen] or None,
                beantwortet=stand.beantwortet("vorhersage", e.id, t.id), richtig=stand.richtig("vorhersage", e.id, t.id)))
        if isinstance(t, KvTeil):
            return KvSicht(id=t.id, eingaenge=t.eingaenge, werte=t.werte, start=t.start, regler=t.regler, plan=t.plan,
                           formeln=[self._kv_formel(t, f) for f in t.formeln])
        if isinstance(t, FrageTeil):
            return FrageTeilSicht(frage=self.frage_sicht(t.frage, stand.beantwortet("frage", e.id, t.frage.id),
                                                         stand.richtig("frage", e.id, t.frage.id)))
        raise TypeError(type(t))

    @staticmethod
    def frage_sicht(f: Frage, beantwortet: bool, richtig: bool) -> FrageSicht:
        basis = {"id": f.id, "frageart": f.frageart, "text": f.text, "beantwortet": beantwortet, "richtig": richtig}
        if isinstance(f, Auswahlfrage):
            return FrageSicht(**basis, code=f.code, optionen=[o.text for o in f.optionen], als_code=f.als_code,
                              mehrere=sum(o.richtig for o in f.optionen) > 1)
        if isinstance(f, Lueckenfrage):
            return FrageSicht(**basis, code=f.code, luecken=len(f.antworten))
        if isinstance(f, Ordnungsfrage):
            return FrageSicht(**basis, zeilen=f.gemischt())
        return FrageSicht(**basis, code=f.code)

    # ---------- Antworten ----------

    @staticmethod
    def beurteile(f: Frage, a: Antwort) -> tuple[bool, str]:
        if isinstance(f, Auswahlfrage):
            return Kursdienst._auswahl(f.optionen, a)
        if isinstance(f, Lueckenfrage):
            gegeben = [x.strip() for x in (a.luecken or [])]
            ok = len(gegeben) == len(f.antworten) and all(g in moeglich for g, moeglich in zip(gegeben, f.antworten))
            return ok, f.erklaerung if ok else f.hinweis
        if isinstance(f, Ordnungsfrage):
            gemischt = f.gemischt()
            reihe = a.reihenfolge or []
            ok = sorted(reihe) == list(range(len(gemischt))) and [gemischt[i] for i in reihe] == f.zeilen
            return ok, f.erklaerung if ok else f.hinweis
        ok = a.zeile == f.zeile
        return ok, f.erklaerung if ok else f.hinweise.get(a.zeile or 0, f.hinweis)

    @staticmethod
    def _auswahl(optionen: list[Option], a: Antwort) -> tuple[bool, str]:
        wahl = sorted(set(a.wahl or []))
        if not wahl or any(not 0 <= i < len(optionen) for i in wahl):
            return False, "Bitte eine der Antworten wählen."
        ok = wahl == [i for i, o in enumerate(optionen) if o.richtig]
        falsch = [optionen[i] for i in wahl if not optionen[i].richtig]
        if ok:
            return True, " ".join(optionen[i].erklaerung for i in wahl)
        return False, falsch[0].erklaerung if falsch else "Da fehlt noch eine richtige Antwort."

    def antworten(self, eid: str, a: Antwort) -> Urteil:
        e = self._einfuehrung(eid)
        for abschnitt in e.abschnitte:
            for t in abschnitt.teile:
                if isinstance(t, FrageTeil) and t.frage.id == a.element:
                    ok, text = self.beurteile(t.frage, a)
                    self.fortschritt.eintragen("frage", eid, a.element, ok)
                    stand = Stand(self.fortschritt.alle())
                    bereit = all(stand.richtig("frage", eid, f.id) for f in abschnitt.fragen())
                    return Urteil(richtig=ok, erklaerung=text, abschnitt_bereit=bereit)
                if isinstance(t, Beispiel) and t.id == a.element and t.vorhersage is not None:
                    ok, text = self._vorhersage(e, t, t.vorhersage, a)
                    self.fortschritt.eintragen("vorhersage", eid, a.element, ok)
                    return Urteil(richtig=ok, erklaerung=text)
        raise NichtGefunden(f"{a.element} ist keine Frage und keine Vorhersage in {eid}")

    def _vorhersage(self, e: Einfuehrung, b: Beispiel, v: Vorhersage, a: Antwort) -> tuple[bool, str]:
        if v.art == "auswahl":
            return self._auswahl(v.optionen, a)
        lauf = self.lauf(e, b)
        if isinstance(lauf, CssLauf):
            raise NichtErlaubt("Vorhersagen zu CSS gehen nur als Auswahl")
        return vorhersage_stimmt(v.vergleich, a.eingetippt or "", lauf.ausgabe), v.erklaerung

    def abschnitt_fertig(self, eid: str, nummer: int) -> None:
        e = self._einfuehrung(eid)
        abschnitt = next((x for x in e.abschnitte if x.nummer == nummer), None)
        if abschnitt is None:
            raise NichtGefunden(f"Abschnitt {nummer} gibt es nicht")
        stand = Stand(self.fortschritt.alle())
        offen = [f.id for f in abschnitt.fragen() if not stand.richtig("frage", eid, f.id)]
        if offen:
            raise NichtErlaubt(f"Erst die Fragen beantworten: {', '.join(offen)}")
        if nummer not in stand.abschnitte_fertig(eid):
            self.fortschritt.eintragen("abschnitt", eid, str(nummer), True)

    # ---------- Beispiele ----------

    def _beispiel(self, e: Einfuehrung, bid: str) -> Beispiel:
        for a in e.abschnitte:
            for b in a.beispiele():
                if b.id == bid:
                    return b
        raise NichtGefunden(f"Beispiel {bid} gibt es nicht")

    def lauf(self, e: Einfuehrung, b: Beispiel, code: str | None = None) -> Lauf:
        """Lauf eines Beispiels: bei Python und JavaScript die Aufzeichnung, bei SQL Ergebnis und Zwischentabellen auf
        dem Datensatz der Einführung, bei CSS Markup und CSS für die Bühne. Das Original wird je Inhalt nur einmal
        gerechnet."""
        if e.kopf.sprache not in AUSFUEHRBAR:
            raise NichtErlaubt(f"Beispiele in {e.kopf.sprache} lassen sich noch nicht ausführen")
        quelltext = b.code if code is None else code
        if e.kopf.sprache == "css":
            return CssLauf(html=b.html or "", css=quelltext)
        schluessel = hashlib.sha256("\0".join([e.kopf.sprache, e.kopf.datensatz or "", quelltext, *b.eingabe]).encode()).hexdigest()
        if code is None and schluessel in self._laeufe:
            return self._laeufe[schluessel]
        ergebnis: Lauf
        if e.kopf.sprache == "sql":
            ergebnis = sql_lauf(self._runner(), self.datensatz_sql(e.kopf.datensatz or ""), quelltext, LAUF)
        else:
            ergebnis = aufzeichnen(self._runner(), quelltext, LAUF, b.eingabe, e.kopf.sprache)
        if code is None and not ergebnis.zeitueberschreitung:
            self._laeufe[schluessel] = ergebnis
        return ergebnis

    def datensatz_sql(self, name: str) -> str:
        datei = self.datensaetze / f"{name}.sql"
        if not datei.is_file():
            raise NichtGefunden(f"Datensatz {name} gibt es nicht")
        return datei.read_text(encoding="utf-8")

    def ausfuehren(self, eid: str, bid: str, code: str | None) -> Lauf:
        e = self._einfuehrung(eid)
        b = self._beispiel(e, bid)
        if b.vorhersage is not None and not Stand(self.fortschritt.alle()).beantwortet("vorhersage", eid, bid):
            raise NichtErlaubt("Erst vorhersagen, dann ausführen")
        return self.lauf(e, b, code if code is not None and code != b.code else None)

    # ---------- Kurztest ----------

    def kurztest(self, eid: str, aufgaben: dict[str, Aufgabe], geloest: set[str]) -> KurztestSicht:
        e = self._einfuehrung(eid)
        test = self.inhalt.kurztests.get(eid)
        if test is None:
            raise NichtGefunden(f"{eid} hat keinen Kurztest")
        stand = Stand(self.fortschritt.alle())
        a = aufgaben.get(test.uebung)
        return KurztestSicht(
            einfuehrung=eid, titel=e.kopf.titel,
            fragen=[self.frage_sicht(f, stand.beantwortet("kurztest_frage", eid, f.id), stand.richtig("kurztest_frage", eid, f.id)) for f in test.fragen],
            uebung=UebungSicht(id=test.uebung, titel=a.titel if a else test.uebung, geloest=test.uebung in geloest),
            bestanden=stand.kurztest_bestanden(eid),
        )

    def kurztest_antworten(self, eid: str, a: Antwort, geloest: set[str]) -> Urteil:
        self._einfuehrung(eid)
        test = self.inhalt.kurztests.get(eid)
        f = next((x for x in test.fragen if x.id == a.element), None) if test else None
        if f is None:
            raise NichtGefunden(f"{a.element} ist keine Frage im Kurztest {eid}")
        ok, text = self.beurteile(f, a)
        self.fortschritt.eintragen("kurztest_frage", eid, f.id, ok)
        self.kurztest_abschliessen(eid, geloest)
        return Urteil(richtig=ok, erklaerung=text)

    def kurztest_abschliessen(self, eid: str, geloest: set[str]) -> bool:
        """Bestanden, wenn jede Frage zuletzt richtig beantwortet und die Übung gelöst ist; wird einmal vermerkt."""
        test = self.inhalt.kurztests.get(eid)
        if test is None:
            return False
        ereignisse = self.fortschritt.alle()
        stand = Stand(ereignisse)
        if stand.kurztest_bestanden(eid):
            return True
        zuletzt = {e.element: e.richtig for e in ereignisse if e.art == "kurztest_frage" and e.einfuehrung == eid}
        if all(zuletzt.get(f.id) for f in test.fragen) and test.uebung in geloest:
            self.fortschritt.eintragen("kurztest", eid, "", True)
            return True
        return False

    # ---------- Merkblatt ----------

    def merkblatt(self, eid: str) -> MerkblattSicht:
        e = self._einfuehrung(eid)
        katalog = self.inhalt.begriffe.get(e.kopf.sprache)
        titel = {b.id: b.titel for b in katalog.begriffe} if katalog else {}
        beispiele = []
        for a in e.abschnitte:
            erstes = next(iter(a.beispiele()), None)
            if erstes is None:
                continue
            ausgabe = None
            if e.kopf.sprache in MIT_ABLAUF:
                try:
                    lauf = self.lauf(e, erstes)
                    ausgabe = lauf.ausgabe if not lauf.fehler else None
                except Exception:  # noqa: BLE001 - ohne Sandbox bleibt das Merkblatt ohne Ausgaben
                    ausgabe = None
            beispiele.append(MerkBeispiel(code=erstes.code, html=erstes.html, ausgabe=ausgabe))
        kapitel = self._kapitelnummer(eid)
        return MerkblattSicht(
            einfuehrung=eid, sprache=e.kopf.sprache, titel=e.kopf.titel, kapitel=kapitel[1] if kapitel else None,
            lernziele=e.kopf.lernziele,
            merke=[t.text for a in e.abschnitte for t in a.teile if isinstance(t, Merke)],
            beispiele=beispiele,
            fallen=[FalleSicht(titel=t.titel, text=t.text) for a in e.abschnitte for t in a.teile if isinstance(t, Falle)],
            begriffe=[titel.get(b, b) for b in e.kopf.fuehrt_ein],
            bild=self._karte(e),
        )
