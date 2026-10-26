class Fisch {
  static anzahl = 0;
  constructor(art) {
    this.art = art;
    Fisch.anzahl++;
  }
  static bericht() {
    return `Gebaut: ${Fisch.anzahl} Fische`;
  }
}
new Fisch("Hering");
new Fisch("Aal");
new Fisch("Butt");
console.log(Fisch.bericht());
