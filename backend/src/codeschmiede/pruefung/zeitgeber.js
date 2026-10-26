// Zeitgeber mit eigener Uhr für die Läufe in der Sandbox (eingesetzt in programm_rahmen.js und kurs/aufzeichner.js).
//
// setTimeout und setInterval warten nicht wirklich: Ihre Rückrufe kommen in eine Liste mit der Zeit, zu der sie dran
// wären. Ist der übrige Code fertig, arbeitet abarbeiten() die Liste in der Reihenfolge dieser Zeiten ab und erledigt
// vor jedem Rückruf die anstehenden Versprechen. So stimmt die Reihenfolge immer, auch wenn ein Debugger den Lauf
// anhält oder der Rechner ausgelastet ist, und niemand wartet echte Millisekunden. Ein Fehler in einem Rückruf beendet
// das Abarbeiten wie in Node das Programm.
function zeitgeberBauen(beimFehler, hoechstens = 10000) {
  const naechsteRunde = () => new Promise((weiter) => setImmediate(weiter));
  let liste = [];
  let jetzt = 0;
  let nummer = 0;
  let abgebrochen = false;

  function planen(rueckruf, ms, argumente, intervall) {
    const id = ++nummer;
    const warten = Math.max(0, Number(ms) || 0);
    liste.push({ id, folge: id, zeit: jetzt + warten, rueckruf, argumente, intervall: intervall ? Math.max(1, warten) : null });
    return id;
  }
  function entfernen(id) {
    liste = liste.filter((t) => t.id !== id);
  }

  return {
    setTimeout: (rueckruf, ms, ...argumente) => planen(rueckruf, ms, argumente, false),
    setInterval: (rueckruf, ms, ...argumente) => planen(rueckruf, ms, argumente, true),
    clearTimeout: entfernen,
    clearInterval: entfernen,
    async abarbeiten() {
      let erledigt = 0;
      for (;;) {
        await naechsteRunde();
        if (abgebrochen || liste.length === 0) {
          return;
        }
        if (++erledigt > hoechstens) {
          beimFehler(new RangeError(`Mehr als ${hoechstens} Zeitgeber-Rückrufe, läuft da ein Intervall ohne Ende?`));
          return;
        }
        liste.sort((a, b) => a.zeit - b.zeit || a.folge - b.folge);
        const t = liste.shift();
        jetzt = t.zeit;
        if (t.intervall !== null) {
          liste.push({ ...t, zeit: jetzt + t.intervall, folge: ++nummer });
        }
        try {
          t.rueckruf(...t.argumente);
        } catch (fehler) {
          abgebrochen = true;
          beimFehler(fehler);
        }
      }
    },
  };
}
