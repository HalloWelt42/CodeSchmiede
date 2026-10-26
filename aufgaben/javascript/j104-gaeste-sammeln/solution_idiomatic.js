const gaeste = [];
while (true) {
  const name = prompt("Gast? ");
  if (!name) {
    break;
  }
  gaeste.push(name);
}
console.log(`${gaeste.length} Gäste: ${gaeste.join(", ")}`);
