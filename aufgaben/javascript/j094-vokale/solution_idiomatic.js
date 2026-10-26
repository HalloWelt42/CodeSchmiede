const wort = prompt("Wort? ").toLowerCase();
let anzahl = 0;
for (const z of wort) {
  if ("aeiouäöü".includes(z)) {
    anzahl++;
  }
}
console.log(`Vokale: ${anzahl}`);
