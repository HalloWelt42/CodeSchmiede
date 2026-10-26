const ziel = Number(prompt("Ziel? "));
let fische = 1;
let tage = 0;
while (fische < ziel) {
  fische *= 2;
  tage++;
}
console.log(`Nach ${tage} Tagen: ${fische} Fische`);
