"""Streak-Berechnung -- aufeinanderfolgende Tage mit mindestens einer
gelösten Aufgabe. Inhaltlich klein, aber zentrale Motivations-Mechanik.
"""

from datetime import date, timedelta

from ..models.progress import Streak


def aktualisiere_streak(streak: Streak, heute: date) -> Streak:
    """Wird aufgerufen, wenn heute eine Aufgabe geloest wurde."""
    if streak.letzter_tag == heute:
        # Heute schon gezählt -- Idempotenz wichtig für mehrere
        # Submissions am gleichen Tag.
        return streak

    if streak.letzter_tag == heute - timedelta(days=1):
        neuer_aktuell = streak.aktuell + 1
    else:
        neuer_aktuell = 1

    return Streak(
        aktuell=neuer_aktuell,
        laengster=max(streak.laengster, neuer_aktuell),
        letzter_tag=heute,
    )


def streak_aktiv(streak: Streak, heute: date) -> bool:
    """True, wenn der Streak heute oder gestern fortgesetzt wurde."""
    if streak.letzter_tag is None:
        return False
    return (heute - streak.letzter_tag).days <= 1
