function istGerade(zahl) {
  return zahl % 2 === 0;
}
const bis = Number(prompt("Bis? "));
const gerade = [];
const ungerade = [];
for (let i = 1; i <= bis; i++) {
  if (istGerade(i)) {
    gerade.push(i);
  } else {
    ungerade.push(i);
  }
}
console.log(`Gerade: ${gerade.join(", ")}`);
console.log(`Ungerade: ${ungerade.join(", ")}`);
