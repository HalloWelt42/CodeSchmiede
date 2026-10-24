"""Gemeinsamer Schlüssel zwischen Backend und Sandbox-Dienst.

Ist er per Umgebung gesetzt, gilt dieser Wert. Sonst liegt er als Datei
im Datenordner; wer zuerst startet, legt sie an (exklusiv, nur für den
Eigentümer lesbar), der andere liest sie.
"""

import os
import secrets
import time
from pathlib import Path

from pydantic import SecretStr


def lade_schluessel(gesetzt: SecretStr, datei: Path) -> str:
    wert = gesetzt.get_secret_value().strip()
    if wert:
        return wert
    datei.parent.mkdir(parents=True, exist_ok=True)
    try:
        fd = os.open(datei, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        # Der andere Prozess kann die Datei gerade erst angelegt haben.
        for _ in range(40):
            if inhalt := datei.read_text(encoding="utf-8").strip():
                return inhalt
            time.sleep(0.05)
        raise RuntimeError(f"Schlüsseldatei {datei} ist leer")
    neu = secrets.token_urlsafe(32)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(neu + "\n")
    return neu
