let aufDemHerd = 0;
let hoechstens = 0;
function kochen(ms) {
  aufDemHerd++;
  hoechstens = Math.max(hoechstens, aufDemHerd);
  return new Promise((erfuellen) => {
    setTimeout(() => {
      aufDemHerd--;
      erfuellen();
    }, ms);
  });
}
async function vergleich() {
  for (const ms of [5, 10, 5]) {
    await kochen(ms);
  }
  console.log(`Nacheinander: höchstens ${hoechstens} auf dem Herd`);
  hoechstens = 0;
  await Promise.all([kochen(5), kochen(10), kochen(5)]);
  console.log(`Zugleich: höchstens ${hoechstens} auf dem Herd`);
}
vergleich();
