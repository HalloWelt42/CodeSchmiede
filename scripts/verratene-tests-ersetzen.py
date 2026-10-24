"""Ersetzt versteckte Tests, die der Aufgabentext samt Erwartung verrät.

Ablauf je Aufgabe (nur Python-Aufgaben mit Funktion und Musterlösungen):
1. Die lokale KI (über die Leitstelle) schlägt für jeden verratenen Test
   eine neue Eingabe vor, die dasselbe prüft (gleicher Sonderfall, gleiche
   Art von Werten), aber nicht im Text steht.
2. Alle Musterlösungen laufen mit den Vorschlägen in der Sandbox. Die
   Erwartung ist ihr gemeinsames Ergebnis; weichen sie voneinander ab oder
   scheitern, fällt der Vorschlag weg.
3. Ein Vorschlag gilt nur, wenn er dieselbe Zahl und Art Argumente hat,
   keinem vorhandenen Test gleicht und selbst nicht verraten ist.
4. Angenommene Vorschläge ersetzen den alten Test in der Datei; die
   Revision der Aufgabe steigt einmal.

Aufruf (aus backend/):
    .venv/bin/python ../scripts/verratene-tests-ersetzen.py [--nur ID ...] [--trocken]

Schlüssel der Leitstelle: data/leitstelle-schluessel oder CODESCHMIEDE_LEITSTELLE_SCHLUESSEL,
Adresse: CODESCHMIEDE_LEITSTELLE_URL (Vorgabe http://leitstelle:8530).
"""

import argparse
import json
import math
import os
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

import httpx2

WURZEL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WURZEL / "backend" / "src"))

from codeschmiede.aufgaben.lecksuche import aufgabentext, ist_verraten, verratene_tests  # noqa: E402
from codeschmiede.aufgaben.loader import AufgabenLoader  # noqa: E402
from codeschmiede.models.aufgabe import Aufgabe, TestFall  # noqa: E402
from codeschmiede.pruefung.kodierung import Unbekannt, gleich  # noqa: E402
from codeschmiede.pruefung.testlauf import fuehre_aus  # noqa: E402
from codeschmiede.sandbox.docker_runner import DockerRunner  # noqa: E402
from codeschmiede.sandbox.result import RunLimits  # noqa: E402

RUNDEN = 3
SYSTEM = (
    "Du hilfst beim Pflegen von Programmieraufgaben. Ein versteckter Test steht wörtlich im "
    "Aufgabentext und muss ersetzt werden. Schlage je verratenem Test genau eine neue Eingabe vor, "
    "die dasselbe prüft: denselben Sonderfall (leer, null, negativ, Grenze, Gleichstand, Sonderzeichen "
    "usw.), dieselbe Art und Anzahl Argumente, ähnliche Größe. Die neue Eingabe darf nicht im "
    "Aufgabentext vorkommen und keinem anderen Test gleichen. Halte dich an die Vorbedingungen der "
    "Aufgabe (gültige Monate, positive Zahlen und so weiter). Gib nur Eingaben an, keine Ergebnisse; "
    "die rechnet das System selbst aus. Die Eingabe steht in input_json als JSON-Liste der Argumente, "
    "genau wie im Feld input der Tests. Antworte auf Deutsch mit echten Umlauten."
)
SCHEMA = {
    "type": "object",
    "properties": {
        "ersatz": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "nummer": {"type": "integer"},
                    "zweck": {"type": "string"},
                    # als JSON-Text: ein offenes Schema für beliebige Werte macht die
                    # strukturierte Ausgabe des Modell-Läufers extrem langsam
                    "input_json": {"type": "string"},
                },
                "required": ["nummer", "zweck", "input_json"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["ersatz"],
    "additionalProperties": False,
}

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


class Leitstelle:
    def __init__(self) -> None:
        self.url = os.environ.get("CODESCHMIEDE_LEITSTELLE_URL", "http://leitstelle:8530").rstrip("/")
        schluessel = os.environ.get("CODESCHMIEDE_LEITSTELLE_SCHLUESSEL") or (
            WURZEL / "data" / "leitstelle-schluessel"
        ).read_text().strip()
        self.client = httpx2.Client(
            headers={
                "Authorization": f"Bearer {schluessel}",
                "X-Leitstelle-Titel": "Codeschmiede%20Tests%20ersetzen",
                "X-Leitstelle-Arbeit": "codeschmiede-tests-ersetzen",
            },
            timeout=httpx2.Timeout(10.0, read=None),
        )

    def frage(self, nachricht: str) -> list[dict[str, Any]]:
        antwort = self.client.post(
            f"{self.url}/v1/chat/completions",
            json={
                "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": nachricht}],
                "response_format": {"type": "json_schema", "json_schema": {"name": "ersatz", "strict": True, "schema": SCHEMA}},
                "temperature": 0.4,
                "max_tokens": 1500,
            },
        )
        antwort.raise_for_status()
        return json.loads(antwort.json()["choices"][0]["message"]["content"])["ersatz"]


