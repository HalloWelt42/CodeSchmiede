const n = Number(prompt("Bis? "));
let i = 1;
let summe = 0;
while (i <= n) {
  summe += i;
  i++;
}
console.log(`Summe 1 bis ${n}: ${summe}`);
