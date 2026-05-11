SELECT titel, exemplare FROM buecher WHERE exemplare > (SELECT AVG(exemplare) FROM buecher) ORDER BY exemplare DESC, titel;
