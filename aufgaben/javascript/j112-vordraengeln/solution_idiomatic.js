const schlange = ["Pia", "Ole"];
schlange.unshift("Bo");
const bedient = schlange.shift();
console.log("Bedient:", bedient);
console.log("Wartet noch:", schlange.join(", "));
