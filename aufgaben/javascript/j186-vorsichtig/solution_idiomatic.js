const kunden = [
  { name: "Pia", karte: { stempel: 3 } },
  { name: "Ole" },
  { name: "Ida", karte: { stempel: 0 } },
];
for (const { name, karte } of kunden) {
  console.log(`${name}: ${karte?.stempel ?? "keine Karte"}`);
}
