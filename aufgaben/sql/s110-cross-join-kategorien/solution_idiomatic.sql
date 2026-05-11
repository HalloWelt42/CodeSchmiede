SELECT k1.name AS a, k2.name AS b FROM kategorien k1 CROSS JOIN kategorien k2 WHERE k1.id < k2.id ORDER BY k1.name, k2.name;
