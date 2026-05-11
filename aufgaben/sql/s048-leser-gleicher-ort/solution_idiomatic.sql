SELECT l1.name AS leser_a, l2.name AS leser_b, l1.ort FROM leser l1 JOIN leser l2 ON l1.ort = l2.ort AND l1.id < l2.id ORDER BY l1.ort, l1.name, l2.name;
