SELECT bestellung_id, produkt_id, menge, einzelpreis, ROUND(menge * einzelpreis, 2) AS zwischensumme FROM bestellpositionen ORDER BY bestellung_id, produkt_id;
