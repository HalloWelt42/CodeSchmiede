// Daten und Zeichnungen der Kursentwürfe. Die Zeichnungen sind Platzhalter: bis zur Stilprobe steht ein Symbol in der
// Farbfamilie der Sprache, nur das Förderband der Pinguine (Kapitel 9) ist als Beispiel für die Bildsprache gezeichnet.

window.KURSE = {
  python: {
    titel: 'Python',
    bloecke: [
      { titel: 'Erste Schritte', kapitel: [
        [1, 'Hallo, Ausgabe', 'fa-bullhorn', 'fertig', 'Ein Papagei mit Megafon ruft laut, was man ihm auf einen Zettel schreibt'],
        [2, 'Werte und Variablen', 'fa-box', 'fertig', 'Umzugskartons mit Namensschildern, einer heißt punkte und quillt über'],
        [3, 'Rechnen', 'fa-calculator', 'fertig', 'Ein Rechenroboter teilt Kuchen, beim Rest bleiben Krümel übrig'],
        [4, 'Text', 'fa-font', 'uebersprungen', 'Buchstaben als Perlen auf einer Kette, eine Ente zählt sie ab'],
        [5, 'Werte umwandeln', 'fa-shuffle', 'fertig', 'Eine Verwandlungsmaschine: oben ein Zettel mit 42, unten fällt ein Klotz 42 heraus'],
      ] },
      { titel: 'Entscheiden und wiederholen', kapitel: [
        [6, 'Wahr und falsch', 'fa-scale-balanced', 'fertig', 'Eine Waage mit Daumen hoch und Daumen runter'],
        [7, 'Verzweigungen', 'fa-code-branch', 'fertig', 'Eine Weiche, der Zug mit Pinguinen fährt links oder rechts'],
        [8, 'Schleifen mit while', 'fa-rotate', 'fertig', 'Ein Hamster im Laufrad, der erst anhält, wenn der Wecker klingelt'],
        [9, 'Schleifen mit for', 'fa-fish', 'aktuell', 'Pinguine fahren auf einem Förderband an der Fischausgabe vorbei'],
      ] },
      { titel: 'Sammeln und ordnen', kapitel: [
        [10, 'Listen', 'fa-list-ol', 'zu', 'Ein Fächerregal mit nummerierten Fächern, das erste Fach hat die 0'],
        [11, 'Listen bearbeiten', 'fa-scissors', 'zu', 'Ein Koch schneidet eine Salami in Scheiben, von hier bis dort'],
        [12, 'Tupel und Entpacken', 'fa-cubes', 'zu', 'Eine Brotdose mit festen Fächern und festgeklebtem Deckel'],
        [13, 'Wörterbücher', 'fa-book', 'zu', 'Ein Schubladenschrank mit beschrifteten Schubladen'],
        [14, 'Mengen', 'fa-circle-nodes', 'zu', 'Ein Sack Murmeln, doppelte Murmeln hüpfen von selbst wieder heraus'],
      ] },
      { titel: 'Eigene Bausteine', kapitel: [
        [15, 'Funktionen', 'fa-gears', 'zu', 'Ein Waffeleisen: Teig hinein, Waffel heraus'],
        [16, 'Sichtbarkeit von Namen', 'fa-eye', 'zu', 'Ein Zimmer mit Spiegelfenster: von drinnen sieht man hinaus, von draußen nicht hinein'],
        [17, 'Fehlerbehandlung', 'fa-shield-halved', 'zu', 'Ein Trapezkünstler mit Sicherheitsnetz'],
        [18, 'Module', 'fa-toolbox', 'zu', 'Eine Werkzeugkiste, aus der man nur den passenden Schlüssel holt'],
      ] },
      { titel: 'Weiter hinaus', kapitel: [
        [19, 'Dateien', 'fa-folder-open', 'zu', 'Ein Eichhörnchen als Archivar vor einem Aktenschrank'],
        [20, 'Klassen', 'fa-robot', 'zu', 'Ein Bauplan und drei gebaute Roboter mit eigenen Namensschildern'],
      ] },
    ],
  },
  sql: {
    titel: 'SQL',
    bloecke: [
      { titel: 'Tabellen lesen', kapitel: [
        [1, 'Was ist eine Tabelle?', 'fa-table', 'fertig', 'Ein Karteikasten, jede Karte eine Zeile'],
        [2, 'Spalten wählen mit SELECT', 'fa-table-columns', 'fertig', 'Eine Schablone, die nur bestimmte Spalten durchlässt'],
        [3, 'Zeilen filtern mit WHERE', 'fa-filter', 'aktuell', 'Ein Sieb, durch das nur passende Karteikarten fallen'],
        [4, 'Sortieren und begrenzen', 'fa-arrow-down-wide-short', 'zu', 'Pinguine stellen sich der Größe nach auf'],
      ] },
      { titel: 'Zusammenfassen', kapitel: [
        [5, 'Zählen und Summen', 'fa-calculator', 'zu', 'Ein Zählwerk an der Tür einer Eisdiele'],
        [6, 'Gruppen mit GROUP BY', 'fa-layer-group', 'zu', 'Socken werden nach Farbe in Körbe sortiert'],
      ] },
      { titel: 'Tabellen verbinden', kapitel: [
        [7, 'Verknüpfen mit JOIN', 'fa-link', 'zu', 'Zwei Puzzleteile, die über eine Nummer zusammenpassen'],
        [8, 'Fehlende Partner', 'fa-link-slash', 'zu', 'Ein Tanzkurs, bei dem einer ohne Partner übrig bleibt'],
      ] },
    ],
  },
  javascript: {
    titel: 'JavaScript',
    bloecke: [
      { titel: 'Erste Schritte', kapitel: [
        [1, 'Ausgabe in der Konsole', 'fa-terminal', 'zu', 'Ein Leuchtturm, der Nachrichten in die Nacht blinkt'],
        [2, 'Werte, let und const', 'fa-box', 'zu', 'Ein Karton mit Deckel zum Öffnen und einer mit Schloss'],
        [3, 'Vergleiche und Wahrheit', 'fa-scale-balanced', 'zu', 'Zwei Waagen, eine streng, eine großzügig'],
      ] },
    ],
  },
  css: {
    titel: 'CSS',
    bloecke: [
      { titel: 'HTML lesen', kapitel: [
        [1, 'Elemente und Verschachtelung', 'fa-code', 'zu', 'Russische Puppen, jede hat ein Namensschild'],
        [2, 'Klassen und Attribute', 'fa-tags', 'zu', 'Gepäckanhänger an Koffern auf dem Förderband'],
      ] },
      { titel: 'Gestalten', kapitel: [
        [3, 'Selektoren treffen', 'fa-crosshairs', 'zu', 'Ein Bogenschütze zielt auf beschriftete Zielscheiben'],
        [4, 'Farben und Schrift', 'fa-palette', 'zu', 'Ein Maler streicht Buchstaben an'],
        [5, 'Das Kastenmodell', 'fa-vector-square', 'zu', 'Ein Bild im Rahmen mit Passepartout, mit Abstand an der Wand'],
        [6, 'Fluss und Anordnung', 'fa-table-cells', 'zu', 'Kisten, die sich in ein Regal sortieren'],
      ] },
    ],
  },
};

