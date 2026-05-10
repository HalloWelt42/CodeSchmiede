-- Punkte-Erweiterung: pro Aufgabe wird in `progress` gespeichert,
-- wieviele Punkte beim besten bisherigen Bestanden erreicht wurden.
-- Berechnung: aufgabe.schwierigkeit_score - Summe der Kosten der bis
-- dahin geoeffneten Hints. Best-of (max ueber alle Submissions).

ALTER TABLE progress ADD COLUMN punkte_erreicht INTEGER DEFAULT 0;
