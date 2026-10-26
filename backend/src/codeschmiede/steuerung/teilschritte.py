"""Teilschritte der Steuerungsspiele: ein Level ist eine Folge kleiner Ziele, die aufeinander aufbauen.

Jeder Teilschritt nennt neue Regeln und neue Abläufe, in denen er gilt; er schließt Regeln und Abläufe der vorigen
ein. Der erste gilt im ersten sichtbaren Ablauf, "alle" nimmt alle dazu, auch die versteckten. Geprüft wird immer
alles. "Schritt für Schritt"
in der Oberfläche zeigt die Ziele bis zum ersten offenen, "Alles auf einmal" alle; einen getrennt gespeicherten Stand
gibt es nicht, der Code selbst sagt, wie weit er ist.

Welche Regeln es gibt und wie sie prüfen, bringt jedes Spiel selbst mit (ampel_regeln); hier geht es nur um die
Folge und um die Befunde.
"""

from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import Literal, Protocol, TypeVar

from pydantic import BaseModel, Field

# so viele Befunde zeigt ein Teilschritt höchstens
BEFUNDE_JE_SCHRITT = 3


@dataclass(frozen=True)
class Befund:
    """Eine verletzte Regel an einer Stelle im Ablauf (Sekunde) oder im Ganzen (None)."""

    sekunde: float | None
    text: str

    def als_text(self, ablauf: str | None) -> str:
        stelle = f"Sekunde {self.sekunde:g}" if self.sekunde is not None else None
        kopf = ", ".join(x for x in (ablauf, stelle) if x)
        return f"{kopf}: {self.text}" if kopf else self.text


class Lauf(Protocol):
    name: str
    sichtbar: bool
    fehler: str | None


L = TypeVar("L", bound=Lauf)
R = TypeVar("R")


class TeilschrittStand(BaseModel):
    titel: str
    text: str
    erfuellt: bool
    # False, wenn der Schritt versteckte Abläufe braucht, die ein Probelauf nicht hat
    geprueft: bool = True
    befunde: list[str] = Field(default_factory=list)


class Vorgabe(Protocol[R]):
    titel: str
    text: str
    regeln: Sequence[R]
    # weitere Abläufe beim Namen, "alle" oder nichts Neues
    ablaeufe: Literal["alle"] | Sequence[str] | None


def ablauf_mengen(teilschritte: Sequence[Vorgabe[R]], alle_namen: Sequence[str], erster: str) -> list[set[str]]:
    """Je Teilschritt die Namen der Abläufe, in denen er gilt."""
    mengen: list[set[str]] = []
    menge = {erster}
    for schritt in teilschritte:
        if schritt.ablaeufe == "alle":
            menge = set(alle_namen)
        elif schritt.ablaeufe:
            menge = menge | set(schritt.ablaeufe)
        mengen.append(menge)
    return mengen


def auswerten(
    teilschritte: Sequence[Vorgabe[R]],
    laeufe: Sequence[L],
    pruefe: Callable[[R, L], list[Befund]],
    mengen: Sequence[set[str]],
) -> list[TeilschrittStand]:
    """Wertet jeden Teilschritt mit allen Regeln bis zu ihm in seinen Abläufen aus. Fehlt einer davon (ein Probelauf
    hat nur die sichtbaren), gilt der Schritt als noch nicht geprüft."""
    staende: list[TeilschrittStand] = []
    regeln: list[R] = []
    vorhanden = {lauf.name for lauf in laeufe}
    for schritt, menge in zip(teilschritte, mengen):
        # die neuen Regeln des Schritts zuerst: ihre Befunde sagen, was für ihn noch fehlt
        regeln = [*schritt.regeln, *regeln]
        auswahl = [lauf for lauf in laeufe if lauf.name in menge]
        befunde: list[str] = []
        for lauf in auswahl:
            name = lauf.name if len(menge) > 1 else None
            if lauf.fehler:
                befunde.append(Befund(None, lauf.fehler).als_text(name))
                continue
            for regel in regeln:
                befunde += [b.als_text(name) for b in pruefe(regel, lauf)]
        staende.append(TeilschrittStand(
            titel=schritt.titel,
            text=schritt.text,
            erfuellt=not befunde,
            geprueft=menge <= vorhanden,
            befunde=befunde[:BEFUNDE_JE_SCHRITT],
        ))
    return staende


def ablauf_befunde(regeln: Sequence[R], lauf: L, pruefe: Callable[[R, L], list[Befund]]) -> list[Befund]:
    """Alle Befunde eines Ablaufs über alle Regeln, nach der Stelle geordnet."""
    if lauf.fehler:
        return [Befund(None, lauf.fehler)]
    befunde = [b for regel in regeln for b in pruefe(regel, lauf)]
    return sorted(befunde, key=lambda b: (b.sekunde is None, b.sekunde or 0))
