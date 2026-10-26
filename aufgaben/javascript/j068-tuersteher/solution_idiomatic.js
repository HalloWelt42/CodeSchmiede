const alter = Number(prompt("Alter? "));
const einladung = prompt("Einladung? ") === "ja";
const fisch = prompt("Fisch? ") === "ja";
const altGenug = alter >= 3;
const mitbringsel = einladung || fisch;
console.log("Alt genug:", altGenug);
console.log("Einladung oder Fisch:", mitbringsel);
console.log("Darf rein:", altGenug && mitbringsel);
