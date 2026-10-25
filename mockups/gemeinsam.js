// Gemeinsame Schale aller Entwürfe, damit Kopf, Navigation und Fuß überall gleich sind.
// Jede Seite setzt <html data-geraet="rechner|telefon" data-bereich="..."> und liefert
// ihren Inhalt in <template id="inhalt">.
(function () {
  const html = document.documentElement;
  const geraet = html.dataset.geraet;
  const bereich = html.dataset.bereich;
  try { html.dataset.theme = localStorage.getItem('cs-mock-theme') || 'dark'; } catch { html.dataset.theme = 'dark'; }

  const BEREICHE = [
    { id: 'dashboard', titel: 'Dashboard', icon: 'fa-house', telefon: true },
    { id: 'kurs', titel: 'Kurs', icon: 'fa-graduation-cap', telefon: true },
    { id: 'aufgaben', titel: 'Aufgaben', icon: 'fa-list-check', telefon: true },
    { id: 'pfade', titel: 'Pfade', icon: 'fa-route', telefon: true },
    { id: 'spiele', titel: 'Spiele', icon: 'fa-gamepad', telefon: true },
    { id: 'verwaltung', titel: 'Verwaltung', icon: 'fa-table-cells-large', telefon: false },
  ];
  const ziel = (id) => `${geraet}-${id === 'dashboard' ? 'start' : id}.html`;
  const inhalt = document.getElementById('inhalt').innerHTML;
  const themaKnopf = '<button class="ikon" onclick="umschalten()" title="Theme wechseln"><i class="fa-solid fa-sun"></i></button>';

  if (geraet === 'rechner') {
    document.body.innerHTML = `
      <div class="app">
        <header class="topbar">
          <button class="ikon"><i class="fa-solid fa-angles-left"></i></button>
          <div class="marke"><i class="fa-solid fa-hammer"></i>Codeschmiede</div>
          <div class="rechts"><span class="kopf-stand" title="Stufe 7, Geselle: 1.284 von 1.600 Punkten bis Stufe 8"><span class="mini-ring" style="--anteil:62"><span>7</span></span>Geselle</span><span class="kopf-stand" title="Serie: 12 Tage, zwei Schutzschilde"><i class="fa-solid fa-fire flamme"></i><span class="num">12</span><i class="fa-solid fa-shield-halved schild"></i><i class="fa-solid fa-shield-halved schild"></i><i class="fa-solid fa-shield-halved schild leer"></i></span><span class="konto"><i class="fa-solid fa-user"></i>marcel<button class="ikon" title="Abmelden"><i class="fa-solid fa-right-from-bracket"></i></button></span>${themaKnopf}</div>
        </header>
        <div class="koerper">
          <aside class="nav">
            ${BEREICHE.map((b) => `<a class="nav-btn ${b.id === bereich ? 'aktiv' : ''}" href="${ziel(b.id)}" title="${b.titel}"><i class="fa-solid ${b.icon}"></i><span>${b.titel}</span></a>`).join('')}
            <div class="nav-fuss">Lokal und abgeschottet</div>
          </aside>
          <main class="haupt">${inhalt}</main>
        </div>
        <footer class="fuss"><span><i class="fa-solid fa-hammer"></i> Codeschmiede v0.71.10</span><span>Lokal, ohne Tracking, ohne Werbung</span></footer>
      </div>`;
  } else {
    document.body.innerHTML = `
      <div class="telefon">
        <header class="t-kopf"><div class="marke"><i class="fa-solid fa-hammer"></i>Codeschmiede</div><div class="rechts"><button class="ikon" title="Abmelden"><i class="fa-solid fa-right-from-bracket"></i></button>${themaKnopf}</div></header>
        <main class="t-inhalt">${inhalt}</main>
        <nav class="t-reiter">
          ${BEREICHE.filter((b) => b.telefon).map((b) => `<button class="${b.id === bereich ? 'aktiv' : ''}" onclick="location.href='${ziel(b.id)}'"><i class="fa-solid ${b.icon}"></i>${b.titel}</button>`).join('')}
        </nav>
      </div>`;
  }
  document.body.insertAdjacentHTML('beforeend', '<div class="mock-leiste"><a href="index.html">Übersicht</a></div>');

  window.umschalten = () => {
    html.dataset.theme = html.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('cs-mock-theme', html.dataset.theme); } catch { /* egal */ }
  };
  // Kleine Umschalter: [data-gruppe] Knöpfe mit data-ziel schalten .t-pane / Reiter
  document.addEventListener('click', (e) => {
    const k = e.target.closest('[data-ziel]');
    if (!k) return;
    const gruppe = k.dataset.gruppe;
    document.querySelectorAll(`[data-gruppe="${gruppe}"]`).forEach((x) => x.classList.toggle('aktiv', x === k));
    document.querySelectorAll(`[data-pane="${gruppe}"]`).forEach((p) => p.classList.toggle('aktiv', p.id === k.dataset.ziel));
  });
})();
