const lager = {};
while (true) {
  const eintrag = prompt("Eintrag? ");
  if (!eintrag) {
    break;
  }
  const teile = eintrag.split(" ");
  const ware = teile[0];
  const menge = Number(teile[1]);
  if (ware in lager) {
    lager[ware] += menge;
  } else {
    lager[ware] = menge;
  }
  if (lager[ware] <= 0) {
    delete lager[ware];
  }
}
const sorten = Object.keys(lager);
if (sorten.length === 0) {
  console.log("Lager leer");
}
for (const ware of sorten) {
  console.log(`${ware}: ${lager[ware]}`);
}
console.log(`Sorten: ${sorten.length}`);
