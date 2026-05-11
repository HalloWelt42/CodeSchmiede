SELECT name FROM leser WHERE alter_jahre < (2026 - (SELECT MIN(jahr) FROM buecher)) ORDER BY name;
