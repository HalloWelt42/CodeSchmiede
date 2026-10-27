"""Häufigkeiten des Deutschen für das Spiel Codes knacken, gezählt aus den eigenen Texten der Codeschmiede.

Gezählt werden die Aufgabentexte, die Kursinhalte und die Dokumentation (ohne Frontmatter und ohne Code), in
Großbuchstaben A bis Z. Ä, Ö, Ü und ß zählen nicht und trennen wie ein Leerzeichen: das Spiel verschlüsselt nur A bis Z,
ein Wort ist dort eine Folge aus A bis Z. Heraus kommt
backend/src/codeschmiede/steuerung/codes_deutsch.json:

  buchstaben  Anteil je Buchstabe in Prozent
  paare       Anteil je Buchstabenpaar in Promille, mit _ für Wortanfang und Wortende ("_E": ein Wort beginnt mit E;
              nur Paare, die vorkommen)

Aufruf (aus dem Projektordner): python3 tools/codes_deutsch.py
"""

import collections
import json
import pathlib
import re

WURZEL = pathlib.Path(__file__).resolve().parent.parent
ZIEL = WURZEL / "backend/src/codeschmiede/steuerung/codes_deutsch.json"
QUELLEN = ["aufgaben/**/aufgabe.md", "docs/*.md", "kurs/**/*.md"]


def text_ohne_code(datei: pathlib.Path) -> str:
    text = datei.read_text(encoding="utf-8", errors="ignore")
    text = re.sub(r"\A---.*?^---", "", text, flags=re.S | re.M)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    return re.sub(r"`[^`]*`", " ", text)


def main() -> None:
    text = " ".join(text_ohne_code(p) for muster in QUELLEN for p in sorted(WURZEL.glob(muster))).upper()
    woerter = re.findall(r"[A-Z]+", text)
    buchstaben = collections.Counter("".join(woerter))
    paare = collections.Counter(w[i:i + 2] for w in (f"_{w}_" for w in woerter) for i in range(len(w) - 1))
    summe_b, summe_p = sum(buchstaben.values()), sum(paare.values())
    daten = {
        "quelle": f"{summe_b} Buchstaben aus den Texten der Codeschmiede",
        "buchstaben": {b: round(100 * buchstaben[b] / summe_b, 2) for b in map(chr, range(65, 91))},
        "paare": {p: round(1000 * n / summe_p, 3) for p, n in sorted(paare.items()) if round(1000 * n / summe_p, 3) > 0},
    }
    ZIEL.write_text(json.dumps(daten, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{ZIEL.relative_to(WURZEL)}: {summe_b} Buchstaben, {len(daten['paare'])} Paare")


if __name__ == "__main__":
    main()
