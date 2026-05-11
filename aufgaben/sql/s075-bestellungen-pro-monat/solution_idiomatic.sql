SELECT strftime('%Y-%m', bestellt_am) AS monat, COUNT(*) AS anzahl FROM bestellungen GROUP BY monat ORDER BY monat;
