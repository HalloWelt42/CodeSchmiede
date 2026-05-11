SELECT status, COUNT(DISTINCT kunde_id) AS kunden FROM bestellungen GROUP BY status ORDER BY status;
