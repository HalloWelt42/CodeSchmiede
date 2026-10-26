const a = Number(prompt("Erstes? "));
const b = Number(prompt("Zweites? "));
console.log(`Summe: ${(a + b).toFixed(1)}`);
console.log("Erstes keine Zahl:", Number.isNaN(a));
console.log("kg: " + String(b));
