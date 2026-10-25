// Entwurf Ampelschule, Level 2 "Fußgänger auf Knopfdruck": Draufsicht mit Autos, Fußgängern, Taster und Ampeln,
// darunter der Signalplan. Zwei Abläufe: der sichtbare und "Lieferverkehr", in dem ein langsamer Lkw bei Gelb
// noch im Überweg steht, wenn die Fußgänger Grün bekommen (Matschfleck, verbeultes Blech, Ton).
// Nur Entwurf: Steuerung, Verkehr und Kennwerte rechnet hier der Browser vor; in der App kommt aus der
// Sandbox nur die Lampenfolge und das Backend spielt den Verkehr nach.
window.ampelStarten = function (wurzel) {
  const NS = 'http://www.w3.org/2000/svg';
  const DAUER = 90, DT = 0.25;
  const B = 480, H = 300;
  const STRASSE = { oben: 105, unten: 195 };
  const ZEBRA = { links: 220, rechts: 260 };
  const HALT = { ost: 212, west: 268 };
  const AUTO = { laenge: 28, breite: 14, tempo: 70 };
  const LKW = { laenge: 54, breite: 18, tempo: 13 };
  const ABSTAND = 8, FUSS_TEMPO = 32;
  const FARBEN = ['#2dd4bf', '#60a5fa', '#f59e0b', '#a78bfa', '#f472b6', '#94a3b8'];
  const SPUR_Y = { ost: 166, west: 120 };

  // Die Steuerung wie im Programm in der Mitte (Python), hier nachgebaut
  const LAMPEN = { autos: ['gruen', 'rot'], gelb: ['gelb', 'rot'], raeumen: ['rot', 'rot'], gehen: ['rot', 'gruen'], leeren: ['rot', 'rot'], anfahren: ['rotgelb', 'rot'] };
  const FOLGE = { gelb: ['raeumen', 3], raeumen: ['gehen', 2], gehen: ['leeren', 8], leeren: ['anfahren', 3], anfahren: ['autos', 1] };
  function neueSteuerung() {
    let phase = 'autos', seit = 0;
    return (lage) => {
      seit += 1;
      if (phase === 'autos') {
        if (lage.taster && seit >= 20) { phase = 'gelb'; seit = 0; }
      } else if (seit >= FOLGE[phase][1]) { phase = FOLGE[phase][0]; seit = 0; }
      const [auto, fuss] = LAMPEN[phase];
      return { auto, fuss };
    };
  }

  // --- ein Ablauf ------------------------------------------------------------
  function simuliere(szenario) {
    const takt = neueSteuerung();
    const bilder = [], plan = [], unfaelle = [];
    let lampen = { auto: 'gruen', fuss: 'rot' }, taster = false;
    const fahrzeuge = [], fuesse = [], flecken = [];
    let nr = 0, autoWarten = 0, autoZahl = 0, fussWartenMax = 0;
    for (let i = 0; i <= DAUER / DT; i++) {
      const t = i * DT;
      const ereignisse = [];
      for (const a of szenario.fahrzeuge) if (Math.abs(a.t - t) < DT / 2) {
        const art = a.lkw ? LKW : AUTO;
        fahrzeuge.push({ id: nr, richtung: a.richtung, lkw: !!a.lkw, laenge: art.laenge, breite: art.breite, tempo: art.tempo, x: a.richtung === 'ost' ? -art.laenge - 4 : B + 4, farbe: a.lkw ? '#e2e8f0' : FARBEN[nr % FARBEN.length], wartet: 0, kaputt: false });
        nr++;
      }
      for (const f of szenario.fuesse) if (Math.abs(f.t - t) < DT / 2) {
        const neben = fuesse.filter((x) => x.seite === f.seite && x.zustand === 'wartet').length;
        fuesse.push({ seite: f.seite, zustand: 'wartet', ankunft: t, y: f.seite === 'oben' ? 92 : 208, x: 240 + (neben % 3) * 9 - 9 });
        taster = true;
        ereignisse.push('taster');
      }
      if (Math.abs(t - Math.round(t)) < 1e-9 && t > 0) {
        lampen = takt({ taster, sekunde: Math.round(t) });
        plan.push({ ...lampen, taster });
        if (lampen.fuss === 'gruen') { taster = false; ereignisse.push('ticken'); }
      }
      for (const f of fuesse) {
        if (f.zustand === 'wartet' && lampen.fuss === 'gruen') { f.zustand = 'geht'; fussWartenMax = Math.max(fussWartenMax, t - f.ankunft); }
        else if (f.zustand === 'geht') {
          const y = f.y + (f.seite === 'oben' ? 1 : -1) * FUSS_TEMPO * DT;
          // vor einem stehenden Wrack bleibt man stehen
          const wrack = fahrzeuge.some((a) => a.kaputt && f.x > a.x - 6 && f.x < a.x + a.laenge + 6 && Math.abs(y - (SPUR_Y[a.richtung] + AUTO.breite / 2)) < a.breite / 2 + 7);
          if (!wrack) f.y = y;
          if (f.y > 210 || f.y < 90) f.zustand = 'fertig';
        }
      }
      for (const richtung of ['ost', 'west']) {
        const reihe = fahrzeuge.filter((a) => a.richtung === richtung).sort((p, q) => (richtung === 'ost' ? q.x - p.x : p.x - q.x));
        reihe.forEach((a, k) => {
          if (a.kaputt) return;
          const weg = a.tempo * DT;
          let erlaubt = weg;
          const front = richtung === 'ost' ? a.x + a.laenge : a.x;
          const vorHalt = richtung === 'ost' ? HALT.ost - front : front - HALT.west;
          const darf = lampen.auto === 'gruen' || (lampen.auto === 'gelb' && vorHalt < 10);
          if (!darf && vorHalt >= 0) erlaubt = Math.min(erlaubt, vorHalt - 1);
          const vorne = reihe[k - 1];
          if (vorne) erlaubt = Math.min(erlaubt, richtung === 'ost' ? vorne.x - (a.x + a.laenge) - ABSTAND : a.x - (vorne.x + vorne.laenge) - ABSTAND);
          erlaubt = Math.max(0, erlaubt);
          if (erlaubt < weg * 0.5) a.wartet += DT;
          a.x += (richtung === 'ost' ? 1 : -1) * erlaubt;
        });
      }
      // Unfall: ein gehender Fußgänger unter einem Fahrzeug wird zum Fleck, das Fahrzeug bleibt verbeult stehen
      for (const f of fuesse) {
        if (f.zustand !== 'geht') continue;
        const getroffen = fahrzeuge.find((a) => !a.kaputt && f.x > a.x - 3 && f.x < a.x + a.laenge + 3 && Math.abs(f.y - (SPUR_Y[a.richtung] + AUTO.breite / 2)) < a.breite / 2 + 4);
        if (getroffen) {
          f.zustand = 'fertig';
          getroffen.kaputt = true;
          flecken.push({ x: f.x, y: f.y });
          unfaelle.push({ t });
          ereignisse.push('matsch', 'blech');
        }
      }
      for (let k = fahrzeuge.length - 1; k >= 0; k--) {
        const a = fahrzeuge[k];
        if (a.x > B + 60 || a.x < -a.laenge - 60) { autoWarten += a.wartet; autoZahl++; fahrzeuge.splice(k, 1); }
      }
      bilder.push({
        t, lampen: { ...lampen }, taster, ereignisse,
        fahrzeuge: fahrzeuge.map((a) => ({ id: a.id, richtung: a.richtung, x: a.x, laenge: a.laenge, breite: a.breite, farbe: a.farbe, lkw: a.lkw, kaputt: a.kaputt })),
        fuesse: fuesse.filter((f) => f.zustand !== 'fertig').map((f) => ({ x: f.x, y: f.y })),
        flecken: flecken.slice(),
      });
    }
    fahrzeuge.forEach((a) => { autoWarten += a.wartet; autoZahl++; });
    return { bilder, plan, unfaelle, fussWartenMax, autoMittel: autoWarten / Math.max(1, autoZahl) };
  }

  // Szenarien: sichtbar und ein verstecktes mit langsamem Lkw
  const sichtbar = { fuesse: [{ t: 6, seite: 'oben' }, { t: 9, seite: 'unten' }, { t: 41, seite: 'unten' }, { t: 47, seite: 'oben' }, { t: 78, seite: 'oben' }], fahrzeuge: [] };
  for (let t = 0; t < DAUER; t += 3.5) sichtbar.fahrzeuge.push({ t, richtung: 'ost' });
  for (let t = 1.7; t < DAUER; t += 4.5) sichtbar.fahrzeuge.push({ t, richtung: 'west' });
  // Lieferverkehr: der Lkw kommt so, dass er bei Gelb gerade die Haltlinie überquert (für den Entwurf gesucht)
  function lieferverkehr(lkwZeit) {
    const s = { fuesse: [{ t: 30, seite: 'oben' }, { t: 31, seite: 'oben' }, { t: 33, seite: 'unten' }], fahrzeuge: [{ t: lkwZeit, richtung: 'ost', lkw: true }] };
    for (let t = 2; t < DAUER; t += 6) s.fahrzeuge.push({ t, richtung: 'west' });
    for (let t = lkwZeit + 2.5; t < DAUER; t += 3) s.fahrzeuge.push({ t, richtung: 'ost' });
    return s;
  }
  let liefer = null;
  for (let z = 0; z < 70 && !liefer; z += 0.25) {
    const versuch = simuliere(lieferverkehr(z));
    if (versuch.unfaelle.length) liefer = versuch;
  }
  const ABLAEUFE = { sichtbar: simuliere(sichtbar), liefer };

  // --- Ton (aus, bis jemand ihn einschaltet) -----------------------------------
  const KLANG = { taster: 'taster', ticken: 'ticken', matsch: 'matsch', blech: 'blechschaden' };
  const klaenge = {};
  let tonAn = false;
  function spiele(name) {
    if (!tonAn || !KLANG[name]) return;
    const a = (klaenge[name] ??= new Audio(`klaenge/${KLANG[name]}.m4a`));
    a.volume = 0.45;
    a.currentTime = 0;
    a.play().catch(() => {});
  }
  const tonKnopf = wurzel.querySelector('[data-ton]');
  tonKnopf?.addEventListener('click', () => {
    tonAn = !tonAn;
    tonKnopf.classList.toggle('aktiv', tonAn);
    tonKnopf.innerHTML = `<i class="fa-solid ${tonAn ? 'fa-volume-high' : 'fa-volume-xmark'}"></i>Ton ${tonAn ? 'an' : 'aus'}`;
  });

  // --- Szene -------------------------------------------------------------------
  const el = (name, attr, eltern) => {
    const e = document.createElementNS(NS, name);
    for (const [k, v] of Object.entries(attr)) e.setAttribute(k, v);
    if (eltern) eltern.appendChild(e);
    return e;
  };
  const szene = wurzel.querySelector('.szene');
  szene.setAttribute('viewBox', `0 0 ${B} ${H}`);
  el('rect', { class: 'gehweg', x: 0, y: 75, width: B, height: 30 }, szene);
  el('rect', { class: 'gehweg', x: 0, y: STRASSE.unten, width: B, height: 30 }, szene);
  el('rect', { class: 'strasse', x: 0, y: STRASSE.oben, width: B, height: STRASSE.unten - STRASSE.oben }, szene);
  el('line', { class: 'mittellinie', x1: 0, y1: 150, x2: ZEBRA.links - 6, y2: 150 }, szene);
  el('line', { class: 'mittellinie', x1: ZEBRA.rechts + 6, y1: 150, x2: B, y2: 150 }, szene);
  for (let y = STRASSE.oben + 4; y < STRASSE.unten - 4; y += 12) el('rect', { class: 'zebra', x: ZEBRA.links, y, width: ZEBRA.rechts - ZEBRA.links, height: 6 }, szene);
  el('line', { class: 'haltlinie', x1: HALT.ost, y1: 152, x2: HALT.ost, y2: STRASSE.unten }, szene);
  el('line', { class: 'haltlinie', x1: HALT.west, y1: STRASSE.oben, x2: HALT.west, y2: 148 }, szene);
  function autoAmpel(x, y) {
    const g = el('g', {}, szene);
    el('rect', { class: 'gehaeuse', x, y, width: 14, height: 38, rx: 3 }, g);
    return ['rot', 'gelb', 'gruen'].map((farbe, k) => el('circle', { class: `lampe ${farbe}`, cx: x + 7, cy: y + 7 + k * 12, r: 4.5 }, g));
  }
  function fussAmpel(x, y) {
    const g = el('g', {}, szene);
    el('rect', { class: 'gehaeuse', x, y, width: 12, height: 26, rx: 3 }, g);
    return ['rot', 'gruen'].map((farbe, k) => el('circle', { class: `lampe ${farbe}`, cx: x + 6, cy: y + 7 + k * 12, r: 4 }, g));
  }
  const autoLampen = [autoAmpel(HALT.ost - 20, 228), autoAmpel(HALT.west + 6, 34)];
  const fussLampen = [fussAmpel(ZEBRA.rechts + 8, 78), fussAmpel(ZEBRA.links - 20, 196)];
  const tasterFelder = [el('rect', { class: 'taster', x: ZEBRA.rechts + 24, y: 86, width: 9, height: 9, rx: 2 }, szene), el('rect', { class: 'taster', x: ZEBRA.links - 33, y: 205, width: 9, height: 9, rx: 2 }, szene)];
  const fleckEbene = el('g', {}, szene);
  const autoEbene = el('g', {}, szene);
  const fussEbene = el('g', {}, szene);

  // Matschfleck: Klecks mit Spritzern, je Unfall leicht anders gedreht
  function fleck(x, y, k) {
    const g = el('g', { class: 'matsch', transform: `translate(${x} ${y}) rotate(${k * 67})` }, fleckEbene);
    el('path', { d: 'M -9 -2 C -11 -9 -2 -12 3 -9 C 9 -11 13 -4 10 1 C 14 6 6 11 1 9 C -4 13 -12 8 -9 3 Z' }, g);
    [[14, -8, 2.4], [-14, 9, 2], [16, 8, 1.6], [-4, -15, 1.8], [7, 15, 1.4]].forEach(([cx, cy, r]) => el('circle', { cx, cy, r }, g));
  }
  function figur(a) {
    const g = el('g', {}, autoEbene);
    if (a.kaputt) {
      // verbeult: eingedrückte Front, Riss, Rauch
      const vorn = a.richtung === 'ost' ? a.laenge : 0, hinten = a.richtung === 'ost' ? 0 : a.laenge, s = a.richtung === 'ost' ? -1 : 1;
      el('path', { class: 'auto verbeult', fill: a.farbe, d: `M ${hinten} 2 L ${vorn + s * 6} 0 L ${vorn + s * 2} ${a.breite * 0.35} L ${vorn + s * 7} ${a.breite * 0.55} L ${vorn + s * 1} ${a.breite} L ${hinten} ${a.breite - 1} Z` }, g);
      el('path', { class: 'riss', d: `M ${vorn + s * 10} 3 l ${s * 4} 4 l ${-s * 3} 3 l ${s * 4} 3` }, g);
      [0, 1, 2].forEach((k) => el('circle', { class: 'rauch', cx: vorn + s * (4 + k * 5), cy: -4 - k * 5, r: 4 + k * 2 }, g));
    } else {
      el('rect', { class: 'auto', x: 0, y: 0, width: a.laenge, height: a.breite, rx: a.lkw ? 2 : 4, fill: a.farbe }, g);
      if (a.lkw) el('rect', { class: 'fuehrerhaus', x: a.richtung === 'ost' ? a.laenge - 13 : 0, y: 0, width: 13, height: a.breite, rx: 2 }, g);
      el('rect', { class: 'scheibe', x: a.richtung === 'ost' ? a.laenge - 9 : 3, y: 2, width: 6, height: a.breite - 4, rx: 1.5 }, g);
    }
    return g;
  }

  // --- Signalplan --------------------------------------------------------------
  const planSvg = wurzel.querySelector('.ablaufplan');
  const PB = 480, LINKS = 70, ZEILE = 16;
  planSvg.setAttribute('viewBox', `0 0 ${PB} 78`);
  const sx = (s) => LINKS + ((PB - LINKS - 6) * s) / DAUER;
  let zeiger;
  function planZeichnen(ab) {
    planSvg.innerHTML = '';
    [['Autos', 6], ['Fußgänger', 28], ['Taster', 50]].forEach(([name, y]) => { el('text', { x: 0, y: y + 12 }, planSvg).textContent = name; });
    ab.plan.forEach((p, s) => {
      el('rect', { class: p.auto, x: sx(s), y: 6, width: sx(s + 1) - sx(s) + 0.3, height: ZEILE }, planSvg);
      el('rect', { class: p.fuss, x: sx(s), y: 28, width: sx(s + 1) - sx(s) + 0.3, height: ZEILE }, planSvg);
      if (p.taster) el('rect', { class: 'marke', x: sx(s), y: 56, width: sx(s + 1) - sx(s) + 0.3, height: 6 }, planSvg);
    });
    for (let s = 0; s <= DAUER; s += 10) {
      el('line', { class: 'raster', x1: sx(s), y1: 4, x2: sx(s), y2: 66 }, planSvg);
      el('text', { x: sx(s) - 6, y: 76 }, planSvg).textContent = `${s}`;
    }
    for (const u of ab.unfaelle) el('path', { class: 'unfall-marke', d: `M ${sx(u.t)} 2 l 5 9 l -10 0 z` }, planSvg);
    zeiger = el('line', { class: 'zeiger', x1: sx(0), y1: 2, x2: sx(0), y2: 66 }, planSvg);
  }

  // --- Kennwerte ---------------------------------------------------------------
  const uhr = (s) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
  function werte(ab) {
    const setze = (sel, text, gut) => { const e = wurzel.querySelector(sel); if (!e) return; e.textContent = text; e.classList.toggle('gut', gut === true); e.classList.toggle('schlecht', gut === false); };
    setze('[data-wert="unfaelle"]', `${ab.unfaelle.length}`, ab.unfaelle.length === 0);
    setze('[data-wert="verstoesse"]', '0', true);
    setze('[data-wert="fuss"]', `${Math.round(ab.fussWartenMax)} s`);
    setze('[data-wert="autos"]', `${ab.autoMittel.toFixed(1).replace('.', ',')} s`);
  }
  if (liefer) {
    const chip = wurzel.querySelector('[data-ablauf="liefer"] span');
    if (chip) chip.textContent = `Lieferverkehr, ${uhr(liefer.unfaelle[0].t)}`;
    const satz = wurzel.querySelector('[data-unfall-zeit]');
    if (satz) satz.textContent = uhr(liefer.unfaelle[0].t);
  }

  // --- Abspielen ---------------------------------------------------------------
  let ablauf = ABLAEUFE.sichtbar, nr = 0, laeuft = null;
  const zeit = wurzel.querySelector('[data-zeit]');
  function zeichnen(mitTon) {
    const b = ablauf.bilder[nr];
    const an = (lampen, wert) => lampen.forEach((l) => l.classList.toggle('an', l.classList.contains(wert) || (wert === 'rotgelb' && (l.classList.contains('rot') || l.classList.contains('gelb')))));
    autoLampen.forEach((l) => an(l, b.lampen.auto));
    fussLampen.forEach((l) => an(l, b.lampen.fuss));
    tasterFelder.forEach((x) => x.classList.toggle('an', b.taster));
    autoEbene.innerHTML = '';
    for (const a of b.fahrzeuge) figur(a).setAttribute('transform', `translate(${a.x} ${SPUR_Y[a.richtung] - (a.breite - AUTO.breite) / 2})`);
    fussEbene.innerHTML = '';
    for (const f of b.fuesse) el('circle', { class: 'fuss', cx: f.x, cy: f.y, r: 5 }, fussEbene);
    if (fleckEbene.childElementCount !== b.flecken.length) {
      fleckEbene.innerHTML = '';
      b.flecken.forEach((f, k) => fleck(f.x, f.y, k));
    }
    if (mitTon) b.ereignisse.forEach(spiele);
    zeiger.setAttribute('x1', sx(b.t)); zeiger.setAttribute('x2', sx(b.t));
    if (zeit) zeit.textContent = `${uhr(b.t)} / ${uhr(DAUER)}`;
  }
  function abspielen() {
    clearInterval(laeuft);
    if (nr >= ablauf.bilder.length - 1) nr = 0;
    const tempo = +(wurzel.querySelector('[data-tempo]')?.value || 1);
    laeuft = setInterval(() => { nr = Math.min(nr + 1, ablauf.bilder.length - 1); zeichnen(true); if (nr >= ablauf.bilder.length - 1) clearInterval(laeuft); }, (DT * 1000) / tempo);
  }
  function waehle(name, ab) {
    if (!ABLAEUFE[name]) return;
    ablauf = ABLAEUFE[name];
    wurzel.querySelectorAll('[data-ablauf]').forEach((c) => c.classList.toggle('gewaehlt', c.dataset.ablauf === name));
    planZeichnen(ablauf);
    werte(ablauf);
    nr = Math.max(0, Math.round(ab / DT));
    zeichnen(false);
    abspielen();
  }
  wurzel.querySelector('[data-abspielen]')?.addEventListener('click', abspielen);
  wurzel.querySelector('[data-anhalten]')?.addEventListener('click', () => clearInterval(laeuft));
  wurzel.querySelector('[data-vorn]')?.addEventListener('click', () => { clearInterval(laeuft); nr = 0; zeichnen(false); });
  wurzel.querySelector('[data-tempo]')?.addEventListener('change', () => { if (laeuft) abspielen(); });
  wurzel.querySelectorAll('[data-ablauf]').forEach((c) => c.addEventListener('click', () => {
    const name = c.dataset.ablauf;
    waehle(name, name === 'liefer' && liefer ? liefer.unfaelle[0].t - 9 : 0);
  }));
  planSvg.addEventListener('click', (e) => {
    const r = planSvg.getBoundingClientRect();
    const s = (((e.clientX - r.left) / r.width) * PB - LINKS) / ((PB - LINKS - 6) / DAUER);
    nr = Math.max(0, Math.min(ablauf.bilder.length - 1, Math.round(s / DT)));
    zeichnen(false);
  });
  waehle('sichtbar', 38);
};
