const teile = prompt("Fänge? ").split(",");
const faenge = [];
for (const t of teile) {
  faenge.push(Number(t));
}
let summe = 0;
let bester = 0;
for (let i = 0; i < faenge.length; i++) {
  summe += faenge[i];
  if (faenge[i] > faenge[bester]) {
    bester = i;
  }
}
console.log(`Tage: ${faenge.length}`);
console.log(`Summe: ${summe}`);
console.log(`Bester Tag: ${bester + 1} mit ${faenge[bester]}`);
console.log(`Schnitt: ${(summe / faenge.length).toFixed(1)}`);
