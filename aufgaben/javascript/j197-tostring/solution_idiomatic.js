class Bestellung {
  constructor(ware, anzahl, preis) {
    this.ware = ware;
    this.anzahl = anzahl;
    this.preis = preis;
  }
  toString() {
    return `${this.anzahl} x ${this.ware} für ${(this.anzahl * this.preis).toFixed(2)} Euro`;
  }
}
const anzahl = Number(prompt("Wie viele? "));
const bestellungen = [new Bestellung("Hering", anzahl, 2.5), new Bestellung("Suppe", 1, 4.5)];
for (const b of bestellungen) {
  console.log(`Bestellung: ${b}`);
}
