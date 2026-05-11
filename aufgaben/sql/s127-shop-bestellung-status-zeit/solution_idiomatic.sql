SELECT strftime('%Y-%m', bestellt_am) AS monat, status, COUNT(*) AS anzahl FROM bestellungen GROUP BY monat, status ORDER BY monat, status;
