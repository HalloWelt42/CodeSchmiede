SELECT id, CAST(julianday(zurueck_am) - julianday(ausgeliehen_am) AS INTEGER) AS tage FROM ausleihen WHERE zurueck_am IS NOT NULL ORDER BY tage DESC, id;
