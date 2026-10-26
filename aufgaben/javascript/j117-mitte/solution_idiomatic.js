const karte = ["Hering", "Aal", "Makrele", "Dorsch"];
const mitte = Math.floor(karte.length / 2);
karte.splice(mitte, 0, "Fischsuppe");
console.log(karte.join(", "));