def anfrage(aufgabe: Aufgabe, offen: list[int], absagen: dict[int, str]) -> str:
    teile = [
        f"Funktion: {aufgabe.funktion}",
        f"Aufgabentext:\n{aufgabe.beschreibung_md}",
        "Sichtbare Tests:\n" + "\n".join(f"- input {json.dumps(t.input, ensure_ascii=False)} -> {json.dumps(t.expected, ensure_ascii=False)}" for t in aufgabe.tests_sichtbar),
        "Versteckte Tests (Nummer, input, Erwartung):\n" + "\n".join(
            f"- Nr. {i}: input {json.dumps(t.input, ensure_ascii=False)} -> {json.dumps(t.expected, ensure_ascii=False)}"
            + ("   <- VERRATEN, bitte ersetzen" if i in offen else "")
            for i, t in enumerate(aufgabe.tests_versteckt)
        ),
    ]
    if absagen:
        teile.append("Frühere Vorschläge wurden abgelehnt:\n" + "\n".join(f"- Nr. {i}: {g}" for i, g in absagen.items()))
    teile.append(f"Ersetze die Nummern {offen}.")
    return "\n\n".join(teile)


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


def bearbeite(aufgabe: Aufgabe, leitstelle: Leitstelle, runner: DockerRunner, loader: AufgabenLoader, trocken: bool) -> tuple[int, list[str]]:
    offen = verratene_tests(aufgabe)
    loesungen = [m["code"] for m in AufgabenLoader.musterloesungen_neben(aufgabe.dateipfad.parent)]
    if aufgabe.sprache != "python" or not aufgabe.funktion or not loesungen:
        return 0, [f"{aufgabe.id}: übersprungen (keine Python-Funktion mit Musterlösung)"]
    text = aufgabentext(aufgabe)
    vorhanden = [json.dumps(t.input, sort_keys=True) for t in aufgabe.tests_sichtbar + aufgabe.tests_versteckt]
    angenommen: dict[int, TestFall] = {}
    absagen: dict[int, str] = {}
    for _ in range(RUNDEN):
        rest = [i for i in offen if i not in angenommen]
        if not rest:
            break
        try:
            vorschlaege = leitstelle.frage(anfrage(aufgabe, rest, absagen))
        except Exception as fehler:  # noqa: BLE001  Netz, Schema, Leitstelle
            absagen = {i: f"Antwort unbrauchbar ({fehler})" for i in rest}
            continue
        kandidaten: list[tuple[int, list[Any]]] = []
        for v in vorschlaege:
            i = v.get("nummer")
            try:
                eingabe = json.loads(v.get("input_json", ""))
            except (TypeError, ValueError):
                eingabe = None
            if i not in rest or i in angenommen or not isinstance(eingabe, list):
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
        if not kandidaten:
            continue
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
                absagen.pop(i, None)
                vorhanden.append(json.dumps(eingabe, sort_keys=True))
    if angenommen and not trocken:
        ersetze_in_datei(aufgabe.dateipfad, angenommen)
        neu = loader.lade_aufgabe(aufgabe.dateipfad)
        for i, t in angenommen.items():
            assert neu.tests_versteckt[i].input == t.input and neu.tests_versteckt[i].expected == t.expected, aufgabe.id
    probleme = [f"{aufgabe.id} Nr. {i}: {absagen.get(i, 'kein Vorschlag')}" for i in offen if i not in angenommen]
    melde(f"{aufgabe.id}: {len(angenommen)} von {len(offen)} ersetzt")
    return len(angenommen), probleme


def main() -> None:
    teil = argparse.ArgumentParser()
    teil.add_argument("--nur", nargs="*", default=None)
    teil.add_argument("--trocken", action="store_true")
    teil.add_argument("--parallel", type=int, default=2)
    args = teil.parse_args()

    loader = AufgabenLoader(WURZEL / "aufgaben")
    aufgaben = [a for a in loader.lade_alle_aufgaben() if verratene_tests(a) and (args.nur is None or a.id in args.nur)]
    runner = DockerRunner({"python": "codeschmiede-sandbox:python"}, startzeit_sekunden=60)
    leitstelle = Leitstelle()
    melde(f"{len(aufgaben)} Aufgaben mit verratenen Tests")
    with ThreadPoolExecutor(max_workers=args.parallel) as pool:
        ergebnisse = list(pool.map(lambda a: bearbeite(a, leitstelle, runner, loader, args.trocken), aufgaben))
    ersetzt = sum(e[0] for e in ergebnisse)
    probleme = [p for e in ergebnisse for p in e[1]]
    melde(f"\nErsetzt: {ersetzt}; offen: {len(probleme)}")
    for p in probleme:
        melde(f"  {p}")


if __name__ == "__main__":
    main()
