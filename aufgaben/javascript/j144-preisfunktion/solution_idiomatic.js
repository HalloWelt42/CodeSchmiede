function preis(anzahl, einzelpreis) {
  return anzahl * einzelpreis;
}

function euro(betrag) {
  return `${betrag.toFixed(2)} Euro`;
}

const broetchen = Number(prompt("Brötchen? "));
const suppen = Number(prompt("Suppen? "));
console.log(`Brötchen: ${euro(preis(broetchen, 2.5))}`);
console.log(`Suppen: ${euro(preis(suppen, 4.5))}`);
console.log(`Zusammen: ${euro(preis(broetchen, 2.5) + preis(suppen, 4.5))}`);
