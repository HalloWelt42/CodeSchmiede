const zeiten = new Map([
  ["Suppe", 30],
  ["Brötchen", 10],
  ["Limonade", 5],
  ["Matjes", 15],
]);
function kochen(gericht) {
  return new Promise((erfuellen) => {
    setTimeout(() => {
      console.log(`fertig: ${gericht}`);
      erfuellen(gericht);
    }, zeiten.get(gericht));
  });
}
async function kueche() {
  const bestellung = [];
  while (true) {
    const gericht = prompt("Gericht? ");
    if (!gericht) {
      break;
    }
    if (!zeiten.has(gericht)) {
      console.log(`${gericht} gibt es nicht`);
      continue;
    }
    bestellung.push(gericht);
  }
  const tablett = await Promise.all(bestellung.map(kochen));
  console.log(`Tablett: ${tablett.length > 0 ? tablett.join(", ") : "leer"}`);
  console.log(`Wartezeit: ${Math.max(0, ...bestellung.map((g) => zeiten.get(g)))} ms`);
}
kueche();
