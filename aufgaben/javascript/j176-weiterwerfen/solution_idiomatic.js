const preise = { Hering: 2.5, Limonade: 1.75 };
function preisVon(ware) {
  if (!(ware in preise)) {
    throw new RangeError(ware);
  }
  return preise[ware];
}

function bon(waren) {
  for (const ware of waren) {
    try {
      console.log(`${ware.trim()}: ${preisVon(ware)}`);
    } catch (fehler) {
      if (fehler.name !== "RangeError") {
        throw fehler;
      }
      console.log(`unbekannt: ${fehler.message}`);
    }
  }
}

try {
  bon(["Hering", "Lachs", null]);
} catch (fehler) {
  console.log("Außen gefangen:", fehler.name);
}
