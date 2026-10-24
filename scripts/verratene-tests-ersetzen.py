"""Ersetzt versteckte Tests, die der Aufgabentext samt Erwartung verrät.

Ablauf:
1. `--dossier akte.json` schreibt je betroffener Aufgabe Funktion, Text,
   Tests, die verratenen Nummern und die Merkmale, die ein Ersatz behalten
   muss (Null, negative Zahl, leerer Behälter, Großbuchstaben ...).
2. Daraus entstehen Vorschläge {aufgaben_id: [{"nummer": i, "input": [...]}]}.
3. `--vorschlaege vorschlaege.json` prüft jeden Vorschlag und trägt ihn ein:
   - alle Musterlösungen laufen in der Sandbox; die Erwartung ist ihr
     gemeinsames Ergebnis (weichen sie ab oder scheitern, fällt er weg)
   - gleiche Zahl und Art der Argumente, Merkmale des alten Tests erhalten
   - gleicht keinem vorhandenen Test und ist selbst nicht verraten
   Angenommene Werte ersetzen den alten Test; die Revision steigt einmal.
   Abgelehnte stehen mit Grund im Bericht.

Aufruf (aus backend/):
    .venv/bin/python ../scripts/verratene-tests-ersetzen.py --dossier akte.json
    .venv/bin/python ../scripts/verratene-tests-ersetzen.py --vorschlaege vorschlaege.json [--trocken]
"""

import argparse
import json
import math
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

WURZEL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WURZEL / "backend" / "src"))

from codeschmiede.aufgaben.lecksuche import aufgabentext, ist_verraten, verratene_tests  # noqa: E402
from codeschmiede.aufgaben.loader import AufgabenLoader  # noqa: E402
from codeschmiede.models.aufgabe import Aufgabe, TestFall  # noqa: E402
from codeschmiede.pruefung.kodierung import Unbekannt, gleich  # noqa: E402
from codeschmiede.pruefung.testlauf import fuehre_aus  # noqa: E402
from codeschmiede.sandbox.docker_runner import DockerRunner  # noqa: E402
from codeschmiede.sandbox.result import RunLimits  # noqa: E402


ausgabe_sperre = threading.Lock()


def melde(text: str) -> None:
    with ausgabe_sperre:
        print(text, flush=True)


def schlicht(wert: Any) -> bool:
    """Lässt sich der Wert als Erwartung in YAML schreiben und wiederlesen?"""
    if wert is None or isinstance(wert, (bool, int, str)):
        return True
    if isinstance(wert, float):
        return math.isfinite(wert)
    if isinstance(wert, list):
        return all(schlicht(x) for x in wert)
    if isinstance(wert, dict):
        return all(isinstance(k, str) and schlicht(v) for k, v in wert.items())
    return False


def merkmale(wert: Any) -> set[str]:
    """Sonderfälle, die ein Test prüft; der Ersatz muss sie behalten."""
    gefunden: set[str] = set()

    def sieh(w: Any) -> None:
        if isinstance(w, bool) or w is None:
            return
        if isinstance(w, (int, float)):
            if w == 0:
                gefunden.add("eine Null")
            if w < 0:
                gefunden.add("eine negative Zahl")
            if isinstance(w, float) and not w.is_integer():
                gefunden.add("eine Kommazahl")
        elif isinstance(w, str):
            if w == "":
                gefunden.add("einen leeren Text")
            if any(c.isupper() for c in w):
                gefunden.add("Großbuchstaben")
            if " " in w:
                gefunden.add("Leerzeichen")
            if any(c.isdigit() for c in w):
                gefunden.add("Ziffern im Text")
            if any(not c.isalnum() and not c.isspace() for c in w):
                gefunden.add("Satz- oder Sonderzeichen")
            if any(ord(c) > 127 for c in w):
                gefunden.add("Umlaute oder andere Nicht-ASCII-Zeichen")
        elif isinstance(w, (list, dict)):
            if not w:
                gefunden.add("einen leeren Behälter")
            for x in (w.values() if isinstance(w, dict) else w):
                sieh(x)

    sieh(wert)
    return gefunden


def gleiche_art(a: Any, b: Any) -> bool:
    if isinstance(a, bool) or isinstance(b, bool):
        return isinstance(a, bool) and isinstance(b, bool)
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return True
    return type(a) is type(b)


