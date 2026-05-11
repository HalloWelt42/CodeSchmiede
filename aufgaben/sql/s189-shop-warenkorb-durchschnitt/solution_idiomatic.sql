WITH summen AS (  SELECT bestellung_id, SUM(menge * einzelpreis) AS wert   FROM bestellpositionen GROUP BY bestellung_id) SELECT ROUND(AVG(wert), 2) AS schnitt FROM summen;
