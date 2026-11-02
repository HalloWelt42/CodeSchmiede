"""Laufzeiten der Sandbox: welche Sprache in welchem Abbild läuft. Eine Laufzeit ist eine Sprache, bei PHP mit ihrer
Fassung ("php-8.3"); jede hat ihr Abbild codeschmiede-sandbox:<laufzeit>. Die Fassungen von PHP stehen nur hier
(Nachschlag WIKI-48 und WIKI-52, Wahl des Nutzers 02.11.2026: 5.6, 7.4 und 8.0 bis 8.5). Der Sandbox-Dienst nimmt
daraus seine Abbilder, die Schnittstelle für Apps ihr Angebot, das Ausrollen baut die PHP-Abbilder aus
sandbox-bilder/php.Dockerfile."""

from __future__ import annotations

#: PHP-Fassungen mit eigenem Abbild, neueste zuerst
PHP_FASSUNGEN: tuple[str, ...] = ("8.5", "8.4", "8.3", "8.2", "8.1", "8.0", "7.4", "5.6")

#: Sprachen, deren Lauf der Debugger aufzeichnen kann (die übrigen nur ausführen)
MIT_AUFZEICHNUNG: tuple[str, ...] = ("python", "javascript")


def laufzeit(sprache: str, fassung: str = "") -> str:
    """Name der Laufzeit: die Sprache, mit Fassung angehängt ("php-8.3")."""
    return f"{sprache}-{fassung}" if fassung else sprache


def grundsprache(name: str) -> str:
    """Die Sprache einer Laufzeit ("php-8.3" -> "php")."""
    return name.split("-", 1)[0]


def abbild(name: str) -> str:
    return f"codeschmiede-sandbox:{name}"


def bilder() -> dict[str, str]:
    """Vorgabe des Sandbox-Dienstes: jede Laufzeit mit ihrem Abbild."""
    namen = [*MIT_AUFZEICHNUNG, *(laufzeit("php", f) for f in PHP_FASSUNGEN)]
    return {n: abbild(n) for n in namen}
