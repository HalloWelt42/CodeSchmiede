SELECT name, kolonie, lieblingsfisch, 2026 - geburtsjahr AS jahre
FROM pinguine
WHERE kolonie IN ('Nord', 'Ost');
