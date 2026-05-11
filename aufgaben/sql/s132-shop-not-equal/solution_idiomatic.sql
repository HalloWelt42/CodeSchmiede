SELECT pr.name, k.name AS kategorie FROM produkte pr JOIN kategorien k ON pr.kategorie_id = k.id WHERE k.name != 'Süßwaren' ORDER BY pr.name;
