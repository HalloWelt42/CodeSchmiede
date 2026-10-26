// Rahmen der Programm-Aufgaben in JavaScript, Gegenstück zum Python-Rahmen in programm_pruefer.py.
//
// Jeder Fall läuft in einem frischen Kontext mit eigener Eingabe: prompt(frage) schreibt die Frage wie input() in
// Python ohne Zeilenumbruch in die Ausgabe und liefert die nächste Eingabezeile (null, wenn keine mehr da ist),
// console schreibt in die Ausgabe des Falls. Ein Fall ist fertig, wenn auch seine Zeitgeber und Versprechen erledigt
// sind. Die Platzhalter __...__ ersetzt programm_pruefer.py durch JSON-Werte, den Code zuletzt.
(async () => {
  const vm = require('node:vm');
  const util = require('node:util');
  const CODE = __CODE__;
  const FAELLE = __FAELLE__;
  const DATEI = __DATEI__;
  const MARKE = __MARKE__;

  const fehlertext = (e) => {
    const name = e && e.name ? e.name : 'Error';
    const text = e && e.message !== undefined ? e.message : String(e);
    return text ? `${name}: ${text}` : name;
  };

  let skript = null;
  let syntax = null;
  try {
    skript = new vm.Script(CODE, { filename: DATEI });
  } catch (e) {
    const m = String(e && e.stack).match(new RegExp(DATEI.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ':(\\d+)'));
    syntax = fehlertext(e) + (m ? ` (Zeile ${m[1]})` : '');
  }

  /** Fehler außerhalb des synchronen Laufs (Rückrufe, Versprechen) gehören zum gerade laufenden Fall */
  let melden = () => {};
  process.on('uncaughtException', (e) => melden(e));
  process.on('unhandledRejection', (e) => melden(e));

  function fall(eingabe) {
    return new Promise((fertig) => {
      const teile = [];
      const zeilen = [...eingabe];
      const offen = new Set();
      let fehler = null;
      let abgeschlossen = false;
      const schreib = (text) => teile.push(text);
      melden = (e) => {
        if (fehler === null) fehler = fehlertext(e);
      };
      const abschliessen = () => {
        // erst nach den Versprechen dieses Durchgangs nachsehen, ob noch etwas aussteht
        setImmediate(() => {
          if (offen.size || abgeschlossen) return;
          abgeschlossen = true;
          fertig({ ausgabe: teile.join(''), fehler });
        });
      };
      const rueckruf = (f, argumente) => {
        try {
          f(...argumente);
        } catch (e) {
          melden(e);
        }
      };
      const konsole = {};
      for (const art of ['log', 'info', 'debug', 'warn', 'error']) konsole[art] = (...x) => schreib(util.format(...x) + '\n');
      const kontext = vm.createContext({
        console: konsole,
        prompt: (frage) => {
          if (frage !== undefined) schreib(String(frage));
          return zeilen.length ? zeilen.shift() : null;
        },
        setTimeout: (f, ms, ...argumente) => {
          const t = setTimeout(() => {
            offen.delete(t);
            rueckruf(f, argumente);
            abschliessen();
          }, ms);
          offen.add(t);
          return t;
        },
        clearTimeout: (t) => {
          clearTimeout(t);
          offen.delete(t);
          abschliessen();
        },
        setInterval: (f, ms, ...argumente) => {
          const t = setInterval(() => rueckruf(f, argumente), ms);
          offen.add(t);
          return t;
        },
        clearInterval: (t) => {
          clearInterval(t);
          offen.delete(t);
          abschliessen();
        },
      });
      try {
        skript.runInContext(kontext);
      } catch (e) {
        melden(e);
      }
      abschliessen();
    });
  }

  const ergebnisse = [];
  for (const eingabe of FAELLE) {
    ergebnisse.push(skript ? await fall(eingabe) : { ausgabe: '', fehler: syntax });
  }
  process.stdout.write('\n' + MARKE + '\n' + JSON.stringify(ergebnisse) + '\n');
  process.exit(0);
})();
