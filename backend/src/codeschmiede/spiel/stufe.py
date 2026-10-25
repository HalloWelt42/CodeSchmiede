"""Stufe aus Punkten: Stufe k gilt ab basis * k * k Punkten, die erste ab 0;
alle `titel_alle` Stufen ein neuer Titel."""

from math import isqrt

from ..models.konfig import SpielRegeln
from ..models.spiel import StufenStand


def schwelle(stufe: int, regeln: SpielRegeln) -> int:
    return 0 if stufe <= 1 else regeln.stufe_basis * stufe * stufe


def titel_von(stufe: int, regeln: SpielRegeln) -> str:
    return regeln.titel[min(stufe // regeln.titel_alle, len(regeln.titel) - 1)]


def stufe_aus_punkten(punkte: int, regeln: SpielRegeln) -> StufenStand:
    stufe = max(1, isqrt(max(0, punkte) // regeln.stufe_basis))
    titel_index = min(stufe // regeln.titel_alle, len(regeln.titel) - 1)
    hat_naechsten = titel_index + 1 < len(regeln.titel)
    return StufenStand(
        stufe=stufe,
        titel=regeln.titel[titel_index],
        punkte=punkte,
        ab=schwelle(stufe, regeln),
        bis=schwelle(stufe + 1, regeln),
        naechster_titel=regeln.titel[titel_index + 1] if hat_naechsten else None,
        naechster_titel_ab_stufe=(titel_index + 1) * regeln.titel_alle if hat_naechsten else None,
    )
