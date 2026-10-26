const wagen = "Zum frostigen Hering";
const waren = ["Heringsbrötchen", "Limonade", "Fischsuppe"];
const preise = [2.5, 1.75, 4.5];
console.log(`*** ${wagen.toUpperCase()} ***`);
const namen = [];
let umsatz = 0;
while (true) {
  const kunde = prompt("Kunde? ");
  if (kunde === null || kunde === "") {
    break;
  }
  const anzahlen = [];
  for (const ware of waren) {
    anzahlen.push(Number(prompt(`${ware}? `)));
  }
  let summe = 0;
  console.log(`Kassenbon für ${kunde}`);
  for (let i = 0; i < waren.length; i++) {
    if (anzahlen[i] === 0) {
      continue;
    }
    console.log(`${anzahlen[i]} x ${waren[i]}: ${(anzahlen[i] * preise[i]).toFixed(2)} Euro`);
    summe += anzahlen[i] * preise[i];
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
  let karte = "";
  for (let i = 0; i < 5; i++) {
    karte += i < stempel ? "[*]" : "[ ]";
  }
  console.log(`Stempel: ${karte}`);
  namen.push(kunde);
  umsatz += summe;
}
console.log(`Kunden heute: ${namen.length}`);
if (namen.length > 0) {
  console.log(`Namen: ${namen.join(", ")}`);
}
console.log(`Tagesumsatz: ${umsatz.toFixed(2)} Euro`);
