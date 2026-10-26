const wagen = "Zum frostigen Hering";
const karte = new Map();
karte.set("Heringsbrötchen", 2.5);
karte.set("Limonade", 1.75);
karte.set("Fischsuppe", 4.5);

function nummernGeber(start) {
  let naechste = start;
  return () => {
    const nummer = naechste;
    naechste++;
    return nummer;
  };
}

const bonNummer = nummernGeber(1);

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
  console.log(`Kassenbon Nr. ${bonNummer()} für ${kunde}`);
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

function tagesabschluss(besuche, verkauft, umsatz, jeKunde) {
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
  const rangliste = [];
  for (const name of jeKunde.keys()) {
    rangliste.push({ name: name, betrag: jeKunde.get(name) });
  }
  if (rangliste.length > 0) {
    rangliste.sort((a, b) => b.betrag - a.betrag);
    console.log(`Rangliste: ${rangliste.map(k => `${k.name} ${k.betrag.toFixed(2)}`).join(", ")}`);
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
const jeKunde = new Map();
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
  const summe = bonDrucken(kunde, anzahlen);
  umsatz += summe;
  jeKunde.set(kunde, (jeKunde.get(kunde) || 0) + summe);
}
tagesabschluss(besuche, verkauft, umsatz, jeKunde);
