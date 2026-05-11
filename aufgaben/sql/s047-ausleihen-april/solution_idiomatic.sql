SELECT id, leser_id, buch_id, ausgeliehen_am FROM ausleihen WHERE ausgeliehen_am BETWEEN '2025-04-01' AND '2025-04-30' ORDER BY ausgeliehen_am, id;
