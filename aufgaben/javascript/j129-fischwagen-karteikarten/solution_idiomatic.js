const wagen = "Zum frostigen Hering";
const karte = [
  { name: "Heringsbrötchen", preis: 2.5 },
  { name: "Limonade", preis: 1.75 },
  { name: "Fischsuppe", preis: 4.5 },
];
console.log(`*** ${wagen.toUpperCase()} ***`);
const besuche = {};
const verkauft = {};
for (const ware of karte) {
  verkauft[ware.name] = 0;
}
let umsatz = 0;
while (true) {
  const kunde = prompt("Kunde? ");
  if (kunde === null || kunde === "") {
    break;
  }
  if (kunde in besuche) {
    console.log(`Willkommen zurück, ${kunde}!`);
    besuche[kunde]++;
  } else {
    besuche[kunde] = 1;
  }
  const anzahlen = [];
  for (const ware of karte) {
    const anzahl = Number(prompt(`${ware.name}? `));
    anzahlen.push(anzahl);
    verkauft[ware.name] += anzahl;
  }
  let summe = 0;
  console.log(`Kassenbon für ${kunde}`);
  for (let i = 0; i < karte.length; i++) {
    if (anzahlen[i] === 0) {
      continue;
    }
    const betrag = anzahlen[i] * karte[i].preis;
    console.log(`${anzahlen[i]} x ${karte[i].name}: ${betrag.toFixed(2)} Euro`);
    summe += betrag;
  }
  if (anzahlen[0] >= 3 && anzahlen[1] === 0) {
    console.log("1 x Limonade: gratis");
  }
  console.log("=".repeat(30));
  if (summe >= 20) {
    const rabatt = summe * 0.1;
    console.log(`Rabatt: -${rabatt.toFixed(2)} Euro`);
    summe -= rabatt;
  }
  console.log(`Summe: ${summe.toFixed(2)} Euro`);
  const stempel = Math.min(5, Math.floor(summe / 10));
  let stempelkarte = "";
  for (let i = 0; i < 5; i++) {
    stempelkarte += i < stempel ? "[*]" : "[ ]";
  }
  console.log(`Stempel: ${stempelkarte}`);
  umsatz += summe;
}
let alle = 0;
for (const name in besuche) {
  alle += besuche[name];
}
console.log(`Besuche heute: ${alle}`);
for (const name in besuche) {
  console.log(`${name}: ${besuche[name]} ${besuche[name] === 1 ? "Besuch" : "Besuche"}`);
}
for (const name in verkauft) {
  console.log(`${name}: ${verkauft[name]} verkauft`);
}
console.log(`Tagesumsatz: ${umsatz.toFixed(2)} Euro`);
