const posten = JSON.parse(prompt("Bestellung? "));
let summe = 0;
for (const { ware, anzahl, preis } of posten) {
  console.log(`${anzahl} x ${ware}: ${(anzahl * preis).toFixed(2)}`);
  summe += anzahl * preis;
}
console.log(`Summe: ${summe.toFixed(2)}`);
