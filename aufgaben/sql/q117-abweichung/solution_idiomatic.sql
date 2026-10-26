SELECT name, gewicht_kg,
       ROUND(gewicht_kg - (SELECT AVG(gewicht_kg) FROM pinguine WHERE kolonie = p.kolonie), 2) AS abweichung
FROM pinguine p
WHERE kolonie = 'Nord';
