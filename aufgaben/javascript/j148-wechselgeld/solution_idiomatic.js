function euro(cent) {
  return `${(cent / 100).toFixed(2)} Euro`;
}

function zerlegen(cent) {
  const werte = [200, 100, 50, 20, 10, 5, 2, 1];
  const namen = ["2 Euro", "1 Euro", "50 Cent", "20 Cent", "10 Cent", "5 Cent", "2 Cent", "1 Cent"];
  const teile = [];
  for (let i = 0; i < werte.length; i++) {
    const anzahl = Math.floor(cent / werte[i]);
    if (anzahl > 0) {
      teile.push(`${anzahl} x ${namen[i]}`);
      cent -= anzahl * werte[i];
    }
  }
  return teile.length > 0 ? teile.join(", ") : "passt genau";
}

const preis = Math.round(Number(prompt("Preis? ")) * 100);
const bezahlt = Math.round(Number(prompt("Bezahlt? ")) * 100);
const rueckgeld = bezahlt - preis;
if (rueckgeld < 0) {
  console.log(`Es fehlen noch ${euro(-rueckgeld)}`);
} else {
  console.log(`Rückgeld: ${euro(rueckgeld)}`);
  console.log(zerlegen(rueckgeld));
}
