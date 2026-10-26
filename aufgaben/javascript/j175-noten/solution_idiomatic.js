const note = Number(prompt("Note? "));
try {
  if (!Number.isInteger(note)) {
    throw new TypeError("Nur ganze Noten");
  }
  if (note < 1 || note > 6) {
    throw new RangeError(`${note} gibt es nicht`);
  }
  console.log(`Note ${note} eingetragen`);
} catch (fehler) {
  if (fehler.name === "TypeError") {
    console.log(`Falsche Art: ${fehler.message}`);
  } else {
    console.log(`Außerhalb: ${fehler.message}`);
  }
}
