const name = prompt("Name? ");
try {
  console.log(`MOIN, ${name.toUpperCase()}!`);
} catch (fehler) {
  console.log("Kein Name, kein Gruß");
}
