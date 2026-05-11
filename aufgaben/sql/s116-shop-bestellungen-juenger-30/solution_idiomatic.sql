SELECT b.id, k.name, k.alter_jahre, b.bestellt_am FROM bestellungen b JOIN kunden k ON b.kunde_id = k.id WHERE k.alter_jahre < 30 ORDER BY b.bestellt_am, b.id;
