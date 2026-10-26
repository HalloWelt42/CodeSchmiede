let wurf;
do {
  wurf = Number(prompt("Würfel? "));
  if (wurf < 1 || wurf > 6) {
    console.log("Nur 1 bis 6!");
  }
} while (wurf < 1 || wurf > 6);
console.log("Gewürfelt:", wurf);
