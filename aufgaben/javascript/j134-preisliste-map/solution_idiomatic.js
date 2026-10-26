const preise = new Map();
preise.set("Hering", 2.5);
preise.set("Aal", 5);
preise.set("Makrele", 3.2);
let summe = 0;
for (const fisch of preise.keys()) {
  console.log(`${fisch}: ${preise.get(fisch).toFixed(2)}`);
  summe += preise.get(fisch);
}
console.log(`Alles einmal: ${summe.toFixed(2)}`);
