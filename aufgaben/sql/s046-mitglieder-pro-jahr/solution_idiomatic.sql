SELECT strftime('%Y', mitglied_seit) AS jahr, COUNT(*) AS anzahl FROM leser GROUP BY jahr ORDER BY jahr;
