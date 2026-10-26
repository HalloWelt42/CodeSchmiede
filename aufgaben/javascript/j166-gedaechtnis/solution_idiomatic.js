function teuer(n) {
  return n * n;
}
function mitGedaechtnis(f) {
  const gemerkt = new Map();
  return (n) => {
    if (gemerkt.has(n)) {
      return `${gemerkt.get(n)} (gemerkt)`;
    }
    const ergebnis = f(n);
    gemerkt.set(n, ergebnis);
    return `${ergebnis}`;
  };
}
const schnell = mitGedaechtnis(teuer);
while (true) {
  const eingabe = prompt("Zahl? ");
  if (eingabe === null) {
    break;
  }
  console.log(schnell(Number(eingabe)));
}
