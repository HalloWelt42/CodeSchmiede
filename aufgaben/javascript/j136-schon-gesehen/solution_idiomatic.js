const gesehen = new Set();
while (true) {
  const fisch = prompt("Fisch? ");
  if (!fisch) {
    break;
  }
  if (gesehen.has(fisch)) {
    console.log("Kenne ich schon");
  } else {
    gesehen.add(fisch);
    console.log("Neu!");
  }
}
console.log(`Verschiedene: ${gesehen.size}`);
