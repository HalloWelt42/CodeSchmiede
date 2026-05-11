SELECT titel, jahr FROM buecher WHERE jahr > (SELECT 2026 - MAX(alter_jahre) FROM leser) ORDER BY jahr, titel;
