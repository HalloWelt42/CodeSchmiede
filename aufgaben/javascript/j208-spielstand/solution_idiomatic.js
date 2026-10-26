let stand;
try {
  stand = JSON.parse(prompt("Spielstand? "));
  if (typeof stand !== "object" || stand === null || Array.isArray(stand)) {
    throw new TypeError("kein Spielstand");
  }
} catch (fehler) {
  console.log("Neues Spiel");
  stand = { name: "Pit", punkte: 0, fische: [] };
}
while (true) {
  const befehl = prompt("Befehl? ");
  if (!befehl) {
    break;
  }
  const [was, wert] = befehl.split(" ");
  if (was === "punkte") {
    stand.punkte += Number(wert);
  } else if (was === "fisch") {
    stand.fische.push(wert);
  } else {
    console.log(`Unbekannt: ${was}`);
  }
}
console.log(`${stand.name} hat ${stand.punkte} Punkte und ${stand.fische.length} Fische`);
console.log(JSON.stringify(stand));
