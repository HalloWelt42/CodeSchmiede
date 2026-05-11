SELECT id, kunde_id, bestellt_am, LAG(bestellt_am) OVER (PARTITION BY kunde_id ORDER BY bestellt_am) AS vorher FROM bestellungen ORDER BY kunde_id, bestellt_am;
