SELECT name, mitglied_seit FROM leser WHERE julianday('2026-05-11') - julianday(mitglied_seit) > 1825 ORDER BY mitglied_seit, name;
