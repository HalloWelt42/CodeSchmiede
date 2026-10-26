const buch = new Map();
while (true) {
  const eintrag = prompt("Eintrag? ");
  if (!eintrag) {
    break;
  }
  const teile = eintrag.split(" ");
  buch.set(teile[0], teile[1]);
}
console.log(`Einträge: ${buch.size}`);
const gesucht = prompt("Wen suchst du? ");
if (buch.has(gesucht)) {
  console.log(`${gesucht}: ${buch.get(gesucht)}`);
} else {
  console.log(`${gesucht} steht nicht drin`);
}
