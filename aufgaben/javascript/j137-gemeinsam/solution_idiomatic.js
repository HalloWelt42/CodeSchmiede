const erster = new Set(prompt("Erster Tag? ").split(","));
const zweiter = new Set(prompt("Zweiter Tag? ").split(","));
const beide = [];
for (const name of erster) {
  if (zweiter.has(name)) {
    beide.push(name);
  }
}
const neu = [];
for (const name of zweiter) {
  if (!erster.has(name)) {
    neu.push(name);
  }
}
console.log(`Beide Tage: ${beide.join(", ")}`);
console.log(`Nur am zweiten: ${neu.join(", ")}`);
