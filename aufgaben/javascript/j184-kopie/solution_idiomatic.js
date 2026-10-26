const karte = [{ name: "Hering", preis: 2.5 }, { name: "Suppe", preis: 4.5 }];
const zeigen = (liste) => liste.map((g) => `${g.name} ${g.preis.toFixed(2)}`).join(", ");
const angebot = [...karte.map((g) => ({ ...g, preis: g.preis * 0.8 })), { name: "Matjes", preis: 3 }];
console.log(`Angebot: ${zeigen(angebot)}`);
console.log(`Original: ${zeigen(karte)}`);
