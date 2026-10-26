SELECT name, SUBSTR(name, 1, 3) AS kuerzel, kolonie, COALESCE(lieblingsfisch, 'unbekannt') AS lieblingsfisch, 2026 - geburtsjahr AS jahre
FROM pinguine
WHERE kolonie IN ('Nord', 'Ost');