window.KAPITEL_LISTE = (sprache) => KURSE[sprache].bloecke.flatMap((b) => b.kapitel);

const MARKE = {
  fertig: ['fa-circle-check', 'Fertig'],
  aktuell: ['fa-circle-play', 'Weiter hier'],
  uebersprungen: ['fa-forward', 'Per Kurztest'],
  zu: ['fa-lock', 'Noch zu'],
};
window.MARKE = MARKE;

// Kleines Kartenbild für Listen
window.miniKarte = (icon, stand) => `<span class="mini-karte ${stand === 'zu' ? 'leer' : ''}"><i class="fa-solid ${stand === 'zu' ? 'fa-lock' : icon}"></i></span>`;

// Ein Pinguin als freigestellte Figur (Platzhalter für die Bildsprache)
const pinguin = (x, y, s = 1, mund = 0) => `
  <g transform="translate(${x} ${y}) scale(${s})">
    <ellipse cx="0" cy="34" rx="15" ry="4" fill="rgba(0,0,0,.18)"/>
    <ellipse cx="0" cy="12" rx="14" ry="20" fill="#2b3442"/>
    <ellipse cx="0" cy="16" rx="9" ry="14" fill="#f4f1ea"/>
    <circle cx="0" cy="-10" r="10" fill="#2b3442"/>
    <circle cx="-3.5" cy="-12" r="2.4" fill="#fff"/><circle cx="3.5" cy="-12" r="2.4" fill="#fff"/>
    <circle cx="-3" cy="-11.6" r="1.2" fill="#111"/><circle cx="4" cy="-11.6" r="1.2" fill="#111"/>
    <path d="M -4 -6 L 4 -6 L 0 ${-1 + mund} Z" fill="#f2a13b"/>
    <path d="M -13 6 Q -20 16 -14 24" stroke="#2b3442" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path d="M 13 6 Q 20 16 14 24" stroke="#2b3442" stroke-width="5" fill="none" stroke-linecap="round"/>
    <ellipse cx="-6" cy="32" rx="5" ry="2.5" fill="#f2a13b"/><ellipse cx="6" cy="32" rx="5" ry="2.5" fill="#f2a13b"/>
  </g>`;

