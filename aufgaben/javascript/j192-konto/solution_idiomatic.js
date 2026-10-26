class Konto {
  constructor() {
    this.stand = 0;
  }
  einzahlen(betrag) {
    this.stand += betrag;
  }
  abheben(betrag) {
    if (betrag > this.stand) {
      throw new Error("Zu wenig Geld");
    }
    this.stand -= betrag;
  }
}
const k = new Konto();
k.einzahlen(20);
k.abheben(5);
console.log(`Stand: ${k.stand.toFixed(2)}`);
try {
  k.abheben(100);
} catch (fehler) {
  console.log(`Abgelehnt: ${fehler.message}`);
}
console.log(`Stand: ${k.stand.toFixed(2)}`);
