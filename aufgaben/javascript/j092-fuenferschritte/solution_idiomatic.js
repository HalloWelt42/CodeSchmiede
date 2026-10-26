const bis = Number(prompt("Bis? "));
let zeile = "";
for (let i = 0; i <= bis; i += 5) {
  zeile += i === 0 ? `${i}` : ` ${i}`;
}
console.log(zeile);
