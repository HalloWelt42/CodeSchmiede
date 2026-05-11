SELECT name, CAST((julianday('2026-05-11') - julianday(mitglied_seit)) / 365 AS INTEGER) AS jahre FROM leser ORDER BY jahre DESC, name;
