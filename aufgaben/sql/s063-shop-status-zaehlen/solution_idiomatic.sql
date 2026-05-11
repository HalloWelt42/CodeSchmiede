SELECT status, COUNT(*) AS anzahl FROM bestellungen GROUP BY status ORDER BY status;
