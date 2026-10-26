const wagen = "Zum frostigen Hering";
const karte = new Map();
karte.set("Heringsbrötchen", 2.5);
karte.set("Limonade", 1.75);
karte.set("Fischsuppe", 4.5);

function euro(betrag) {
  return `${betrag.toFixed(2)} Euro`;
}

function rabattSatz(summe) {
  if (summe >= 40) {
    return 15;
  }
  if (summe >= 20) {
    return 10;
  }
  return 0;
}

function stempelkarte(summe) {
  const stempel = Math.min(5, Math.floor(summe / 10));
  let karteText = "";
  for (let i = 0; i < 5; i++) {
    karteText += i < stempel ? "[*]" : "[ ]";
  }
  return karteText;
}

function anzahlenAbfragen() {
  const anzahlen = new Map();
  for (const ware of karte.keys()) {
    anzahlen.set(ware, Number(prompt(`${ware}? `)));
  }
  return anzahlen;
}

function bonDrucken(kunde, anzahlen) {
  let summe = 0;
  console.log(`Kassenbon für ${kunde}`);
  for (const ware of karte.keys()) {
    const anzahl = anzahlen.get(ware);
    if (anzahl === 0) {
      continue;
    }
    const betrag = anzahl * karte.get(ware);
    console.log(`${anzahl} x ${ware}: ${euro(betrag)}`);
    summe += betrag;
  }
  if (anzahlen.get("Heringsbrötchen") >= 3 && anzahlen.get("Limonade") === 0) {
    console.log("1 x Limonade: gratis");
  }
  console.log("=".repeat(30));
  const satz = rabattSatz(summe);
  if (satz > 0) {
    const rabatt = (summe * satz) / 100;
    console.log(`Rabatt ${satz} %: -${euro(rabatt)}`);
    summe -= rabatt;
  }
  console.log(`Summe: ${euro(summe)}`);
  console.log(`Stempel: ${stempelkarte(summe)}`);
  return summe;
}

function tagesabschluss(besuche, verkauft, umsatz) {
  let alle = 0;
  for (const anzahl of besuche.values()) {
    alle += anzahl;
  }
  console.log(`Besuche heute: ${alle}`);
  console.log(`Verschiedene Kunden: ${besuche.size}`);
  for (const name of besuche.keys()) {
    const n = besuche.get(name);
    console.log(`${name}: ${n} ${n === 1 ? "Besuch" : "Besuche"}`);
  }
  const nie = [];
  for (const ware of verkauft.keys()) {
    const n = verkauft.get(ware);
    if (n === 0) {
      nie.push(ware);
    } else {
      console.log(`${ware}: ${n} verkauft`);
    }
  }
  if (nie.length > 0) {
    console.log(`Nicht verkauft: ${nie.join(", ")}`);
  }
  console.log(`Tagesumsatz: ${euro(umsatz)}`);
}

console.log(`*** ${wagen.toUpperCase()} ***`);
const besuche = new Map();
const verkauft = new Map();
for (const ware of karte.keys()) {
  verkauft.set(ware, 0);
}
let umsatz = 0;
while (true) {
  const kunde = prompt("Kunde? ");
  if (kunde === null || kunde === "") {
    break;
  }
  if (besuche.has(kunde)) {
    console.log(`Willkommen zurück, ${kunde}!`);
    besuche.set(kunde, besuche.get(kunde) + 1);
  } else {
    besuche.set(kunde, 1);
  }
  const anzahlen = anzahlenAbfragen();
  for (const ware of karte.keys()) {
    verkauft.set(ware, verkauft.get(ware) + anzahlen.get(ware));
  }
  umsatz += bonDrucken(kunde, anzahlen);
}
tagesabschluss(besuche, verkauft, umsatz);
