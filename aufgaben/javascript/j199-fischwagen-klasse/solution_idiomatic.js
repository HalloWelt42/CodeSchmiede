class Kasse {
  constructor(wagen) {
    this.wagen = wagen;
    this.karte = new Map([
      ["Heringsbrötchen", 2.5],
      ["Limonade", 1.75],
      ["Fischsuppe", 4.5],
    ]);
    this.gutscheine = new Map([
      ["FISCH5", 5],
      ["HERING2", 2],
    ]);
    this.besuche = new Map();
    this.verkauft = new Map();
    for (const ware of this.karte.keys()) {
      this.verkauft.set(ware, 0);
    }
    this.jeKunde = new Map();
    this.umsatz = 0;
    this.naechsteNummer = 1;
  }

  static euro(betrag) {
    return `${betrag.toFixed(2)} Euro`;
  }

  static rabattSatz(summe) {
    if (summe >= 40) {
      return 15;
    }
    if (summe >= 20) {
      return 10;
    }
    return 0;
  }

  static stempelkarte(summe) {
    const stempel = Math.min(5, Math.floor(summe / 10));
    let text = "";
    for (let i = 0; i < 5; i++) {
      text += i < stempel ? "[*]" : "[ ]";
    }
    return text;
  }

  static liesAnzahl(text) {
    if (text === null) {
      throw new Error("keine Eingabe");
    }
    const zahl = Number(text);
    if (text.trim() === "" || !Number.isInteger(zahl)) {
      throw new Error(`"${text}" ist keine Zahl`);
    }
    if (zahl < 0) {
      throw new RangeError(`${zahl} ist weniger als nichts`);
    }
    return zahl;
  }

  get bons() {
    return this.naechsteNummer - 1;
  }

  anzahlenAbfragen() {
    const anzahlen = new Map();
    for (const ware of this.karte.keys()) {
      while (true) {
        const text = prompt(`${ware}? `);
        try {
          anzahlen.set(ware, Kasse.liesAnzahl(text));
          break;
        } catch (fehler) {
          console.log(`Ungültig: ${fehler.message}`);
          if (text === null) {
            anzahlen.set(ware, 0);
            break;
          }
        }
      }
    }
    return anzahlen;
  }

  gutscheinAbfragen() {
    const code = prompt("Gutschein? ");
    if (!code) {
      return 0;
    }
    const abzug = this.gutscheine.get(code) ?? 0;
    if (abzug === 0) {
      console.log("Gutschein unbekannt");
    }
    return abzug;
  }

  bonDrucken({ kunde, anzahlen, abzug = 0 }) {
    let summe = 0;
    console.log(`Kassenbon Nr. ${this.naechsteNummer} für ${kunde}`);
    this.naechsteNummer++;
    for (const [ware, preis] of this.karte) {
      const anzahl = anzahlen.get(ware);
      if (anzahl === 0) {
        continue;
      }
      console.log(`${anzahl} x ${ware}: ${Kasse.euro(anzahl * preis)}`);
      summe += anzahl * preis;
    }
    if (anzahlen.get("Heringsbrötchen") >= 3 && anzahlen.get("Limonade") === 0) {
      console.log("1 x Limonade: gratis");
    }
    console.log("=".repeat(30));
    const satz = Kasse.rabattSatz(summe);
    if (satz > 0) {
      const rabatt = (summe * satz) / 100;
      console.log(`Rabatt ${satz} %: -${Kasse.euro(rabatt)}`);
      summe -= rabatt;
    }
    if (abzug > 0) {
      const weg = Math.min(abzug, summe);
      console.log(`Gutschein: -${Kasse.euro(weg)}`);
      summe -= weg;
    }
    console.log(`Summe: ${Kasse.euro(summe)}`);
    console.log(`Stempel: ${Kasse.stempelkarte(summe)}`);
    return summe;
  }

  bedienen(kunde) {
    if (this.besuche.has(kunde)) {
      console.log(`Willkommen zurück, ${kunde}!`);
    }
    this.besuche.set(kunde, (this.besuche.get(kunde) ?? 0) + 1);
    const anzahlen = this.anzahlenAbfragen();
    const abzug = this.gutscheinAbfragen();
    for (const [ware, anzahl] of anzahlen) {
      this.verkauft.set(ware, this.verkauft.get(ware) + anzahl);
    }
    const summe = this.bonDrucken({ kunde, anzahlen, abzug });
    this.umsatz += summe;
    this.jeKunde.set(kunde, (this.jeKunde.get(kunde) ?? 0) + summe);
  }

  tagesabschluss() {
    const besuche = [...this.besuche.values()].reduce((s, n) => s + n, 0);
    console.log(`Besuche heute: ${besuche}`);
    console.log(`Verschiedene Kunden: ${this.besuche.size}`);
    for (const [name, n] of this.besuche) {
      console.log(`${name}: ${n} ${n === 1 ? "Besuch" : "Besuche"}`);
    }
    const nie = [];
    for (const [ware, n] of this.verkauft) {
      if (n === 0) {
        nie.push(ware);
      } else {
        console.log(`${ware}: ${n} verkauft`);
      }
    }
    if (nie.length > 0) {
      console.log(`Nicht verkauft: ${nie.join(", ")}`);
    }
    const rangliste = [...this.jeKunde].map(([name, betrag]) => ({ name, betrag }));
    if (rangliste.length > 0) {
      rangliste.sort((a, b) => b.betrag - a.betrag);
      console.log(`Rangliste: ${rangliste.map((k) => `${k.name} ${k.betrag.toFixed(2)}`).join(", ")}`);
    }
    console.log(`Tagesumsatz: ${Kasse.euro(this.umsatz)}`);
    console.log(`Bons heute: ${this.bons}`);
  }
}

const kasse = new Kasse("Zum frostigen Hering");
console.log(`*** ${kasse.wagen.toUpperCase()} ***`);
while (true) {
  const kunde = prompt("Kunde? ");
  if (kunde === null || kunde === "") {
    break;
  }
  kasse.bedienen(kunde);
}
kasse.tagesabschluss();
