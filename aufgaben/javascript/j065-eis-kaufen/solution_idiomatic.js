const geld = Number(prompt("Geld? "));
const stunde = Number(prompt("Stunde? "));
const offen = stunde >= 10 && stunde < 18;
console.log("Eis:", geld >= 2 && offen);
