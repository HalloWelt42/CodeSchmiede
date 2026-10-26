const anzahl = Number(prompt("Brötchen? "));
let preis = 0;
if (anzahl > 0) {
  preis = anzahl * 2.5;
}
console.log("Preis:", preis);
