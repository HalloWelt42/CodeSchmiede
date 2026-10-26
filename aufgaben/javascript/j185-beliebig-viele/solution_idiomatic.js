const idasPreise = [2.5, 4.5, 1.75, 4.75];
function bon(kunde, ...preise) {
  const summe = preise.reduce((s, p) => s + p, 0);
  return `${kunde}: ${preise.length} Posten, ${summe.toFixed(2)} Euro`;
}
console.log(bon("Pia", 2.5, 4.5, 1.75));
console.log(bon("Ole"));
console.log(bon("Ida", ...idasPreise));
