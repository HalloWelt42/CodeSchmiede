function teilen(fische, pinguine) {
  if (pinguine === 0) {
    throw new Error("Niemand da zum Teilen");
  }
  return fische / pinguine;
}
const fische = Number(prompt("Fische? "));
const pinguine = Number(prompt("Pinguine? "));
try {
  console.log(`Jeder bekommt ${teilen(fische, pinguine)}`);
} catch (fehler) {
  console.log(`Fehler: ${fehler.message}`);
} finally {
  console.log("Fertig");
}
