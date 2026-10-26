class Scholle {
  constructor(breite, laenge) {
    this.breite = breite;
    this.laenge = laenge;
  }
  get flaeche() {
    return this.breite * this.laenge;
  }
  get umfang() {
    return 2 * (this.breite + this.laenge);
  }
}
const s = new Scholle(3, 4);
console.log("Fläche:", s.flaeche);
console.log("Umfang:", s.umfang);
s.breite = 5;
console.log("Fläche:", s.flaeche);
