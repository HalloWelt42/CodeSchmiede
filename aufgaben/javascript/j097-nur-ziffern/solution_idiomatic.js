const nummer = prompt("Nummer? ");
let ziffern = "";
for (const z of nummer) {
  if (!"0123456789".includes(z)) {
    continue;
  }
  ziffern += z;
}
console.log(ziffern);
