_NAMEN = [
    "",
    "Januar", "Februar", "Maerz", "April",
    "Mai", "Juni", "Juli", "August",
    "September", "Oktober", "November", "Dezember",
]


def monatsname(monat: int) -> str:
    if 1 <= monat <= 12:
        return _NAMEN[monat]
    return ""
