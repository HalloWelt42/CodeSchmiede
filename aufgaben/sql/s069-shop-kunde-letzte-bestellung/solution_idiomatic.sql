SELECT k.name, MAX(b.bestellt_am) AS letzte FROM bestellungen b JOIN kunden k ON b.kunde_id = k.id GROUP BY k.id, k.name ORDER BY letzte DESC, k.name;
