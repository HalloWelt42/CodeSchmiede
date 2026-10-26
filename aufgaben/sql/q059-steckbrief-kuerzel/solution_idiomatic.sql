SELECT name, SUBSTR(name, 1, 3) AS kuerzel, kolonie, lieblingsfisch, 2026 - geburtsjahr AS jahre
FROM pinguine
WHERE kolonie IN ('Nord', 'Ost');
