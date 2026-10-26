let zahl = Number(prompt("Ab? "));
const takt = setInterval(() => {
  if (zahl === 0) {
    console.log("Start!");
    clearInterval(takt);
  } else {
    console.log(zahl);
    zahl--;
  }
}, 10);
