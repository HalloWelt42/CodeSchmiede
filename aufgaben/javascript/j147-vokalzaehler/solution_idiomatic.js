function vokale(wort) {
  let anzahl = 0;
  for (const z of wort.toLowerCase()) {
    if ("aeiouäöü".includes(z)) {
      anzahl++;
    }
  }
  return anzahl;
}
let bestes = "";
while (true) {
  const wort = prompt("Wort? ");
  if (!wort) {
    break;
  }
  console.log(`${wort}: ${vokale(wort)}`);
  if (bestes === "" || vokale(wort) > vokale(bestes)) {
    bestes = wort;
  }
}
console.log(`Die meisten: ${bestes}`);
