SELECT p.name
FROM fahrtenbuch b
JOIN fahrzeuge z ON z.kennzeichen = b.kennzeichen
JOIN firmen f ON f.id = z.firma_id
JOIN personen p ON p.id = b.fahrer_id
WHERE f.name = 'Schlüssel Sommer'
  AND z.farbe = 'blau'
  AND b.datum = '2026-03-14';
