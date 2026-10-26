const preise = prompt("Preise? ").split(",").map(Number);
console.log(`Auf: ${preise.slice().sort((a, b) => a - b).join(", ")}`);
console.log(`Ab: ${preise.slice().sort((a, b) => b - a).join(", ")}`);
console.log(`Original: ${preise.join(", ")}`);
