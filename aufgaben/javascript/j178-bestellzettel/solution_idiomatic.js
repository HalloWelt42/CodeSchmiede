const karte = { Hering: 2.5, Limonade: 1.75, Suppe: 4.5 };
function pruefen(zeile) {
  const teile = zeile.split(" ");
  if (teile.length !== 2) {
    throw new Error("Format ist: Anzahl Ware");
  }
  const anzahl = Number(teile[0]);
  if (teile[0].trim() === "" || !Number.isInteger(anzahl) || anzahl <= 0) {
    throw new RangeError(`"${teile[0]}" ist keine gültige Anzahl`);
  }
  if (!(teile[1] in karte)) {
    throw new Error(`${teile[1]} gibt es nicht`);
  }
  return { anzahl: anzahl, ware: teile[1] };
}
let summe = 0;
let fehlerhaft = 0;
while (true) {
  const zeile = prompt("Zeile? ");
  if (!zeile) {
    break;
  }
  try {
    const posten = pruefen(zeile);
    const betrag = posten.anzahl * karte[posten.ware];
    summe += betrag;
    console.log(`${posten.anzahl} x ${posten.ware}: ${betrag.toFixed(2)} Euro`);
  } catch (fehler) {
    fehlerhaft++;
    console.log(`Übersprungen: ${fehler.message}`);
  }
}
console.log(`Summe: ${summe.toFixed(2)} Euro`);
console.log(`Fehlerhafte Zeilen: ${fehlerhaft}`);
