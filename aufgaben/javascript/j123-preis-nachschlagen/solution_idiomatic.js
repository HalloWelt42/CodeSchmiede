const preise = { Hering: 2.5, Aal: 5, Makrele: 3.2 };
const fisch = prompt("Fisch? ");
if (fisch in preise) {
  console.log(`${fisch} kostet ${preise[fisch].toFixed(2)} Euro`);
} else {
  console.log(`${fisch} haben wir nicht`);
}
