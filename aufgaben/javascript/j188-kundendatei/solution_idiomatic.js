const kunden = [];
while (true) {
  const zeile = prompt("Zeile? ");
  if (!zeile) {
    break;
  }
  const [name, alter, ...lieblinge] = zeile.split(";");
  kunden.push({ name, alter: Number(alter), lieblinge });
}
for (const { name, alter, lieblinge } of kunden) {
  console.log(`${name} (${alter}) mag ${lieblinge.length > 0 ? lieblinge.join(", ") : "nichts Besonderes"}`);
}
if (kunden.length > 0) {
  console.log(`Ältester: ${Math.max(...kunden.map((k) => k.alter))}`);
  const alle = new Set();
  for (const k of kunden) {
    for (const fisch of k.lieblinge) {
      alle.add(fisch);
    }
  }
  console.log(`Alle Lieblinge: ${alle.size > 0 ? [...alle].join(", ") : "keine"}`);
}
