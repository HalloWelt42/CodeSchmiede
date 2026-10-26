function verkaufen(anzahl) {
  if (anzahl > 10) {
    throw new Error("zu viele");
  }
  console.log(`${anzahl} verkauft`);
}
for (let i = 0; i < 2; i++) {
  try {
    verkaufen(Number(prompt("Anzahl? ")));
  } catch (fehler) {
    console.log(`Abgelehnt: ${fehler.message}`);
  } finally {
    console.log("Kasse zu");
  }
}
