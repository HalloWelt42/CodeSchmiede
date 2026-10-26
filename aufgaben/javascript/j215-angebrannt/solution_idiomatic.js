function kochen(gericht) {
  return new Promise((erfuellen, ablehnen) => {
    setTimeout(() => {
      if (gericht === "Eis") {
        ablehnen(new Error("Eis kocht man nicht"));
      } else {
        erfuellen(`${gericht} ist fertig`);
      }
    }, 5);
  });
}
async function kueche() {
  while (true) {
    const gericht = prompt("Gericht? ");
    if (!gericht) {
      break;
    }
    try {
      console.log(await kochen(gericht));
    } catch (fehler) {
      console.log(`Oh nein: ${fehler.message}`);
    }
  }
  console.log("Feierabend");
}
kueche();
