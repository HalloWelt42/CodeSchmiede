function warte(ms, wert) {
  return new Promise((erfuellen) => {
    setTimeout(() => erfuellen(wert), ms);
  });
}
warte(10, "Hering").then((fisch) => console.log(`Angekommen: ${fisch}`));
console.log("Warte auf den Fisch ...");
