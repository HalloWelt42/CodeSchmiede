SELECT id, kunde_id, bestellt_am, ROW_NUMBER() OVER (PARTITION BY kunde_id ORDER BY bestellt_am) AS rang FROM bestellungen ORDER BY kunde_id, rang;
