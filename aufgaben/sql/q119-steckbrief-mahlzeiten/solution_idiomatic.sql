SELECT p.name, SUBSTR(p.name, 1, 3) AS kuerzel, p.kolonie, k.lage, COALESCE(p.lieblingsfisch, 'unbekannt') AS lieblingsfisch,
       2026 - p.geburtsjahr AS jahre,
       (SELECT COUNT(*) FROM fuetterungen f WHERE f.pinguin_id = p.id) AS mahlzeiten
FROM pinguine p
JOIN kolonien k ON k.name = p.kolonie
WHERE p.kolonie IN ('Nord', 'Ost')
ORDER BY jahre DESC, p.name;
