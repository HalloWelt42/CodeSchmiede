-- Fortschritt im Aufbaukurs (kurs/fortschritt.py): jede Antwort auf eine Frage oder Vorhersage, jeder fertige
-- Abschnitt und jeder bestandene Kurztest als Ereignis. Stand, Erfahrung und Wiederholung leiten sich daraus ab.

CREATE TABLE kurs_ereignisse (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  art TEXT NOT NULL,           -- frage, vorhersage, abschnitt, kurztest_frage, kurztest
  einfuehrung TEXT NOT NULL,   -- Kennung der Einführung
  element TEXT NOT NULL,       -- Frage, Beispiel oder Abschnittsnummer; leer beim Kurztest
  richtig INTEGER NOT NULL,
  zeit DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX kurs_ereignisse_einfuehrung ON kurs_ereignisse (einfuehrung, art);
