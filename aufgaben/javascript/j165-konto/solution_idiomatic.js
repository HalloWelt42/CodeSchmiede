function kontoEroeffnen(start) {
  let guthaben = start;
  return {
    einzahlen: (betrag) => {
      guthaben += betrag;
    },
    stand: () => guthaben,
  };
}
const konto = kontoEroeffnen(20);
while (true) {
  const eingabe = prompt("Betrag? ");
  if (!eingabe) {
    break;
  }
  konto.einzahlen(Number(eingabe));
}
console.log(`Kontostand: ${konto.stand().toFixed(2)} Euro`);
