SELECT titel FROM buecher WHERE id NOT IN (SELECT DISTINCT buch_id FROM ausleihen) ORDER BY titel;
