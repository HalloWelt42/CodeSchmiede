SELECT id, status, bestellt_am, COUNT(*) OVER (PARTITION BY status ORDER BY bestellt_am, id) AS lfd FROM bestellungen ORDER BY status, bestellt_am, id;
