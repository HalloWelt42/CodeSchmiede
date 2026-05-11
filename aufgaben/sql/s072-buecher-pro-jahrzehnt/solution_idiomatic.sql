SELECT (jahr / 10) * 10 AS jahrzehnt, COUNT(*) AS anzahl FROM buecher GROUP BY (jahr / 10) * 10 ORDER BY jahrzehnt;
