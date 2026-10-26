INSERT INTO fuetterungen (pinguin_id, tag, fisch, menge)
SELECT id, '2026-10-23', 'Hering', 3
FROM pinguine
WHERE kolonie = 'Ost';
