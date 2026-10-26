const faenge = [4, 9, 2, 7, 5, 8, 6];
let summe = 0;
for (const f of faenge) {
  summe += f;
}
console.log("Summe:", summe);
console.log("Schnitt:", (summe / faenge.length).toFixed(1));
