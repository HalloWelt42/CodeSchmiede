SELECT tag,
       SUM(CASE WHEN menge >= 6 THEN 1 ELSE 0 END) AS grosse,
       SUM(CASE WHEN fisch = 'Lachs' THEN menge ELSE 0 END) AS lachs,
       SUM(menge) AS alle
FROM fuetterungen
GROUP BY tag
ORDER BY tag;
