function gruss(name = "Gast") {
  return `Moin, ${name}!`;
}
const name = prompt("Name? ");
console.log(name ? gruss(name) : gruss());
