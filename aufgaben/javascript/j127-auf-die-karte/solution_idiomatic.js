const karte = [
  { name: "Heringsbrötchen", preis: 2.5 },
  { name: "Fischsuppe", preis: 4.5, scharf: true },
];
const name = prompt("Gericht? ");
const preis = Number(prompt("Preis? "));
karte.push({ name: name, preis: preis });
delete karte[1].scharf;
for (const gericht of karte) {
  console.log(`${gericht.name}: ${gericht.preis.toFixed(2)}`);
}
console.log("Scharf:", "scharf" in karte[1]);