class DateiQuelle:
    """Vorschläge aus einer Datei; Absagen stehen im Bericht."""

    def __init__(self, pfad: Path) -> None:
        self.vorschlaege: dict[str, list[dict[str, Any]]] = json.loads(pfad.read_text(encoding="utf-8"))

    def vorschlaege_fuer(self, aufgabe: Aufgabe) -> list[dict[str, Any]]:
        return self.vorschlaege.get(aufgabe.id, [])



def berechne(runner: DockerRunner, aufgabe: Aufgabe, loesungen: list[str], eingaben: list[list[Any]]) -> list[tuple[bool, Any, str]]:
    """Je Eingabe: (gültig, Erwartung, Grund)."""
    laeufe = [
        fuehre_aus(runner, "python", code, aufgabe.funktion, eingaben, RunLimits(timeout_sekunden=aufgabe.zeitlimit_sekunden))
        for code in loesungen
    ]
    ergebnis = []
    for j in range(len(eingaben)):
        aufrufe = [l.aufrufe[j] if l.aufrufe else None for l in laeufe]
        if any(a is None or not a.ok for a in aufrufe):
            fehler = next((a.fehler for a in aufrufe if a and not a.ok), "Lauf abgebrochen")
            ergebnis.append((False, None, f"Musterlösung scheitert: {fehler}"))
            continue
        werte = [a.wert for a in aufrufe]
        if any(isinstance(w, Unbekannt) for w in werte) or not all(gleich(w, werte[0]) for w in werte):
            ergebnis.append((False, None, "Musterlösungen liefern verschiedene Ergebnisse"))
        elif not schlicht(werte[0]):
            ergebnis.append((False, None, "Ergebnis ist kein schlichter Wert (Tupel, Menge o. ä.)"))
        else:
            ergebnis.append((True, werte[0], ""))
    return ergebnis


def ersetze_in_datei(datei: Path, ersatz: dict[int, TestFall]) -> None:
    text = datei.read_text(encoding="utf-8")
    kopf_ende = text.index("\n---", 3)
    zeilen = text[:kopf_ende].split("\n")
    start = zeilen.index("tests_versteckt:")
    ende = next((k for k in range(start + 1, len(zeilen)) if zeilen[k] and not zeilen[k][0].isspace()), len(zeilen))
    punkte = [k for k in range(start + 1, ende) if re.match(r"^\s*- ", zeilen[k])]
    einrueck = min(len(zeilen[k]) - len(zeilen[k].lstrip()) for k in punkte)
    punkte = [k for k in punkte if len(zeilen[k]) - len(zeilen[k].lstrip()) == einrueck]
    for i in sorted(ersatz, reverse=True):
        von = punkte[i]
        bis = punkte[i + 1] if i + 1 < len(punkte) else ende
        neu = [
            f"{' ' * einrueck}- input: {json.dumps(ersatz[i].input, ensure_ascii=False)}",
            f"{' ' * einrueck}  expected: {json.dumps(ersatz[i].expected, ensure_ascii=False)}",
        ]
        zeilen[von:bis] = neu
    kopf = "\n".join(zeilen)
    kopf = re.sub(r"^revision: (\d+)$", lambda m: f"revision: {int(m.group(1)) + 1}", kopf, count=1, flags=re.M)
    datei.write_text(kopf + text[kopf_ende:], encoding="utf-8")


