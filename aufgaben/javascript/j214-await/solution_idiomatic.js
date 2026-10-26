const warte = (ms) => new Promise((erfuellen) => setTimeout(erfuellen, ms));
async function fruehstueck() {
  const teile = ["Kaffee", "Brötchen", "Hering"];
  for (const teil of teile) {
    await warte(5);
    console.log(`${teil} ist fertig`);
  }
  return teile.length;
}
async function hauptprogramm() {
  const anzahl = await fruehstueck();
  console.log(`Frühstück aus ${anzahl} Teilen`);
}
hauptprogramm();