const fisch = (x, y, s = 1, r = 0) => `
  <g transform="translate(${x} ${y}) rotate(${r}) scale(${s})">
    <ellipse cx="0" cy="0" rx="10" ry="5" fill="#7cc4e8"/>
    <path d="M 8 0 L 16 -6 L 16 6 Z" fill="#5aa9d4"/>
    <circle cx="-5" cy="-1" r="1.2" fill="#123"/>
  </g>`;

// Förderband mit drei Pinguinen und der Fischausgabe: "for pinguin in kolonie"
window.pinguinBand = (mitFisch = 1) => `
  <svg viewBox="0 0 260 170" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Pinguine auf einem Förderband an der Fischausgabe">
    <rect x="10" y="118" width="200" height="22" rx="11" fill="#48505c"/>
    <rect x="16" y="122" width="188" height="14" rx="7" fill="#5e6774"/>
    ${[24, 52, 80, 108, 136, 164, 192].map((x) => `<circle cx="${x}" cy="129" r="5" fill="#3a414b"/><circle cx="${x}" cy="129" r="1.6" fill="#8b94a1"/>`).join('')}
    <path d="M 30 150 L 190 150" stroke="var(--s-b, #4f8fd6)" stroke-width="3" stroke-dasharray="7 6"/>
    <path d="M 190 150 l -9 -5 v 10 Z" fill="var(--s-b, #4f8fd6)"/>
    ${pinguin(42, 80, 1)}${pinguin(96, 80, 1)}${pinguin(150, 80, 1, mitFisch ? 2 : 0)}
    <rect x="200" y="40" width="50" height="78" rx="6" fill="var(--s-a, #f2b84b)"/>
    <rect x="207" y="48" width="36" height="22" rx="3" fill="#fff6dd"/>
    ${fisch(225, 59, .8)}
    <path d="M 200 92 L 178 92" stroke="#6b5520" stroke-width="4" stroke-linecap="round"/>
    ${mitFisch ? fisch(170, 96, .7, -20) : ''}
    <circle cx="225" cy="98" r="7" fill="#e5484d"/><circle cx="225" cy="98" r="3" fill="#ffb3b5"/>
  </svg>`;