def bearbeite(aufgabe: Aufgabe, quelle: DateiQuelle, runner: DockerRunner, loader: AufgabenLoader, trocken: bool) -> tuple[int, list[str]]:
    offen = verratene_tests(aufgabe)
    loesungen = [m["code"] for m in AufgabenLoader.musterloesungen_neben(aufgabe.dateipfad.parent)]
    if aufgabe.sprache != "python" or not aufgabe.funktion or not loesungen:
        return 0, [f"{aufgabe.id}: übersprungen (keine Python-Funktion mit Musterlösung)"]
    text = aufgabentext(aufgabe)
    vorhanden = [json.dumps(t.input, sort_keys=True) for t in aufgabe.tests_sichtbar + aufgabe.tests_versteckt]
    angenommen: dict[int, TestFall] = {}
    absagen: dict[int, str] = {}
    kandidaten: list[tuple[int, list[Any]]] = []
    for v in quelle.vorschlaege_fuer(aufgabe):
        i, eingabe = v["nummer"], v["input"]
        if i not in offen or not isinstance(eingabe, list):
            continue
        alt = aufgabe.tests_versteckt[i].input
        if len(eingabe) != len(alt) or not all(gleiche_art(a, b) for a, b in zip(eingabe, alt)):
            absagen[i] = f"input {json.dumps(eingabe, ensure_ascii=False)}: Anzahl oder Art der Argumente passt nicht"
        elif fehlend := merkmale(alt) - merkmale(eingabe):
            absagen[i] = (
                f"input {json.dumps(eingabe, ensure_ascii=False)}: der alte Test enthielt "
                f"{', '.join(sorted(fehlend))}; der Ersatz muss das ebenfalls enthalten"
            )
        elif json.dumps(eingabe, sort_keys=True) in vorhanden:
            absagen[i] = f"input {json.dumps(eingabe, ensure_ascii=False)}: gleicht einem vorhandenen Test"
        else:
            kandidaten.append((i, eingabe))
            vorhanden.append(json.dumps(eingabe, sort_keys=True))
    if kandidaten:
        for (i, eingabe), (gueltig, erwartung, grund) in zip(
            kandidaten, berechne(runner, aufgabe, loesungen, [k[1] for k in kandidaten])
        ):
            test = TestFall(input=eingabe, expected=erwartung)
            if not gueltig:
                absagen[i] = f"input {json.dumps(eingabe, ensure_ascii=False)}: {grund}"
            elif ist_verraten(test, text):
                absagen[i] = f"input {json.dumps(eingabe, ensure_ascii=False)}: steht samt Ergebnis im Text"
            else:
                angenommen[i] = test
    if angenommen and not trocken:
        ersetze_in_datei(aufgabe.dateipfad, angenommen)
        neu = loader.lade_aufgabe(aufgabe.dateipfad)
        for i, t in angenommen.items():
            assert neu.tests_versteckt[i].input == t.input and neu.tests_versteckt[i].expected == t.expected, aufgabe.id
    probleme = [f"{aufgabe.id} Nr. {i}: {absagen.get(i, 'kein Vorschlag')}" for i in offen if i not in angenommen]
    melde(f"{aufgabe.id}: {len(angenommen)} von {len(offen)} ersetzt")
    return len(angenommen), probleme


def dossier(aufgaben: list[Aufgabe]) -> list[dict[str, Any]]:
    akte = []
    for a in aufgaben:
        offen = verratene_tests(a)
        akte.append({
            "id": a.id,
            "funktion": a.funktion,
            "text": a.beschreibung_md,
            "sichtbar": [{"input": t.input, "expected": t.expected} for t in a.tests_sichtbar],
            "versteckt": [
                {"nummer": i, "input": t.input, "expected": t.expected, "verraten": i in offen,
                 "muss_enthalten": sorted(merkmale(t.input)) if i in offen else []}
                for i, t in enumerate(a.tests_versteckt)
            ],
        })
    return akte


def main() -> None:
    teil = argparse.ArgumentParser()
    teil.add_argument("--nur", nargs="*", default=None)
    teil.add_argument("--trocken", action="store_true")
    teil.add_argument("--parallel", type=int, default=2)
    teil.add_argument("--dossier", type=Path)
    teil.add_argument("--vorschlaege", type=Path)
    args = teil.parse_args()

    loader = AufgabenLoader(WURZEL / "aufgaben")
    aufgaben = [a for a in loader.lade_alle_aufgaben() if verratene_tests(a) and (args.nur is None or a.id in args.nur)]
    runner = DockerRunner({"python": "codeschmiede-sandbox:python"}, startzeit_sekunden=60)
    if args.dossier:
        args.dossier.write_text(json.dumps(dossier(aufgaben), ensure_ascii=False, indent=1), encoding="utf-8")
        melde(f"Akte mit {len(aufgaben)} Aufgaben geschrieben: {args.dossier}")
        return
    if not args.vorschlaege:
        teil.error("--dossier oder --vorschlaege angeben")
    quelle = DateiQuelle(args.vorschlaege)
    melde(f"{len(aufgaben)} Aufgaben mit verratenen Tests")
    with ThreadPoolExecutor(max_workers=args.parallel) as pool:
        ergebnisse = list(pool.map(lambda a: bearbeite(a, quelle, runner, loader, args.trocken), aufgaben))
    ersetzt = sum(e[0] for e in ergebnisse)
    probleme = [p for e in ergebnisse for p in e[1]]
    melde(f"\nErsetzt: {ersetzt}; offen: {len(probleme)}")
    for p in probleme:
        melde(f"  {p}")


if __name__ == "__main__":
    main()
