SELECT name, SUBSTR(name, 1, INSTR(name, ' ') - 1) AS vorname, SUBSTR(name, INSTR(name, ' ') + 1) AS nachname FROM leser ORDER BY nachname, vorname;
