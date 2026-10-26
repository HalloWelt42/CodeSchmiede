const wort = prompt("Wort? ");
let ergebnis = "";
for (let i = wort.length - 1; i >= 0; i--) {
  ergebnis += wort[i];
}
console.log(ergebnis);
