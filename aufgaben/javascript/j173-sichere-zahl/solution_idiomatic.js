function liesZahl(text) {
  const zahl = Number(text);
  if (text.trim() === "" || Number.isNaN(zahl)) {
    throw new Error(`"${text}" ist keine Zahl`);
  }
  return zahl;
}
let anzahl;
while (true) {
  try {
    anzahl = liesZahl(prompt("Anzahl? "));
    break;
  } catch (fehler) {
    console.log(fehler.message);
  }
}
console.log(`Doppelt: ${anzahl * 2}`);
