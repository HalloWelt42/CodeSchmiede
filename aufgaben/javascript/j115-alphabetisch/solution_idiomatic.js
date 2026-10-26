const namen = prompt("Namen? ").split(",");
const sortiert = namen.slice().sort();
console.log(`Sortiert: ${sortiert.join(", ")}`);
console.log(`Rückwärts: ${sortiert.slice().reverse().join(", ")}`);
console.log(`Original: ${namen.join(", ")}`);
