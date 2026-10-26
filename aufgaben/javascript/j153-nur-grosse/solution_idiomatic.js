const faenge = prompt("Fänge? ").split(",").map(Number);
console.log(faenge.filter(f => f >= 5));
