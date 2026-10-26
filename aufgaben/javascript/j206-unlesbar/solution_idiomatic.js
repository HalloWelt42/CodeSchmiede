let gelesen = 0;
while (true) {
  const text = prompt("Zettel? ");
  if (!text) {
    break;
  }
  try {
    const daten = JSON.parse(text);
    gelesen++;
    console.log(daten?.name ?? "ohne Namen");
  } catch (fehler) {
    console.log("unlesbar");
  }
}
console.log(`Gelesen: ${gelesen}`);
