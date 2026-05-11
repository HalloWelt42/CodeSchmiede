SELECT strftime('%Y-%m', ausgeliehen_am) AS monat, COUNT(*) AS anzahl FROM ausleihen GROUP BY monat ORDER BY monat;
