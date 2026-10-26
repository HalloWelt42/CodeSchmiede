SELECT name, 2026 - geburtsjahr AS jahre
FROM pinguine
WHERE kolonie IN ('Nord', 'Süd')
ORDER BY jahre DESC, name
LIMIT 3;
