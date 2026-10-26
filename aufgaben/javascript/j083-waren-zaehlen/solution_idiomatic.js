let anzahl = 0;
while (true) {
  const ware = prompt("Ware? ");
  if (ware === null || ware === "fertig") {
    break;
  }
  anzahl++;
}
console.log(`${anzahl} Waren`);
