const buch = [];
while (true) {
  const eintrag = prompt("Fang? ");
  if (!eintrag) {
    break;
  }
  const teile = eintrag.split(" ");
  buch.push({ name: teile[0], anzahl: Number(teile[1]) });
}
console.log(`Gesamt: ${buch.reduce((s, f) => s + f.anzahl, 0)}`);
const grosse = buch.filter(f => f.anzahl >= 10).map(f => `${f.name} ${f.anzahl}`);
console.log(`Große Fänge: ${grosse.length > 0 ? grosse.join(", ") : "keine"}`);
const rang = buch.slice().sort((a, b) => b.anzahl - a.anzahl).map(f => f.name);
console.log(`Rangliste: ${rang.join(", ")}`);
console.log(`Jemand ohne Fang: ${buch.some(f => f.anzahl === 0) ? "ja" : "nein"}`);
