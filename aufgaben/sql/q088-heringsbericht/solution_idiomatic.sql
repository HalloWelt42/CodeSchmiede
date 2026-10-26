SELECT COUNT(*) AS fuetterungen, SUM(menge) AS fische, MAX(menge) AS groesste,
       ROUND(AVG(menge), 1) AS schnitt
FROM fuetterungen
WHERE fisch = 'Hering';
