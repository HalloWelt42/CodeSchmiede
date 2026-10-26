class Fisch {
  constructor(name, art, gramm) {
    this.name = name;
    this.art = art;
    this.gramm = gramm;
  }
  beschreibung() {
    return `${this.name} der ${this.art} (${this.gramm} g)`;
  }
}

class Aquarium {
  constructor() {
    this.fische = [];
  }
  static ausZeile(zeile) {
    const [name, art, gramm] = zeile.split(" ");
    return new Fisch(name, art, Number(gramm));
  }
  einsetzen(fisch) {
    this.fische.push(fisch);
  }
  get schwerster() {
    return this.fische.reduce((a, b) => (b.gramm > a.gramm ? b : a));
  }
  get gesamtKilo() {
    return this.fische.reduce((s, f) => s + f.gramm, 0) / 1000;
  }
}

const becken = new Aquarium();
while (true) {
  const zeile = prompt("Fisch? ");
  if (!zeile) {
    break;
  }
  becken.einsetzen(Aquarium.ausZeile(zeile));
}
for (const f of becken.fische) {
  console.log(f.beschreibung());
}
if (becken.fische.length > 0) {
  console.log(`Schwerster: ${becken.schwerster.name}`);
  console.log(`Gesamt: ${becken.gesamtKilo.toFixed(1)} kg`);
}
console.log(`Fische im Becken: ${becken.fische.length}`);
