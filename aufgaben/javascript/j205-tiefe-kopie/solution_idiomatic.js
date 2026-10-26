const kunde = { name: "Pia", lieblinge: ["Hering"] };
const kopie = JSON.parse(JSON.stringify(kunde));
kopie.lieblinge.push("Aal");
console.log(`Original: ${kunde.lieblinge.join(", ")}`);
console.log(`Kopie: ${kopie.lieblinge.join(", ")}`);
