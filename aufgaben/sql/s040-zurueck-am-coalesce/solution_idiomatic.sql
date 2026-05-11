SELECT id, COALESCE(zurueck_am, 'offen') AS zurueck FROM ausleihen ORDER BY id;
