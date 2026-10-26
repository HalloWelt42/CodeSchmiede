function automatBauen(voll) {
  const stempel = new Map();
  return {
    stempeln: (name) => {
      let stand = (stempel.get(name) || 0) + 1;
      if (stand === voll) {
        stand = 0;
        stempel.set(name, stand);
        return `${name}: Karte voll, ein Brötchen gratis!`;
      }
      stempel.set(name, stand);
      return `${name}: ${stand} von ${voll}`;
    },
    karten: () => stempel.size,
  };
}
const automat = automatBauen(5);
while (true) {
  const name = prompt("Wer? ");
  if (!name) {
    break;
  }
  console.log(automat.stempeln(name));
}
console.log(`Karten: ${automat.karten()}`);
