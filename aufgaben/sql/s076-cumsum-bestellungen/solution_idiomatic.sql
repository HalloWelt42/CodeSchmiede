SELECT bestellt_am, COUNT(*) AS tag, SUM(COUNT(*)) OVER (ORDER BY bestellt_am) AS kumulativ FROM bestellungen GROUP BY bestellt_am ORDER BY bestellt_am;
