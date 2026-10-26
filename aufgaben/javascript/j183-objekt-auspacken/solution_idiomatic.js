const suppe = { name: "Fischsuppe", preis: 4.5, scharf: true };
const broetchen = { name: "Heringsbrötchen", preis: 2.5 };
function zeile({ name, preis, scharf = false }) {
  return `${name}: ${preis.toFixed(2)} Euro${scharf ? " (scharf)" : ""}`;
}
console.log(zeile(suppe));
console.log(zeile(broetchen));