// Platzhalter für Bilder, die erst nach der Stilprobe entstehen
window.platzhalter = (icon) => `<i class="fa-solid ${icon}"></i>`;

// Sammelkarte eines Kapitels
window.sammelkarte = (sprache, [nr, titel, icon, stand, motiv], kann, breite) => {
  const offen = stand === 'fertig' || stand === 'uebersprungen' || kann;
  if (!offen) return `<div class="sammelkarte verdeckt" data-sprache="${sprache}" ${breite ? `style="--breite:${breite}px"` : ''}><div class="kopf"><span>${titel}</span><span class="nr">${nr}</span></div><div class="bildfeld"><i class="fa-solid fa-lock"></i></div><div class="fuss-karte"><span>noch verdeckt</span></div></div>`;
  const bild = nr === 9 && sprache === 'python' ? pinguinBand() : platzhalter(icon);
  return `<div class="sammelkarte ${stand === 'fertig' ? '' : ''}" data-sprache="${sprache}" title="${motiv}" ${breite ? `style="--breite:${breite}px"` : ''}>
    <div class="kopf"><span>${titel}</span><span class="nr">${String(nr).padStart(2, '0')}</span></div>
    <div class="bildfeld">${bild}</div>
    ${kann ? `<div class="kann"><b>Kann ich jetzt</b>${kann}</div>` : ''}
    <div class="fuss-karte"><span>${KURSE[sprache].titel}</span><span>${stand === 'uebersprungen' ? 'Kurztest' : 'Kapitel'}</span></div>
  </div>`;
};

// Hervorhebung für Python-Zeilen der Entwürfe (genug für die Beispiele, kein vollständiger Zerleger)
window.pyZeile = (z) => z
  .replace(/(&quot;|")(.*?)(\1)/g, '<span class="cs">"$2"</span>')
  .replace(/\b(for|in|if|else|elif|while|def|return|print|range|len|True|False|None)\b(?![^<]*<\/span>)/g, (w) => (['print', 'range', 'len'].includes(w) ? `<span class="cf">${w}</span>` : `<span class="ck">${w}</span>`))
  .replace(/(#.*)$/, '<span class="cm">$1</span>')
  .replace(/\b(\d+)\b(?![^<]*<\/span>)/g, '<span class="cz">$1</span>');

window.codeBlock = (zeilen, opt = {}) => `<div class="code" ${opt.id ? `id="${opt.id}"` : ''}>${zeilen.map((z, i) => `<div data-zeile="${i + 1}" class="${(opt.klassen || {})[i + 1] || ''}"><span class="ln">${i + 1}</span><span>${opt.roh ? z : pyZeile(z)}</span></div>`).join('')}</div>`;

// Auswahlfrage oder Vorhersage: Knöpfe A bis D, Erklärung je Antwort, Rückruf nach der Wahl
window.wahlFrage = (ortId, erklOrtId, eintraege, beiWahl, mitPre = false) => {
  const ort = document.getElementById(ortId);
  ort.innerHTML = eintraege.map((e, i) => `<button class="wahlknopf" data-i="${i}"><kbd>${'ABCD'[i]}</kbd>${mitPre ? `<pre>${e.t}</pre>` : `<span>${e.t}</span>`}</button>`).join('');
  ort.querySelectorAll('.wahlknopf').forEach((b) => b.addEventListener('click', () => {
    const e = eintraege[Number(b.dataset.i)];
    ort.querySelectorAll('.wahlknopf').forEach((x) => x.classList.remove('richtig', 'falsch'));
    b.classList.add(e.richtig ? 'richtig' : 'falsch');
    document.getElementById(erklOrtId).innerHTML = `<div class="erklaerung ${e.richtig ? 'gut' : 'schlecht'}"><i class="fa-solid ${e.richtig ? 'fa-circle-check' : 'fa-lightbulb'}"></i><span>${e.erkl}</span></div>`;
    if (beiWahl) beiWahl(e);
  }));
};
