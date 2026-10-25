SELECT DISTINCT f.name
FROM firmen f
JOIN fahrzeuge z ON z.firma_id = f.id
JOIN durchfahrten d ON d.kennzeichen = z.kennzeichen
WHERE f.branche = 'Schlüsseldienst'
  AND z.farbe = 'blau'
  AND d.zeit BETWEEN '2026-03-14 21:00' AND '2026-03-14 22:30';
