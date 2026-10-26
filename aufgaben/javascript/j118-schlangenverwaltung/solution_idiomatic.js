const schlange = [];
while (true) {
  const befehl = prompt("Befehl? ");
  if (!befehl) {
    break;
  }
  const teile = befehl.split(" ");
  switch (teile[0]) {
    case "an":
      schlange.push(teile[1]);
      break;
    case "vor":
      schlange.unshift(teile[1]);
      break;
    case "weiter":
      console.log(schlange.length > 0 ? `Bedient: ${schlange.shift()}` : "Niemand da");
      break;
    case "weg": {
      const stelle = schlange.indexOf(teile[1]);
      if (stelle === -1) {
        console.log(`${teile[1]} steht nicht an`);
      } else {
        schlange.splice(stelle, 1);
      }
      break;
    }
    default:
      console.log("Unbekannt");
  }
}
console.log("Schlange:", schlange);
