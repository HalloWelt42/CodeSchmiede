let anzahl = 0;
let summe = 0;
let groesste = 0;
while (true) {
  const eingabe = prompt("Betrag? ");
  if (eingabe === null || eingabe === "fertig") {
    break;
  }
  const betrag = Number(eingabe);
  if (betrag <= 0) {
    console.log("Nur positive Beträge!");
  } else {
    anzahl++;
    summe += betrag;
    if (betrag > groesste) {
      groesste = betrag;
    }
  }
}
console.log(`Einzahlungen: ${anzahl}`);
console.log(`Summe: ${summe.toFixed(2)} Euro`);
console.log(`Größte: ${groesste.toFixed(2)} Euro`);
