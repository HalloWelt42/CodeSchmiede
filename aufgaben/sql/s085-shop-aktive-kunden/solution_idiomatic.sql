SELECT COUNT(DISTINCT kunde_id) AS aktive FROM bestellungen WHERE status != 'storniert';
