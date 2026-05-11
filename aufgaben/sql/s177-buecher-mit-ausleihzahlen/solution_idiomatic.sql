SELECT b.titel, COUNT(a.id) AS ausleihen FROM buecher b LEFT JOIN ausleihen a ON a.buch_id = b.id GROUP BY b.id, b.titel ORDER BY ausleihen DESC, b.titel;
