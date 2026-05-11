import csv


def csv_zeile(s: str) -> list[str]:
    if not s:
        return []
    return list(csv.reader([s]))[0]
