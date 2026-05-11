SELECT strftime('%Y', mitglied_seit) AS kohorte, COUNT(*) AS anzahl, ROUND(AVG(alter_jahre), 1) AS schnitt_alter FROM leser GROUP BY kohorte ORDER BY kohorte;
