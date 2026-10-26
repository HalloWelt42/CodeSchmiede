const karte = [
  { name: "Heringsbrötchen", preis: 2.5 },
  { name: "Fischplatte", preis: 9.9 },
  { name: "Fischsuppe", preis: 4.5 },
];
let teuerstes = karte[0];
for (const gericht of karte) {
  if (gericht.preis > teuerstes.preis) {
    teuerstes = gericht;
  }
}
console.log(`Am teuersten: ${teuerstes.name} für ${teuerstes.preis.toFixed(2)} Euro`);
