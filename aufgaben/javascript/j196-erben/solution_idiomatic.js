class Gericht {
  constructor(name, preis) {
    this.name = name;
    this.preis = preis;
  }
  zeile() {
    return `${this.name}: ${this.preis.toFixed(2)} Euro`;
  }
}
class Suppe extends Gericht {
  constructor(name, preis, scharf) {
    super(name, preis);
    this.scharf = scharf;
  }
  zeile() {
    return super.zeile() + (this.scharf ? " (scharf)" : "");
  }
}
const karte = [new Gericht("Heringsbrötchen", 2.5), new Suppe("Fischsuppe", 4.5, true), new Suppe("Kartoffelsuppe", 3.9, false)];
for (const g of karte) {
  console.log(g.zeile());
}
