const preise = { Hering: 2.5, Aal: 5, Makrele: 3.2 };
for (const fisch in preise) {
  console.log(`${fisch}: ${preise[fisch].toFixed(2)} Euro`);
}
console.log(`${Object.keys(preise).length} Sorten`);
