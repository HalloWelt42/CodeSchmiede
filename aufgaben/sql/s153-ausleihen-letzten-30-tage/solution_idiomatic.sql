SELECT id, leser_id, buch_id, ausgeliehen_am FROM ausleihen WHERE julianday('2025-05-01') - julianday(ausgeliehen_am) <= 30 AND ausgeliehen_am <= '2025-05-01' ORDER BY ausgeliehen_am DESC, id;
