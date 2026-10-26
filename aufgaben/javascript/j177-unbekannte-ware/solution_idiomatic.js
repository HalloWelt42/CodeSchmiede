const karte = new Map();
karte.set("Hering", 2.5);
karte.set("Limonade", 1.75);
karte.set("Suppe", 4.5);
function preis(ware) {
  if (!karte.has(ware)) {
    throw new Error("Ware gibt es nicht");
  }
  return karte.get(ware);
}
let summe = 0;
while (true) {
  const ware = prompt("Ware? ");
  if (!ware) {
    break;
  }
  try {
    const p = preis(ware);
    summe += p;
    console.log(`${ware}: ${p.toFixed(2)}`);
  } catch (fehler) {
    console.log(`${ware}: ${fehler.message}`);
  }
}
console.log(`Summe: ${summe.toFixed(2)}`);
