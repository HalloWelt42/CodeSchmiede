let zahl = Number(prompt("Zahl? "));
let summe = 0;
while (zahl > 0) {
  summe += zahl % 10;
  zahl = Math.floor(zahl / 10);
}
console.log("Quersumme:", summe);
