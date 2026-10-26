SELECT SUM(CASE WHEN lieblingsfisch IS NULL THEN 1 ELSE 0 END) AS raetsel,
       COUNT(*) AS alle
FROM pinguine;
