const sportarten = new Map();
const mitglieder = new Set();
const mehrfach = [];
while (true) {
  const anmeldung = prompt("Anmeldung? ");
  if (!anmeldung) {
    break;
  }
  const teile = anmeldung.split(" ");
  const name = teile[0];
  const sport = teile[1];
  if (mitglieder.has(name) && !mehrfach.includes(name)) {
    mehrfach.push(name);
  }
  mitglieder.add(name);
  sportarten.set(sport, (sportarten.get(sport) || 0) + 1);
}
for (const sport of sportarten.keys()) {
  console.log(`${sport}: ${sportarten.get(sport)}`);
}
console.log(`Mitglieder: ${mitglieder.size}`);
if (mehrfach.length > 0) {
  console.log(`Mehrfach dabei: ${mehrfach.join(", ")}`);
}
