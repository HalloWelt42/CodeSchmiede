// Entwurf Ausgabe-Sprint: zehn Schnipsel gegen die Uhr, Kette, Auswertung mit Erklärung (nur Entwurf, Antworten im Browser)
window.SCHNIPSEL = [
  { code: 'print(3 * "ab")', optionen: ['ababab', 'ab3', '3ab', 'Fehler'], richtig: 0, warum: 'Ein Text mal einer Zahl wiederholt den Text.' },
  { code: 'x = [1, 2, 3]\ny = x\ny.append(4)\nprint(len(x))', optionen: ['3', '4', 'Fehler', 'None'], richtig: 1, warum: 'y ist kein neues Objekt, sondern ein zweiter Name für dieselbe Liste.' },
  { code: 'print(0.1 + 0.2 == 0.3)', optionen: ['True', 'False', '0.3', 'Fehler'], richtig: 1, warum: '0.1 und 0.2 sind im Binärsystem nicht genau darstellbar; die Summe ist 0.30000000000000004.' },
  { code: 'print(bool([]), bool([0]))', optionen: ['False False', 'False True', 'True True', 'True False'], richtig: 1, warum: 'Eine leere Liste ist falsch, eine Liste mit einem Element ist wahr, egal welches Element.' },
  { code: 'for i in range(2, 8, 3):\n    print(i, end=" ")', optionen: ['2 5', '2 5 8', '2 4 6', '3 6'], richtig: 0, warum: 'range endet vor 8: 2, dann 5, dann wäre 8 schon außerhalb.' },
  { code: 'print("Code"[1:3])', optionen: ['Co', 'od', 'ode', 'o'], richtig: 1, warum: 'Der Ausschnitt beginnt bei Stelle 1 und endet vor Stelle 3.' },
  { code: 'a, b = 5, 2\nprint(a // b, a % b)', optionen: ['2 1', '2.5 1', '2 2', '3 1'], richtig: 0, warum: '// ist ganzzahlige Division, % der Rest.' },
  { code: 'print(max("Apfel", "apfel"))', optionen: ['Apfel', 'apfel', 'Fehler', 'True'], richtig: 1, warum: 'Kleinbuchstaben stehen im Zeichensatz hinter den Großbuchstaben.' },
  { code: 'd = {"a": 1}\nprint(d.get("b", 0) + 1)', optionen: ['1', '2', 'Fehler', 'None'], richtig: 0, warum: 'get liefert die Vorgabe 0, wenn der Schlüssel fehlt.' },
  { code: 'print(sorted([3, 1, 2])[-1])', optionen: ['1', '2', '3', '[3]'], richtig: 2, warum: '-1 ist das letzte Element der sortierten Liste.' },
];

window.sprintStarten = function (wurzel) {
  const DAUER = 90;
  let nr = 0, kette = 0, besteKette = 0, rest = DAUER, antworten = [], takt;
  const telefon = document.documentElement.dataset.geraet === 'telefon';

  function frage() {
    const s = SCHNIPSEL[nr];
    wurzel.innerHTML = `
      <div class="sprint-kopf"><span>Frage <span class="num">${nr + 1} / 10</span></span>
        <span><i class="fa-regular fa-clock"></i> <span class="num" id="rest">${rest}</span> s</span>
        <span class="kette"><i class="fa-solid fa-link"></i> Kette ${kette}</span></div>
      <div class="uhr"><span id="uhr" style="width:${(rest / DAUER) * 100}%"></span></div>
      <div class="gruppe" style="margin:0">Was gibt dieser Code aus?</div>
      <pre class="schnipsel">${s.code.replace(/</g, '&lt;')}</pre>
      <div class="antworten">${s.optionen.map((o, i) => `<button class="antwort" data-i="${i}"><kbd>${i + 1}</kbd><span>${o}</span></button>`).join('')}</div>
      ${telefon ? '' : '<p class="dim" style="font-size:var(--fs-sm);margin:0;text-align:center">Tasten 1 bis 4 wählen eine Antwort</p>'}`;
    wurzel.querySelectorAll('.antwort').forEach((b) => (b.onclick = () => waehlen(+b.dataset.i)));
  }

  function waehlen(i) {
    const s = SCHNIPSEL[nr];
    const ok = i === s.richtig;
    kette = ok ? kette + 1 : 0;
    besteKette = Math.max(besteKette, kette);
    antworten.push({ ok, gewaehlt: i });
    wurzel.querySelectorAll('.antwort').forEach((b) => {
      b.disabled = true;
      if (+b.dataset.i === s.richtig) b.classList.add('richtig');
      else if (+b.dataset.i === i) b.classList.add('falsch');
    });
    setTimeout(() => { nr++; nr < SCHNIPSEL.length && rest > 0 ? frage() : auswertung(); }, ok ? 450 : 1100);
  }

  function auswertung() {
    clearInterval(takt);
    const richtig = antworten.filter((a) => a.ok).length;
    const sterne = richtig >= 10 ? 3 : richtig >= 8 ? 2 : richtig >= 6 ? 1 : 0;
    const punkte = Math.round((15 * sterne) / 3);
    wurzel.innerHTML = `
      <div class="belohnung">
        <div class="belohnung-kopf"><span class="plus">+${punkte}</span><span>${richtig} von 10 richtig, längste Kette ${besteKette}</span></div>
        <div class="zeile"><span class="sterne gross">${[1, 2, 3].map((k) => `<i class="fa-solid fa-star ${k <= sterne ? '' : 'aus'}"></i>`).join('')}</span></div>
        <div class="zeile"><i class="fa-solid fa-bullseye"></i>Tagesauftrag: Spiel-Level erledigt (2 / 3)</div>
      </div>
      <div class="gruppe" style="margin:0">Auswertung</div>
      <div>${SCHNIPSEL.slice(0, antworten.length).map((s, k) => {
        const a = antworten[k];
        return `<div class="auswertung-zeile"><i class="fa-solid ${a.ok ? 'fa-check ok' : 'fa-xmark nein'}"></i><div>
          <pre>${s.code.replace(/</g, '&lt;')}</pre>
          ${a.ok ? `<span class="dim">${s.optionen[s.richtig]}</span>` : `<span>Richtig: <b>${s.optionen[s.richtig]}</b>, gewählt: ${s.optionen[a.gewaehlt]}</span><div class="erklaerung">${s.warum}</div>`}
        </div></div>`;
      }).join('')}</div>
      <div style="display:flex;gap:var(--sp-2)"><button class="knopf voll" id="neu"><i class="fa-solid fa-rotate"></i>Neue Runde</button><button class="knopf"><i class="fa-solid fa-arrow-left"></i>Zu den Spielen</button></div>`;
    wurzel.querySelector('#neu').onclick = () => starten();
  }

  function starten() {
    nr = 0; kette = 0; besteKette = 0; rest = DAUER; antworten = [];
    clearInterval(takt);
    takt = setInterval(() => {
      rest--;
      const r = wurzel.querySelector('#rest'), u = wurzel.querySelector('#uhr');
      if (r) r.textContent = rest;
      if (u) u.style.width = `${(rest / DAUER) * 100}%`;
      if (rest <= 0) auswertung();
    }, 1000);
    frage();
  }

  document.addEventListener('keydown', (e) => {
    const b = wurzel.querySelector(`.antwort[data-i="${+e.key - 1}"]`);
    if (b && !b.disabled) b.click();
  });
  starten();
};
