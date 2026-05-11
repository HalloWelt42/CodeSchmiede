SELECT id, leser_id, buch_id, ausgeliehen_am FROM ausleihen WHERE zurueck_am IS NULL AND julianday('2026-05-11') - julianday(ausgeliehen_am) > 30 ORDER BY ausgeliehen_am;
