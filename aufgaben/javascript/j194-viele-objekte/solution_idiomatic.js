class Pinguin {
  constructor(name, alter) {
    this.name = name;
    this.alter = alter;
  }
  vorstellen() {
    return `${this.name} (${this.alter})`;
  }
}
const kolonie = [];
while (true) {
  const zeile = prompt("Pinguin? ");
  if (!zeile) {
    break;
  }
  const [name, alter] = zeile.split(" ");
  kolonie.push(new Pinguin(name, Number(alter)));
}
for (const p of kolonie) {
  console.log(p.vorstellen());
}
if (kolonie.length > 0) {
  const aeltester = kolonie.reduce((a, b) => (b.alter > a.alter ? b : a));
  console.log(`Ältester: ${aeltester.name}`);
}
