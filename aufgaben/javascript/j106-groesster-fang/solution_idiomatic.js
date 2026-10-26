const faenge = [4, 9, 2, 7, 5];
let bester = 0;
for (let i = 1; i < faenge.length; i++) {
  if (faenge[i] > faenge[bester]) {
    bester = i;
  }
}
console.log(`Bester Tag: ${bester + 1} mit ${faenge[bester]} Fischen`);
