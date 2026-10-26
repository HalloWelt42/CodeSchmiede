const alter = Number(prompt("Alter? "));
const mitglied = prompt("Mitglied? ");
let preis;
if (alter < 6) {
  preis = 0;
} else if (alter < 18) {
  preis = 4;
} else if (alter >= 65) {
  preis = 5;
} else {
  preis = 8;
}
if (mitglied === "ja") {
  preis /= 2;
}
console.log(`Eintritt: ${preis === 0 ? "frei" : `${preis.toFixed(2)} Euro`}`);
