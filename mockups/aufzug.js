// Entwurf Aufzugsteuerung, Level 2 "Rufe sammeln": Haus mit offenem Schacht, Kabine mit mittig öffnender Tür,
// Etagenanzeigen, Wartenden mit Rufknöpfen, darunter das Fahrdiagramm. Die Tür fährt weich auf, bleibt offen,
// während Leute aus- und einsteigen, und fährt weich zu; Gong und Türgeräusch laufen im Takt (Ton aus, bis man
// ihn einschaltet). Nur Entwurf: Steuerung und Fahrgäste rechnet hier der Browser vor; in der App kommt aus der
// Sandbox nur die Folge der Befehle und das Backend spielt die Fahrt nach.
window.aufzugStarten = function (wurzel) {
  const NS = 'http://www.w3.org/2000/svg';
  const DAUER = 120, DT = 0.1, ETAGEN = 6;
  const TEMPO = 0.5; // Etagen je Sekunde in voller Fahrt
  const TUER = { auf: 1.3, offen: 2.6, zu: 1.3 }; // Sekunden
  const TUER_ZYKLUS = TUER.auf + TUER.offen + TUER.zu;
  const B = 360, H = 340, ETAGE_H = 50, BODEN = 320;
  const SCHACHT = { links: 156, rechts: 216 };
  const KABINE = { breite: 52, hoehe: 36 };
  const NAMEN = ['EG', '1', '2', '3', '4', '5'];
  const weich = (x) => (x <= 0 ? 0 : x >= 1 ? 1 : x * x * (3 - 2 * x)); // sanft anfahren und abbremsen

  const RUFE = [
    { t: 1, von: 0, nach: 4 }, { t: 4, von: 3, nach: 0 }, { t: 9, von: 5, nach: 2 }, { t: 14, von: 1, nach: 5 },
    { t: 22, von: 4, nach: 1 }, { t: 35, von: 0, nach: 3 }, { t: 41, von: 2, nach: 0 }, { t: 58, von: 5, nach: 0 },
    { t: 66, von: 3, nach: 5 }, { t: 80, von: 0, nach: 2 }, { t: 88, von: 4, nach: 0 }, { t: 101, von: 1, nach: 3 },
  ];

  // Die Steuerung wie im Programm in der Mitte (Python), hier nachgebaut
  let richtung = 0;
  function takt(lage) {
    const hier = lage.etage;
    const offen = [...new Set([...lage.ziele, ...lage.rufe[1], ...lage.rufe[-1]])];
    if (!offen.some((e) => (e - hier) * richtung > 0)) {
      if (offen.some((e) => e > hier)) richtung = 1;
      else if (offen.some((e) => e < hier)) richtung = -1;
      else richtung = lage.rufe[1].has(hier) ? 1 : offen.length ? -1 : 0;
    }
    if (lage.ziele.has(hier) || (lage.rufe[richtung] && lage.rufe[richtung].has(hier))) return 'halten';
    return richtung === 1 ? 'hoch' : richtung === -1 ? 'runter' : 'warten';
  }

  // --- Vorrechnen ----------------------------------------------------------
  // Fahrt: weich anfahren und abbremsen zwischen zwei Etagen (eine Etage dauert 1 / TEMPO Sekunden)
  const bilder = [], fahrt = [], rufPunkte = [];
  const wartende = [], kabine = [];
  let pos = 0, befehl = 'warten', fahrtVon = 0, fahrtZeit = 0;
  let tuerZeit = -1; // Sekunden seit Beginn des Türzyklus, -1 ohne Halt
  let aus = [], ein = [];
  let wartenSumme = 0, wartenMax = 0, bedient = 0, nr = 0;
  for (let i = 0; i <= DAUER / DT; i++) {
    const t = +(i * DT).toFixed(2);
    const ereignisse = [];
    for (const r of RUFE) if (Math.abs(r.t - t) < DT / 2) {
      wartende.push({ ...r, nr: nr++, richtung: Math.sign(r.nach - r.von) });
      rufPunkte.push({ t, etage: r.von });
    }
    if (tuerZeit >= 0) {
      tuerZeit += DT;
      if (Math.abs(tuerZeit - (TUER.auf + TUER.offen)) < DT / 2) ereignisse.push('tuer_zu');
      if (tuerZeit >= TUER_ZYKLUS) { tuerZeit = -1; aus = []; ein = []; }
    } else if (befehl === 'hoch' || befehl === 'runter') {
      fahrtZeit += DT;
      const anteil = Math.min(1, fahrtZeit * TEMPO);
      pos = fahrtVon + (befehl === 'hoch' ? 1 : -1) * weich(anteil);
      if (anteil >= 1) { pos = Math.round(pos); befehl = 'warten'; }
    }
    if (tuerZeit < 0 && befehl === 'warten') {
      const lage = {
        etage: pos,
        ziele: new Set(kabine.map((p) => p.nach)),
        rufe: { 1: new Set(wartende.filter((w) => w.richtung === 1).map((w) => w.von)), [-1]: new Set(wartende.filter((w) => w.richtung === -1).map((w) => w.von)) },
      };
      befehl = takt(lage);
      if (befehl === 'halten') {
        // Halt: wer hier will, steigt aus; wer in Fahrtrichtung will, steigt ein
        tuerZeit = 0;
        ereignisse.push('gong', 'tuer_auf');
        aus = kabine.filter((p) => p.nach === pos);
        ein = wartende.filter((w) => w.von === pos && w.richtung === richtung);
        for (const p of aus) kabine.splice(kabine.indexOf(p), 1);
        for (const w of ein) {
          wartenSumme += t - w.t; wartenMax = Math.max(wartenMax, t - w.t); bedient++;
          wartende.splice(wartende.indexOf(w), 1);
          kabine.push(w);
        }
        befehl = 'warten';
      } else if (befehl === 'hoch' || befehl === 'runter') { fahrtVon = pos; fahrtZeit = 0; }
    }
    // Tür: weich auf, offen, weich zu; Aussteiger gehen zuerst, dann steigen die Wartenden ein
    let tuer = 0, ausAnteil = 0, einAnteil = 0;
    if (tuerZeit >= 0) {
      tuer = tuerZeit < TUER.auf ? weich(tuerZeit / TUER.auf) : tuerZeit < TUER.auf + TUER.offen ? 1 : 1 - weich((tuerZeit - TUER.auf - TUER.offen) / TUER.zu);
      ausAnteil = weich((tuerZeit - TUER.auf * 0.7) / 1.1);
      einAnteil = weich((tuerZeit - TUER.auf * 0.7 - (aus.length ? 0.9 : 0)) / 1.2);
    }
    if (i % 5 === 0) fahrt.push({ t, pos });
    bilder.push({
      t, pos, tuer, richtung, ereignisse,
      kabine: kabine.length - (einAnteil < 1 ? ein.length : 0),
      aus: aus.length, ausAnteil, ein: ein.length, einAnteil,
      wartende: wartende.map((w) => ({ von: w.von, richtung: w.richtung })),
    });
  }

  const el = (name, attr, eltern) => {
    const e = document.createElementNS(NS, name);
    for (const [k, v] of Object.entries(attr)) e.setAttribute(k, v);
    if (eltern) eltern.appendChild(e);
    return e;
  };

  // --- Haus: Etagen, offener Schacht, Türrahmen, Anzeigen ---------------------
  const szene = wurzel.querySelector('.szene');
  szene.setAttribute('viewBox', `0 0 ${B} ${H}`);
  const yEtage = (e) => BODEN - e * ETAGE_H;
  const kabineX = SCHACHT.links + (SCHACHT.rechts - SCHACHT.links - KABINE.breite) / 2;
  const oben = BODEN - ETAGEN * ETAGE_H;
  el('rect', { class: 'gehweg', x: 16, y: oben, width: B - 32, height: ETAGEN * ETAGE_H }, szene);
  el('rect', { class: 'schacht', x: SCHACHT.links, y: oben, width: SCHACHT.rechts - SCHACHT.links, height: ETAGEN * ETAGE_H }, szene);
  // Seile von oben zur Kabine
  const seile = el('g', { class: 'seil' }, szene);
  const rufLampen = [], anzeigen = [];
  for (let e = 0; e < ETAGEN; e++) {
    el('line', { class: 'etage', x1: 16, y1: yEtage(e), x2: B - 16, y2: yEtage(e) }, szene);
    el('text', { class: 'beschriftung', x: SCHACHT.rechts + 48, y: yEtage(e) - 18 }, szene).textContent = NAMEN[e];
    // Türrahmen um die Schachtöffnung dieser Etage
    el('rect', { class: 'rahmen-tuer', x: kabineX - 3, y: yEtage(e) - KABINE.hoehe - 3, width: KABINE.breite + 6, height: KABINE.hoehe + 3 }, szene);
    // Anzeige über der Tür: Etage und Richtung
    el('rect', { class: 'anzeige-feld', x: kabineX + KABINE.breite / 2 - 12, y: yEtage(e) - KABINE.hoehe - 12, width: 24, height: 8, rx: 1.5 }, szene);
    anzeigen.push(el('text', { class: 'anzeige', x: kabineX + KABINE.breite / 2, y: yEtage(e) - KABINE.hoehe - 5.6, 'text-anchor': 'middle' }, szene));
    const hoch = e < ETAGEN - 1 ? el('path', { class: 'ruf', d: `M ${SCHACHT.links - 12} ${yEtage(e) - 28} l 4 -6 l 4 6 z` }, szene) : null;
    const runter = e > 0 ? el('path', { class: 'ruf', d: `M ${SCHACHT.links - 12} ${yEtage(e) - 22} l 4 6 l 4 -6 z` }, szene) : null;
    rufLampen.push({ 1: hoch, [-1]: runter });
  }
  const wartendeEbene = el('g', {}, szene);
  const defs = el('defs', {}, szene);

  // Kabine: beleuchtetes Inneres, Handlauf, Fahrgäste, zwei Türblätter, die in die Wand gleiten
  const kabineG = el('g', {}, szene);
  const clip = el('clipPath', { id: 'kabine-schnitt' }, defs);
  el('rect', { x: 0, y: 0, width: KABINE.breite, height: KABINE.hoehe }, clip);
  el('rect', { class: 'kabine-innen', x: 0, y: 0, width: KABINE.breite, height: KABINE.hoehe }, kabineG);
  el('line', { class: 'handlauf', x1: 4, y1: KABINE.hoehe * 0.55, x2: KABINE.breite - 4, y2: KABINE.hoehe * 0.55 }, kabineG);
  const fahrgaeste = el('g', {}, kabineG);
  const tuerG = el('g', { 'clip-path': 'url(#kabine-schnitt)' }, kabineG);
  const blattL = el('g', {}, tuerG), blattR = el('g', {}, tuerG);
  for (const [g, x] of [[blattL, 0], [blattR, KABINE.breite / 2]]) {
    el('rect', { class: 'tuerblatt', x, y: 0, width: KABINE.breite / 2, height: KABINE.hoehe }, g);
    el('line', { class: 'tuerkante', x1: x + (x ? 0.6 : KABINE.breite / 2 - 0.6), y1: 0, x2: x + (x ? 0.6 : KABINE.breite / 2 - 0.6), y2: KABINE.hoehe }, g);
  }
  el('rect', { class: 'kabine', x: 0, y: 0, width: KABINE.breite, height: KABINE.hoehe, fill: 'none' }, kabineG);

  // Schachttüren je Etage: Glas, damit man die Kabine fahren sieht; an der Halteetage gleiten sie mit der Kabinentür
  const schachttueren = [];
  for (let e = 0; e < ETAGEN; e++) {
    const y = yEtage(e) - KABINE.hoehe;
    const c = el('clipPath', { id: `schacht-${e}` }, defs);
    el('rect', { x: kabineX, y, width: KABINE.breite, height: KABINE.hoehe }, c);
    const g = el('g', { 'clip-path': `url(#schacht-${e})` }, szene);
    const links = el('g', {}, g), rechts = el('g', {}, g);
    for (const [h, x] of [[links, kabineX], [rechts, kabineX + KABINE.breite / 2]]) {
      el('rect', { class: 'glas', x, y, width: KABINE.breite / 2, height: KABINE.hoehe }, h);
      el('line', { class: 'glas-kante', x1: x + 1, y1: y, x2: x + 1, y2: y + KABINE.hoehe }, h);
      el('line', { class: 'glas-kante', x1: x + KABINE.breite / 2 - 1, y1: y, x2: x + KABINE.breite / 2 - 1, y2: y + KABINE.hoehe }, h);
      el('line', { class: 'glas-schein', x1: x + 6, y1: y + 6, x2: x + 12, y2: y + 16 }, h);
    }
    schachttueren.push([links, rechts]);
  }
  const laeufer = el('g', {}, szene); // wer gerade ein- oder aussteigt

  // --- Fahrdiagramm ----------------------------------------------------------
  const plan = wurzel.querySelector('.ablaufplan');
  const PB = 480, PH = 112, LINKS = 26, OBEN = 6, UNTEN = 96;
  plan.setAttribute('viewBox', `0 0 ${PB} ${PH}`);
  const px = (t) => LINKS + ((PB - LINKS - 6) * t) / DAUER;
  const py = (e) => UNTEN - ((UNTEN - OBEN) * e) / (ETAGEN - 1);
  for (let e = 0; e < ETAGEN; e++) {
    el('line', { class: 'raster', x1: LINKS, y1: py(e), x2: PB - 6, y2: py(e) }, plan);
    el('text', { x: 0, y: py(e) + 3 }, plan).textContent = NAMEN[e];
  }
  for (let s = 0; s <= DAUER; s += 20) el('text', { x: px(s) - 6, y: PH - 2 }, plan).textContent = `${s}`;
  el('polyline', { class: 'fahrt', points: fahrt.map((f) => `${px(f.t).toFixed(1)},${py(f.pos).toFixed(1)}`).join(' ') }, plan);
  for (const r of rufPunkte) el('circle', { class: 'marke', cx: px(r.t), cy: py(r.etage), r: 2.6 }, plan);
  const zeiger = el('line', { class: 'zeiger', x1: px(0), y1: OBEN - 4, x2: px(0), y2: UNTEN + 2 }, plan);

  const setze = (sel, text, klasse) => { const e = wurzel.querySelector(sel); if (e) { e.textContent = text; if (klasse) e.classList.add(klasse); } };
  setze('[data-wert="verstoesse"]', '0', 'gut');
  setze('[data-wert="mittel"]', `${(wartenSumme / Math.max(1, bedient)).toFixed(1).replace('.', ',')} s`);
  setze('[data-wert="max"]', `${Math.round(wartenMax)} s`);
  setze('[data-wert="bedient"]', `${bedient} / ${RUFE.length}`);

  // --- Ton (aus, bis jemand ihn einschaltet) ---------------------------------
  const klaenge = {};
  let tonAn = false;
  function spiele(name) {
    if (!tonAn) return;
    const a = (klaenge[name] ??= new Audio(`klaenge/${name}.m4a`));
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

  // --- Abspielen -------------------------------------------------------------
  let nr2 = 0, laeuft = null;
  const zeit = wurzel.querySelector('[data-zeit]');
  const uhr = (s) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
  const mensch = (eltern, cx, cy, klasse = 'fuss') => {
    const g = el('g', { class: klasse }, eltern);
    el('circle', { cx, cy: cy - 9, r: 3.2 }, g);
    el('rect', { x: cx - 3.4, y: cy - 6, width: 6.8, height: 9, rx: 2.5 }, g);
    return g;
  };
  function zeichnen(mitTon) {
    const b = bilder[nr2];
    if (mitTon) b.ereignisse.forEach(spiele);
    const ky = BODEN - b.pos * ETAGE_H - KABINE.hoehe;
    kabineG.setAttribute('transform', `translate(${kabineX} ${ky})`);
    seile.innerHTML = '';
    for (const dx of [16, 26, 36]) el('line', { x1: kabineX + dx, y1: oben, x2: kabineX + dx, y2: ky }, seile);
    const weg = (KABINE.breite / 2) * b.tuer;
    blattL.setAttribute('transform', `translate(${-weg} 0)`);
    blattR.setAttribute('transform', `translate(${weg} 0)`);
    schachttueren.forEach(([l, r], e) => {
      const w = e === Math.round(b.pos) ? weg : 0;
      l.setAttribute('transform', `translate(${-w} 0)`);
      r.setAttribute('transform', `translate(${w} 0)`);
    });
    // Fahrgäste in der Kabine stehen nebeneinander, sichtbar durch die offene Tür
    fahrgaeste.innerHTML = '';
    const drin = b.kabine + (b.aus ? Math.round(b.aus * (1 - Math.min(1, b.ausAnteil * 2))) : 0);
    for (let k = 0; k < Math.min(drin, 5); k++) mensch(fahrgaeste, 8 + k * 9, KABINE.hoehe - 4);
    // Aussteiger gehen nach rechts aus der Tür, Einsteiger kommen von links herein
    laeufer.innerHTML = '';
    const boden = yEtage(Math.round(b.pos)) - 4;
    for (let k = 0; k < b.aus; k++) if (b.ausAnteil > 0 && b.ausAnteil < 1) mensch(laeufer, kabineX + KABINE.breite / 2 + b.ausAnteil * 70 + k * 8, boden);
    for (let k = 0; k < b.ein; k++) if (b.einAnteil < 1) mensch(laeufer, SCHACHT.links - 26 - k * 10 + b.einAnteil * (kabineX + 14 - SCHACHT.links + 26 + k * 10), boden);
    wartendeEbene.innerHTML = '';
    const proEtage = {};
    for (const w of b.wartende) {
      const k = (proEtage[w.von] = (proEtage[w.von] || 0) + 1) - 1;
      mensch(wartendeEbene, SCHACHT.links - 26 - k * 12, yEtage(w.von) - 4);
    }
    rufLampen.forEach((l, e) => [1, -1].forEach((r) => l[r]?.classList.toggle('an', b.wartende.some((w) => w.von === e && w.richtung === r))));
    const pfeil = b.richtung === 1 ? '▲' : b.richtung === -1 ? '▼' : '';
    anzeigen.forEach((a) => (a.textContent = `${pfeil}${NAMEN[Math.round(b.pos)]}`));
    zeiger.setAttribute('x1', px(b.t)); zeiger.setAttribute('x2', px(b.t));
    if (zeit) zeit.textContent = `${uhr(b.t)} / ${uhr(DAUER)}`;
  }
  function abspielen() {
    clearInterval(laeuft);
    if (nr2 >= bilder.length - 1) nr2 = 0;
    const tempo = +(wurzel.querySelector('[data-tempo]')?.value || 1);
    laeuft = setInterval(() => {
      const ziel = Math.min(nr2 + tempo, bilder.length - 1);
      // bei höherem Tempo keine Klänge überspringen
      while (nr2 < ziel) { nr2++; if (nr2 < ziel) bilder[nr2].ereignisse.forEach(spiele); }
      zeichnen(true);
      if (nr2 >= bilder.length - 1) clearInterval(laeuft);
    }, DT * 1000);
  }
  wurzel.querySelector('[data-abspielen]')?.addEventListener('click', abspielen);
  wurzel.querySelector('[data-anhalten]')?.addEventListener('click', () => clearInterval(laeuft));
  wurzel.querySelector('[data-vorn]')?.addEventListener('click', () => { clearInterval(laeuft); nr2 = 0; zeichnen(false); });
  wurzel.querySelector('[data-tempo]')?.addEventListener('change', () => { if (laeuft) abspielen(); });
  plan.addEventListener('click', (e) => {
    const r = plan.getBoundingClientRect();
    const s = (((e.clientX - r.left) / r.width) * PB - LINKS) / ((PB - LINKS - 6) / DAUER);
    nr2 = Math.max(0, Math.min(bilder.length - 1, Math.round(s / DT)));
    zeichnen(false);
  });
  nr2 = Math.round(10 / DT);
  zeichnen(false);
  abspielen();
};
