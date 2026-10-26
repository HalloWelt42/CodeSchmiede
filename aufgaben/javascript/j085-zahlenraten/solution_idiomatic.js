const geheim = 42;
let versuche = 0;
while (true) {
  const tipp = Number(prompt("Tipp? "));
  versuche++;
  if (tipp < geheim) {
    console.log("zu klein");
  } else if (tipp > geheim) {
    console.log("zu groß");
  } else {
    break;
  }
}
console.log(`Richtig nach ${versuche} Versuchen!`);
