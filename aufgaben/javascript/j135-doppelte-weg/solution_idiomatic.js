const fische = prompt("Fische? ").split(",");
const sorten = new Set(fische);
console.log(`${fische.length} Fische, ${sorten.size} verschiedene`);
const liste = [];
for (const f of sorten) {
  liste.push(f);
}
console.log(liste.join(", "));
