const woerter = prompt("Bestellung? ").split(" ");
const zaehler = {};
for (const wort of woerter) {
  if (wort in zaehler) {
    zaehler[wort]++;
  } else {
    zaehler[wort] = 1;
  }
}
for (const wort in zaehler) {
  console.log(`${wort}: ${zaehler[wort]}`);
}
