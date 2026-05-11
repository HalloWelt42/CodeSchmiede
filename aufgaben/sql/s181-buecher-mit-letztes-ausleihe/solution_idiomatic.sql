SELECT b.titel, MAX(a.ausgeliehen_am) AS letztes FROM ausleihen a JOIN buecher b ON a.buch_id = b.id GROUP BY b.id, b.titel ORDER BY letztes DESC, b.titel;
