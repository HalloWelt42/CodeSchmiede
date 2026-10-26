const tag = prompt("Tag? ");
switch (tag) {
  case "Montag":
  case "Dienstag":
    console.log("Ruhetag");
    break;
  case "Mittwoch":
    console.log("Matjes");
    break;
  case "Freitag":
    console.log("Bratfisch");
    break;
  default:
    console.log("Heringsbrötchen");
}
