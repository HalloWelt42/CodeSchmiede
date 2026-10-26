SELECT p.name AS pinguin, f.fisch, f.menge
FROM fuetterungen f
JOIN pinguine p ON p.id = f.pinguin_id
WHERE f.tag = '2026-10-21';
