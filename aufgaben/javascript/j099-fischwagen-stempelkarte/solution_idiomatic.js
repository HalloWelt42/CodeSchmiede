const wagen = "Zum frostigen Hering";
const preisBroetchen = 2.5;
const preisLimonade = 1.75;
console.log(`*** ${wagen.toUpperCase()} ***`);
let kunden = 0;
let umsatz = 0;
while (true) {
  const kunde = prompt("Kunde? ");
  if (kunde === null || kunde === "") {
    break;
  }
  const broetchen = Number(prompt("Brötchen? "));
  const limonaden = Number(prompt("Limonaden? "));
  let summe = 0;
  console.log(`Kassenbon für ${kunde}`);
  console.log(`${broetchen} x Heringsbrötchen: ${(broetchen * preisBroetchen).toFixed(2)} Euro`);
  summe += broetchen * preisBroetchen;
  console.log(`${limonaden} x Limonade: ${(limonaden * preisLimonade).toFixed(2)} Euro`);
  summe += limonaden * preisLimonade;
  if (broetchen >= 3 && limonaden === 0) {
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
  kunden++;
  umsatz += summe;
}
console.log(`Kunden heute: ${kunden}`);
console.log(`Tagesumsatz: ${umsatz.toFixed(2)} Euro`);
