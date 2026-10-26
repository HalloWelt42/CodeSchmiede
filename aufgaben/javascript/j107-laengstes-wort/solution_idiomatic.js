const woerter = prompt("Satz? ").split(" ");
let laengstes = woerter[0];
for (const wort of woerter) {
  if (wort.length > laengstes.length) {
    laengstes = wort;
  }
}
console.log(`Wörter: ${woerter.length}`);
console.log(`Längstes: ${laengstes}`);
