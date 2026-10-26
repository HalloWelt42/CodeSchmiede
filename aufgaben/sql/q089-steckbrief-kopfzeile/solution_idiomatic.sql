SELECT COUNT(*) AS pinguine, ROUND(AVG(2026 - geburtsjahr), 1) AS durchschnittsalter
FROM pinguine
WHERE kolonie IN ('Nord', 'Ost');
