SELECT tag, pinguin_id, fisch, menge
FROM fuetterungen
WHERE tag BETWEEN '2026-10-20' AND '2026-10-21'
  AND fisch IN ('Hering', 'Makrele')
  AND menge >= 5;
