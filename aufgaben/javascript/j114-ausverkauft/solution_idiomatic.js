const karte = ["Hering", "Aal", "Makrele", "Dorsch"];
const fisch = prompt("Ausverkauft? ");
const stelle = karte.indexOf(fisch);
if (stelle !== -1) {
  karte.splice(stelle, 1);
}
console.log(`Karte: ${karte.join(", ")}`);
