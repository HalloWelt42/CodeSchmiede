SELECT id, kunde_id, bestellt_am FROM bestellungen WHERE status = 'geliefert' ORDER BY bestellt_am DESC LIMIT 1;
