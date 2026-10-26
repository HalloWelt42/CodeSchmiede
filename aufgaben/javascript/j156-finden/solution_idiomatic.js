const karte = [
  { name: "Fischsuppe", preis: 4.5 },
  { name: "Heringsbrötchen", preis: 2.5 },
  { name: "Limonade", preis: 1.75 },
];
console.log("Erstes unter 3 Euro:", karte.find(g => g.preis < 3).name);
console.log("Etwas über 8 Euro:", karte.some(g => g.preis > 8));
console.log("Alles unter 10 Euro:", karte.every(g => g.preis < 10));
