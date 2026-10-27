"""Codes knacken: die Verfahren, mit denen der Server Nachrichten verschlüsselt, und die Häufigkeiten des Deutschen.

Im Level stehen je Nachricht nur Klartext und Schlüssel; den Geheimtext rechnet der Server hier aus. So kann kein
Level einen Geheimtext tragen, der nicht zu seinem Klartext passt.

Verfahren und ihre Schlüssel:
  caesar     Zahl 0 bis 25: jeder Buchstabe A bis Z rückt so viele Stellen weiter
  ersetzung  Mischung des Alphabets (26 Buchstaben) oder eine Zahl als Startwert für eine feste Mischung:
             A wird zum 1. Buchstaben der Mischung, B zum 2. usw.
  vigenere   Wort aus A bis Z: der n-te Buchstabe rückt um den n-ten Buchstaben des Worts (A = 0) weiter
  xor        Wort: die Bytes des Klartexts (UTF-8) mit den Bytes des Worts, reihum, als Hex
  schichten  Liste wie ["caesar:3", "base64", "hex"]: der Reihe nach angewandt
  pin        kein Schlüssel: der Klartext ist eine PIN, der Geheimtext ihr Prüfwert (SHA-256 als Hex)
Zeichen außer A bis Z (Leerzeichen, Satzzeichen, Ziffern, auch Ä, Ö, Ü und ß) bleiben bei den Buchstabenverfahren,
wie sie sind; Klartexte sind dort in Großbuchstaben.

Die Häufigkeiten (codes_deutsch.json) zählt tools/codes_deutsch.py aus den eigenen Texten.
"""

import base64
import hashlib
import json
import random
import re
from pathlib import Path
from typing import Literal

Verfahren = Literal["caesar", "ersetzung", "vigenere", "xor", "schichten", "pin"]
VERFAHREN: tuple[str, ...] = ("caesar", "ersetzung", "vigenere", "xor", "schichten", "pin")
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SCHICHTEN = ("base64", "hex")
PIN = re.compile(r"^[0-9]{4}$")

_DATEN = json.loads((Path(__file__).parent / "codes_deutsch.json").read_text(encoding="utf-8"))
# Anteil je Buchstabe in Prozent
DEUTSCH: dict[str, float] = _DATEN["buchstaben"]
# Anteil je Buchstabenpaar in Promille, _ steht für Wortanfang und Wortende
PAARE: dict[str, float] = _DATEN["paare"]


def schiebe(text: str, n: int) -> str:
    return "".join(ALPHABET[(ALPHABET.index(c) + n) % 26] if c in ALPHABET else c for c in text)


def mischung(startwert: int) -> str:
    return "".join(random.Random(startwert).sample(ALPHABET, 26))


def ersetze(text: str, alphabet: str) -> str:
    return "".join(alphabet[ALPHABET.index(c)] if c in ALPHABET else c for c in text)


def vigenere(text: str, wort: str) -> str:
    raus, i = [], 0
    for c in text:
        if c in ALPHABET:
            c = schiebe(c, ALPHABET.index(wort[i % len(wort)]))
            i += 1
        raus.append(c)
    return "".join(raus)


def xor_hex(text: str, wort: str) -> str:
    schluessel = wort.encode()
    return bytes(b ^ schluessel[i % len(schluessel)] for i, b in enumerate(text.encode())).hex()


def schicht(text: str, art: str) -> str:
    if art == "base64":
        return base64.b64encode(text.encode()).decode()
    if art == "hex":
        return text.encode().hex()
    return schiebe(text, int(art.split(":")[1]))


def pruefwert(pin: str) -> str:
    return hashlib.sha256(pin.encode()).hexdigest()


def verschluessele(verfahren: str, klar: str, schluessel: int | str | list[str] | None) -> str:
    if verfahren == "caesar":
        return schiebe(klar, int(schluessel))
    if verfahren == "ersetzung":
        return ersetze(klar, schluessel if isinstance(schluessel, str) else mischung(int(schluessel)))
    if verfahren == "vigenere":
        return vigenere(klar, str(schluessel))
    if verfahren == "xor":
        return xor_hex(klar, str(schluessel))
    if verfahren == "schichten":
        for art in schluessel:
            klar = schicht(klar, art)
        return klar
    if verfahren == "pin":
        return pruefwert(klar)
    raise ValueError(f"Verfahren {verfahren} gibt es nicht")


def _nur_grossbuchstaben(klar: str) -> list[str]:
    fremd = sorted({c for c in klar if c.isalpha() and c not in ALPHABET + "ÄÖÜß"})
    return [f"nur Großbuchstaben, nicht {''.join(fremd)}"] if fremd else []


def schluessel_fehler(verfahren: str, klar: str, schluessel: int | str | list[str] | None) -> list[str]:
    """Was an Klartext und Schlüssel nicht zum Verfahren passt (für die Bestandsprüfung)."""
    if verfahren == "ersetzung" and isinstance(schluessel, str):
        if sorted(schluessel) != list(ALPHABET):
            return ["die Mischung hat jeden Buchstaben A bis Z genau einmal"]
        return _nur_grossbuchstaben(klar)
    if verfahren in ("caesar", "ersetzung"):
        if not isinstance(schluessel, int) or isinstance(schluessel, bool):
            return ["der Schlüssel ist eine Zahl"]
        if verfahren == "caesar" and not 1 <= schluessel <= 25:
            return ["der Schlüssel liegt zwischen 1 und 25"]
        return _nur_grossbuchstaben(klar)
    if verfahren == "vigenere":
        if not isinstance(schluessel, str) or not schluessel or any(c not in ALPHABET for c in schluessel):
            return ["der Schlüssel ist ein Wort aus A bis Z"]
        return _nur_grossbuchstaben(klar)
    if verfahren == "xor":
        if not isinstance(schluessel, str) or not schluessel or not schluessel.isascii():
            return ["der Schlüssel ist ein Wort aus ASCII-Zeichen"]
        return []
    if verfahren == "schichten":
        if not isinstance(schluessel, list) or not schluessel:
            return ["der Schlüssel ist eine Liste von Schichten"]
        falsch = [s for s in schluessel if s not in SCHICHTEN and not re.fullmatch(r"caesar:([1-9]|1[0-9]|2[0-5])", s)]
        return [f"Schicht {s} gibt es nicht" for s in falsch] + _nur_grossbuchstaben(klar)
    if verfahren == "pin":
        return [] if schluessel is None and PIN.match(klar) else ["der Klartext ist eine PIN aus vier Ziffern, ohne Schlüssel"]
    return [f"Verfahren {verfahren} gibt es nicht"]


def anteil_gleich(ergebnis: str, soll: str) -> float:
    """Anteil der Buchstaben des Solls, die im Ergebnis an derselben Stelle stehen (ohne Buchstaben alle Zeichen).
    Leerzeichen und Satzzeichen bleiben beim Verschlüsseln, wie sie sind; sie zählen deshalb nicht mit."""
    stellen = [i for i, c in enumerate(soll) if c.isalpha()] or list(range(len(soll)))
    if not stellen:
        return 1.0 if ergebnis == soll else 0.0
    return sum(1 for i in stellen if i < len(ergebnis) and ergebnis[i] == soll[i]) / len(stellen)
