// Aufzeichnung eines JavaScript-Laufs für den Kurs, Gegenstück zum Python-Aufzeichner in aufzeichnung.py.
//
// Der Nutzercode läuft im Hauptthread als Skript mit dem Dateinamen BEISPIEL. Ein Worker verbindet sich über den
// Inspector mit dem Hauptthread wie ein Debugger: er setzt an jede mögliche Haltestelle des Beispiels einen
// Haltepunkt und liest bei jedem Halt die Namen der Aufrufrahmen aus. Bibliotheken und dieser Rahmen selbst haben
// keine Haltepunkte und bleiben unsichtbar (kein Tiefendebugger). Rückrufe aus Zeitgebern und Versprechen werden
// mit aufgezeichnet; die Ergebnisse kommen, sobald nichts mehr zu tun ist.
//
// Die Platzhalter __...__ ersetzt aufzeichnung.py durch JSON-Werte. Alles steht in einer Funktion, damit kein Name
// dieses Rahmens neben den Namen des Beispiels im Speicher erscheint.
(() => {
  const BEISPIEL = __BEISPIEL__;
  const [MAX_SCHRITTE, MAX_TIEFE, MAX_ELEMENTE, MAX_ZEICHEN] = __GRENZEN__;
  const CODE = __CODE__;
  const EINGABE = __EINGABE__;
  const MARKE = __MARKE__;
  const HILFE = Symbol.for('codeschmiede.aufzeichnung');

  // ---------- Verfolger: läuft im Worker und hält den Hauptthread an jeder Stelle des Beispiels an ----------

  function verfolger() {
    const { parentPort, workerData } = require('node:worker_threads');
    const inspector = require('node:inspector');
    const sitzung = new inspector.Session();
    sitzung.connectToMainThread();
    const post = (methode, werte) => new Promise((ok, nein) => sitzung.post(methode, werte, (e, r) => (e ? nein(e) : ok(r))));
    const LESEN = `function (bauplan, ...bereiche) { return globalThis[Symbol.for('codeschmiede.aufzeichnung')].lesen(bauplan, bereiche); }`;
    const RAHMEN_BEREICHE = ['local', 'block', 'closure', 'catch'];

    const schritte = [];
    let skriptId = null;
    let haltestellenGesetzt = false;
    /** Zeilen des Beispiels: endet eine Funktion an einer schließenden Klammer, zählt die Zeile davor */
    let quelle = [];
    let gekuerzt = false;
    let fertig = false;
    /** Zeile, Rahmentiefe und Spalte des letzten Halts: seine Zeile ist fertig, sobald es woanders weitergeht */
    let vorige = null;

    sitzung.on('Debugger.scriptParsed', ({ params }) => {
      if (params.url === workerData.beispiel) skriptId = params.scriptId;
    });

    /** Bauplan für das Lesen: welche Bereiche zu welchem Rahmen gehören. Das Hauptprogramm hat die Namen der
     * obersten Ebene (global und script) und, wenn es selbst läuft, seine Blöcke; jede Funktion ihre eigenen. */
    function bauplan(rahmen) {
      const plan = [];
      const bereiche = [];
      const unten = rahmen[rahmen.length - 1];
      const untenIstModul = !unten.scopeChain.some((b) => b.type === 'local');
      const modul = { name: 'Modul', bereiche: [] };
      for (const b of [...unten.scopeChain].reverse()) {
        if (b.type === 'global' || b.type === 'script' || (untenIstModul && b.type === 'block')) {
          modul.bereiche.push({ nr: bereiche.length, global: b.type === 'global' });
          bereiche.push({ objectId: b.object.objectId });
        }
      }
      plan.push(modul);
      for (const f of [...rahmen].reverse()) {
        if (f === unten && untenIstModul) continue;
        const r = { name: f.functionName || '(anonym)', bereiche: [] };
        for (const b of [...f.scopeChain].reverse()) {
          if (!RAHMEN_BEREICHE.includes(b.type)) continue;
          r.bereiche.push({ nr: bereiche.length, global: false });
          bereiche.push({ objectId: b.object.objectId });
        }
        plan.push(r);
      }
      return { plan, bereiche };
    }

    async function festhalten(zeile, rahmen, rueckgabe) {
      const { plan, bereiche } = bauplan(rahmen);
      const r = await post('Runtime.callFunctionOn', {
        objectId: bereiche[0].objectId,
        functionDeclaration: LESEN,
        arguments: [{ value: plan }, ...bereiche],
        returnByValue: true,
      });
      const gelesen = r.result.value;
      const schritt = { zeile, rahmen: gelesen.rahmen, ausgabe: gelesen.ausgabe };
      // Ein Schritt, der nichts Neues zeigt (etwa Bedingung nach dem Hochzählen einer for-Schleife), entfällt
      const letzter = schritte[schritte.length - 1];
      if (!rueckgabe && !schritt.ausgabe && letzter && letzter.zeile === zeile && !letzter.rueckgabe
          && JSON.stringify(letzter.rahmen) === JSON.stringify(schritt.rahmen)) return;
      if (rueckgabe) {
        const w = await post('Runtime.callFunctionOn', {
          objectId: bereiche[0].objectId,
          functionDeclaration: `function (w) { return globalThis[Symbol.for('codeschmiede.aufzeichnung')].wert(w); }`,
          arguments: [rueckgabe.objectId ? { objectId: rueckgabe.objectId } : { value: rueckgabe.value, unserializableValue: rueckgabe.unserializableValue }],
          returnByValue: true,
        });
        schritt.rueckgabe = w.result.value;
      }
      schritte.push(schritt);
      if (schritte.length >= workerData.maxSchritte) {
        gekuerzt = true;
        await post('Debugger.setBreakpointsActive', { active: false });
      }
    }

    async function haltestellenSetzen() {
      haltestellenGesetzt = true;
      quelle = (await post('Debugger.getScriptSource', { scriptId: skriptId })).scriptSource.split('\n');
      const m = await post('Debugger.getPossibleBreakpoints', { start: { scriptId: skriptId, lineNumber: 0, columnNumber: 0 } });
      for (const stelle of m.locations) await post('Debugger.setBreakpoint', { location: stelle }).catch(() => {});
    }

    sitzung.on('Debugger.paused', async ({ params }) => {
      try {
        const rahmen = params.callFrames.filter((f) => f.location.scriptId === skriptId);
        const oben = rahmen[0];
        // Halt vor dem Start eines Skripts: ist es das Beispiel, kommen die Haltepunkte jetzt
        if (params.reason === 'instrumentation') {
          if (!haltestellenGesetzt && skriptId !== null && params.data && params.data.scriptId === skriptId) await haltestellenSetzen();
          return;
        }
        if (!oben || gekuerzt || fertig) return;
        const zeile = oben.location.lineNumber + 1;
        const tiefe = rahmen.length;
        const istFunktion = oben.scopeChain.some((b) => b.type === 'local');
        if (params.reason === 'exception' || params.reason === 'promiseRejection') {
          // Fehler: die Zeile, in der er entstand, mit dem Speicher in diesem Moment
          await festhalten(zeile, rahmen, null);
          vorige = null;
        } else if (oben.returnValue && istFunktion) {
          // Rückkehr aus einer Funktion: ihre zuletzt ausgeführte Zeile (nicht die schließende Klammer) mit dem
          // Rückgabewert, danach ist die Zeile des Aufrufers dran
          const schliesst = /^\s*}/.test(quelle[zeile - 1] || '');
          if (schliesst && vorige && vorige.tiefe === tiefe) {
            await festhalten(vorige.zeile, rahmen, oben.returnValue);
          } else {
            if (vorige && vorige.tiefe === tiefe && vorige.zeile !== zeile) await festhalten(vorige.zeile, rahmen, null);
            await festhalten(zeile, rahmen, oben.returnValue);
          }
          vorige = rahmen.length > 1 ? { zeile: rahmen[1].location.lineNumber + 1, tiefe: tiefe - 1, spalte: rahmen[1].location.columnNumber } : null;
        } else if (oben.returnValue) {
          // Ende des Hauptprogramms
          if (vorige) await festhalten(vorige.zeile, rahmen, null);
          vorige = null;
        } else {
          // Mehrere Halte in einer Zeile sind ein Schritt, solange es in ihr vorangeht; ein Sprung zurück an eine
          // frühere Stelle derselben Zeile ist ein neuer Durchgang (Schleife)
          const spalte = oben.location.columnNumber;
          const weiter = vorige && vorige.zeile === zeile && vorige.tiefe === tiefe && spalte > vorige.spalte;
          if (vorige && !weiter) await festhalten(vorige.zeile, rahmen, null);
          vorige = { zeile, tiefe, spalte };
        }
      } catch (e) {
        process._rawDebug('Aufzeichnung: ' + (e && e.message));
      } finally {
        await post('Debugger.resume').catch(() => {});
      }
    });

    (async () => {
      await post('Debugger.enable');
      await post('Debugger.setPauseOnExceptions', { state: 'all' });
      await post('Debugger.setInstrumentationBreakpoint', { instrumentation: 'beforeScriptExecution' });
      Atomics.store(workerData.bereit, 0, 1);
    })();

    parentPort.on('message', () => {
      fertig = true;
      // ohne Trennen wartet Node beim Beenden auf den Debugger
      sitzung.disconnect();
      parentPort.postMessage({ schritte, gekuerzt });
    });
  }

  // ---------- Hauptthread: Werte lesen, Ausgabe mitschreiben, Beispiel ausführen ----------

  const { Worker } = require('node:worker_threads');
  const vm = require('node:vm');
  const util = require('node:util');

  const neu = [];
  const alles = [];
  const schreib = (text) => { neu.push(text); alles.push(text); };
  const eingabe = [...EINGABE];
  globalThis.prompt = (frage) => {
    if (frage !== undefined) schreib(String(frage));
    return eingabe.length ? eingabe.shift() : null;
  };
  for (const art of ['log', 'info', 'debug', 'warn', 'error']) console[art] = (...teile) => schreib(util.format(...teile) + '\n');
  const vorhanden = new Set(Object.getOwnPropertyNames(globalThis));

  const kennungen = new WeakMap();
  let naechsteKennung = 1;
  const kennung = (o) => {
    if (!kennungen.has(o)) kennungen.set(o, naechsteKennung++);
    return kennungen.get(o);
  };
  const kurz = (s) => (s.length <= MAX_ZEICHEN ? s : s.slice(0, MAX_ZEICHEN - 3) + '...');
  const zeige = (w) => kurz(util.inspect(w, { breakLength: Infinity, depth: 1, maxArrayLength: MAX_ELEMENTE }));

  function wert(w, tiefe = 0) {
    if (w === null) return { art: 'nichts', darstellung: 'null' };
    if (w === undefined) return { art: 'nichts', darstellung: 'undefined' };
    const typ = typeof w;
    if (typ === 'boolean') return { art: 'wahrheit', darstellung: String(w) };
    if (typ === 'number' || typ === 'bigint') return { art: 'zahl', darstellung: zeige(w) };
    if (typ === 'string') return { art: 'text', darstellung: zeige(w) };
    if (typ === 'symbol') return { art: 'sonst', darstellung: zeige(w) };
    if (typ === 'function') {
      const klasse = /^class\b/.test(Function.prototype.toString.call(w));
      return { art: klasse ? 'klasse' : 'funktion', darstellung: w.name || '(anonym)', kennung: kennung(w) };
    }
    const d = { art: 'objekt', darstellung: zeige(w), kennung: kennung(w) };
    if (Array.isArray(w)) d.art = 'liste';
    else if (w instanceof Set) d.art = 'menge';
    else if (w instanceof Map) d.art = 'woerterbuch';
    if (tiefe >= MAX_TIEFE) {
      d.gekuerzt = true;
      return d;
    }
    if (d.art === 'liste' || d.art === 'menge') {
      const teile = [...w];
      d.elemente = teile.slice(0, MAX_ELEMENTE).map((x) => wert(x, tiefe + 1));
      d.gekuerzt = teile.length > MAX_ELEMENTE;
    } else if (d.art === 'woerterbuch') {
      const paare = [...w];
      d.paare = paare.slice(0, MAX_ELEMENTE).map(([k, v]) => [wert(k, tiefe + 1), wert(v, tiefe + 1)]);
      d.gekuerzt = paare.length > MAX_ELEMENTE;
    } else {
      // Objekte zeigen ihre Eigenschaften; eigene Klassen tragen ihren Namen, einfache Objekte heißen Objekt
      const proto = Object.getPrototypeOf(w);
      d.darstellung = proto && proto !== Object.prototype && proto.constructor && proto.constructor.name ? proto.constructor.name : 'Objekt';
      const eintraege = Object.entries(w);
      d.attribute = Object.fromEntries(eintraege.slice(0, MAX_ELEMENTE).map(([k, v]) => [k, wert(v, tiefe + 1)]));
      d.gekuerzt = eintraege.length > MAX_ELEMENTE;
    }
    return d;
  }

  function namen(bereich, global) {
    const v = {};
    const liste = global ? Object.getOwnPropertyNames(bereich).filter((n) => !vorhanden.has(n)) : Object.keys(bereich);
    for (const n of liste) {
      try {
        v[n] = wert(bereich[n]);
      } catch {
        // noch nicht angelegt (let und const vor ihrer Zeile)
      }
    }
    return v;
  }

  globalThis[HILFE] = {
    wert: (w) => wert(w),
    lesen(bauplan, bereiche) {
      const rahmen = bauplan.map((r) => ({
        name: r.name,
        variablen: Object.assign({}, ...r.bereiche.map((b) => namen(bereiche[b.nr], b.global))),
      }));
      return { rahmen, ausgabe: neu.splice(0).join('') };
    },
  };

  const ergebnis = { fehler: null, fehlerzeile: null };
  const zeilenMuster = new RegExp(BEISPIEL.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ':(\\d+)');
  function fehler(e) {
    if (ergebnis.fehler !== null) return;
    const name = e && e.name ? e.name : 'Error';
    const text = e && e.message !== undefined ? e.message : String(e);
    ergebnis.fehler = text ? `${name}: ${text}` : name;
    const m = String(e && e.stack).match(zeilenMuster);
    ergebnis.fehlerzeile = m ? Number(m[1]) : null;
  }
  process.on('uncaughtException', fehler);
  process.on('unhandledRejection', fehler);

  const bereit = new Int32Array(new SharedArrayBuffer(4));
  const worker = new Worker(`(${verfolger.toString()})()`, {
    eval: true,
    workerData: { bereit, beispiel: BEISPIEL, maxSchritte: MAX_SCHRITTE },
    // klein halten: die Sandbox begrenzt den Adressraum, ein Worker mit Standardwerten passt nicht hinein
    resourceLimits: { codeRangeSizeMb: 8, maxOldGenerationSizeMb: 32, maxYoungGenerationSizeMb: 4, stackSizeMb: 1 },
  });
  // Warten, bis der Verfolger bereit ist. Bewusst eine Schleife statt Atomics.wait: nur solange JavaScript läuft,
  // nimmt der Hauptthread die Nachrichten des Inspectors an.
  const start = Date.now();
  while (Atomics.load(bereit, 0) === 0 && Date.now() - start < 10000) { /* warten */ }

  let skript = null;
  try {
    skript = new vm.Script(CODE, { filename: BEISPIEL });
  } catch (e) {
    fehler(e);
  }
  if (skript) {
    try {
      skript.runInThisContext();
    } catch (e) {
      fehler(e);
    }
  }

  // Erst abschließen, wenn auch Zeitgeber und Versprechen des Beispiels erledigt sind
  worker.unref();
  process.once('beforeExit', () => {
    worker.ref();
    worker.once('message', ({ schritte, gekuerzt }) => {
      const rest = neu.splice(0).join('');
      if (rest && schritte.length) schritte[schritte.length - 1].ausgabe += rest;
      process.stdout.write('\n' + MARKE + '\n' + JSON.stringify({ schritte, gekuerzt, ausgabe: alles.join(''), ...ergebnis }) + '\n');
      process.exit(0);
    });
    worker.postMessage('fertig');
  });
})();
