const lager = new Map();
lager.set("Hering", 12);
lager.set("Aal", 3);
const objekt = {};
for (const [ware, menge] of lager) {
  objekt[ware] = menge;
}
const text = JSON.stringify(objekt);
console.log(text);
const geladen = JSON.parse(text);
const neu = new Map();
for (const ware in geladen) {
  neu.set(ware, geladen[ware]);
}
console.log(`Wieder da: ${neu.size} Sorten, Hering: ${neu.get("Hering")}`);
