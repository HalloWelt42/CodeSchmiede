const preise = [2, 3, 4];
const rabatte = [1, 1, 1];
let summe = 0;
for (const p of preise) {
  summe += p;
}
if (rabatte.length > 0) {
  let summe = 0;
  for (const r of rabatte) {
    summe += r;
  }
  console.log("Summe der Rabatte:", summe);
}
console.log("Summe der Preise:", summe);
