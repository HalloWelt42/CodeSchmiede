function groessere(a, b) {
  if (a > b) {
    return a;
  }
  return b;
}
const a = Number(prompt("Pia? "));
const b = Number(prompt("Paul? "));
const c = Number(prompt("Pit? "));
console.log("Größter Fang:", groessere(groessere(a, b), c));
