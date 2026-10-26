const standard = { waehrung: "Euro", rabatt: "10", stempel: "5" };
const wuensche = {};
const text = prompt("Wünsche? ");
if (text) {
  for (const paar of text.split(",")) {
    const [schluessel, wert] = paar.split("=");
    wuensche[schluessel] = wert;
  }
}
const einstellungen = { ...standard, ...wuensche };
for (const schluessel in einstellungen) {
  console.log(`${schluessel}: ${einstellungen[schluessel]}`);
}
