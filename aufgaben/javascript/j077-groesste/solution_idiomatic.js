const a = Number(prompt("Pia? "));
const b = Number(prompt("Paul? "));
const c = Number(prompt("Pit? "));
let groesster;
if (a >= b && a >= c) {
  groesster = a;
} else if (b >= c) {
  groesster = b;
} else {
  groesster = c;
}
console.log("Größter Fang:", groesster);
