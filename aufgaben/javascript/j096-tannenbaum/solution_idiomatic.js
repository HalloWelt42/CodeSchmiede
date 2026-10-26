const hoehe = Number(prompt("Höhe? "));
for (let z = 1; z <= hoehe; z++) {
  let zeile = "";
  for (let i = 0; i < hoehe - z; i++) {
    zeile += " ";
  }
  for (let i = 0; i < 2 * z - 1; i++) {
    zeile += "*";
  }
  console.log(zeile);
}
