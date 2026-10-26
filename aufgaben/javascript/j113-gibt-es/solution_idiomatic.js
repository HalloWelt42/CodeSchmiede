const karte = ["Hering", "Aal", "Makrele", "Dorsch"];
const fisch = prompt("Fisch? ");
if (karte.includes(fisch)) {
  console.log(`${fisch} gibt es, Nummer ${karte.indexOf(fisch) + 1}`);
} else {
  console.log(`${fisch} gibt es nicht`);
}
