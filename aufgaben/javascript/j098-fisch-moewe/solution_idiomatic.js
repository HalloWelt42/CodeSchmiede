const bis = Number(prompt("Bis? "));
for (let i = 1; i <= bis; i++) {
  if (i % 7 === 0) {
    continue;
  }
  if (i % 3 === 0 && i % 5 === 0) {
    console.log("Fischmöwe");
  } else if (i % 3 === 0) {
    console.log("Fisch");
  } else if (i % 5 === 0) {
    console.log("Möwe");
  } else {
    console.log(i);
  }
}
