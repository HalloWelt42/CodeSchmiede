<script lang="ts">
  /*
   * Rechte Spalte: Ergebnis der Pruefung.
   * Bei Bestanden zeigt eine Erfolgs-Zeile mit Punkten und einem
   * Weiter-Button zur nächsten Aufgabe.
   * Stdout vom Nutzer-Code wird oben angezeigt, wenn nicht leer.
   */
  import type { SubmissionAntwort, TestErgebnis } from '../types/Submission';

  interface Props {
    ergebnis: SubmissionAntwort | null;
    fehler: string | null;
    laeuft: boolean;
    anzahl_versteckt: number;
    schwierigkeit_score: number;
    onWeiter: () => void;
  }

  let { ergebnis, fehler, laeuft, anzahl_versteckt, schwierigkeit_score, onWeiter }: Props = $props();

  function formatiereWert(wert: unknown): string {
    return JSON.stringify(wert);
  }
</script>

<div class="output">
  <header class="kopf">
    <span class="label">Ergebnis</span>
    {#if ergebnis}
      <span class="status" class:bestanden={ergebnis.bestanden}>
        <i class="fa-solid {ergebnis.bestanden ? 'fa-check' : 'fa-xmark'}" aria-hidden="true"></i>
        {ergebnis.bestanden ? 'Bestanden' : 'Noch nicht bestanden'}
      </span>
    {/if}
  </header>

  {#if laeuft}
    <div class="leer">
      <i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i>
      Code läuft im Container ...
    </div>
  {:else if fehler}
    <div class="leer fehler">
      <i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i>
      {fehler}
    </div>
  {:else if !ergebnis}
    <div class="leer">
      <i class="fa-solid fa-flask" aria-hidden="true"></i>
      Noch nicht geprüft. Klick auf <strong>Prüfen</strong> startet den Sandbox-Lauf.
    </div>
  {:else}
    {@const p = ergebnis.pruefung}

    {#if ergebnis.bestanden}
      <section class="erfolg">
        <div class="erfolg-info">
          <span class="punkte num">+{ergebnis.progress.punkte_erreicht}</span>
          <span class="punkte-text">von {schwierigkeit_score} Punkten</span>
        </div>
        <button type="button" class="weiter" onclick={onWeiter}>
          Weiter
          <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
        </button>
      </section>
    {/if}

    {#if p.stdout}
      <section class="block stdout-block">
        <h3>Standardausgabe</h3>
        <pre class="konsole">{p.stdout}</pre>
      </section>
    {/if}

    <section class="block">
      <h3>Sichtbare Tests</h3>
      <ul class="test-liste">
        {#each p.sichtbar as t (t.index)}
          <li class:bestanden={t.bestanden} class:fail={!t.bestanden}>
            <i class="fa-solid {t.bestanden ? 'fa-check' : 'fa-xmark'}" aria-hidden="true"></i>
            <code class="aufruf">f({t.eingabe.map(formatiereWert).join(', ')})</code>
            {#if t.bestanden}
              <span class="zeichen">=</span>
              <code class="wert">{formatiereWert(t.tatsaechlich)}</code>
            {:else if t.fehler}
              <span class="fehlertext">{t.fehler}</span>
            {:else}
              <span class="zeichen">→</span>
              <code class="wert ist">{formatiereWert(t.tatsaechlich)}</code>
              <span class="zeichen">≠</span>
              <code class="wert soll">{formatiereWert(t.erwartet)}</code>
            {/if}
          </li>
        {/each}
      </ul>
    </section>

    {#if anzahl_versteckt > 0}
      <section class="block">
        <h3>Versteckte Tests</h3>
        <div class="versteckt-zeile">
          <span class="versteckt-balken">
            {#each Array(anzahl_versteckt) as _, i}
              <span
                class="punkt"
                class:pass={i < p.versteckt_pass}
                class:fail={i >= p.versteckt_pass && i < p.versteckt_pass + p.versteckt_fail}
                title={i < p.versteckt_pass ? 'bestanden' : 'fehlgeschlagen'}
              ></span>
            {/each}
          </span>
          <span class="versteckt-stats num">
            {p.versteckt_pass} / {anzahl_versteckt}
          </span>
        </div>
      </section>
    {/if}

    {#if p.timeout}
      <section class="block warn">
        <i class="fa-solid fa-clock" aria-hidden="true"></i>
        Timeout -- der Code lief länger als erlaubt.
      </section>
    {/if}

    {#if p.stderr}
      <section class="block">
        <h3>Fehlerausgabe</h3>
        <pre class="konsole stderr">{p.stderr}</pre>
      </section>
    {/if}

    <section class="block performance">
      <h3>Performance</h3>
      <dl class="metrik">
        <div>
          <dt>Laufzeit</dt>
          <dd class="num">{p.laufzeit_ms.toFixed(0)} ms</dd>
        </div>
        <div>
          <dt>Codelänge</dt>
          <dd class="num">{ergebnis.codelaenge_zeichen} Zeichen</dd>
        </div>
        <div>
          <dt>Versuche</dt>
          <dd class="num">{ergebnis.progress.versuche}</dd>
        </div>
      </dl>
    </section>
  {/if}
</div>

<style>
  .output {
    display: flex;
    flex-direction: column;
    min-height: 0;
  }
  .kopf {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: var(--sp-2) var(--sp-3);
    border-bottom: 1px solid var(--border);
    background: var(--bg-card);
    flex-shrink: 0;
  }
  .label {
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .status {
    display: inline-flex;
    align-items: center;
    gap: var(--sp-2);
    color: var(--red);
    font-size: var(--fs-sm);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .status.bestanden { color: var(--green); }

  .leer {
    padding: var(--sp-5);
    color: var(--fg-dim);
    text-align: center;
    font-family: var(--quick);
    font-size: var(--fs-sm);
    display: flex;
    flex-direction: column;
    gap: var(--sp-3);
    align-items: center;
  }
  .leer i { font-size: var(--fs-xl); color: var(--fg-mute); }
  .leer.fehler { color: var(--red); }
  .leer.fehler i { color: var(--red); }

  .erfolg {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: var(--sp-3);
    background: color-mix(in srgb, var(--green) 10%, transparent);
    border-bottom: 1px solid var(--green);
  }
  .erfolg-info {
    display: flex;
    align-items: baseline;
    gap: var(--sp-2);
  }
  .punkte {
    color: var(--green);
    font-size: var(--fs-xl);
  }
  .punkte-text {
    color: var(--fg-dim);
    font-size: var(--fs-sm);
  }
  .weiter {
    background: var(--green);
    border: 1px solid var(--green);
    color: var(--bg);
    padding: 8px 14px;
    font-size: var(--fs-sm);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: var(--radius-sm);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: var(--sp-2);
  }
  .weiter:hover {
    filter: brightness(1.1);
  }

  .block {
    padding: var(--sp-3);
    border-bottom: 1px solid var(--border);
  }
  .block.stdout-block {
    background: var(--bg-card-2);
  }
  .block.warn {
    background: color-mix(in srgb, var(--orange) 10%, transparent);
    color: var(--orange);
    display: flex;
    align-items: center;
    gap: var(--sp-2);
  }
  h3 {
    font-family: var(--sans);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--fg-dim);
    margin: 0 0 var(--sp-2);
  }

  .test-liste {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: var(--sp-1);
  }
  .test-liste li {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    padding: 4px var(--sp-2);
    background: var(--bg);
    border: 1px solid var(--border);
    font-size: var(--fs-xs);
    flex-wrap: wrap;
  }
  .test-liste li.bestanden i { color: var(--green); }
  .test-liste li.fail i { color: var(--red); }
  .test-liste code {
    font-family: var(--mono);
    background: transparent;
    border: none;
    padding: 0;
    color: var(--fg);
  }
  .aufruf { color: var(--fg-dim) !important; }
  .wert.ist { color: var(--red) !important; }
  .wert.soll { color: var(--green) !important; }
  .zeichen { color: var(--fg-mute); }
  .fehlertext {
    color: var(--red);
    font-family: var(--mono);
    font-size: var(--fs-xs);
  }

  .versteckt-zeile {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
  }
  .versteckt-balken {
    display: inline-flex;
    gap: 4px;
    flex: 1;
  }
  .punkt {
    display: inline-block;
    width: 14px;
    height: 14px;
    border-radius: 2px;
    background: var(--bg);
    border: 1px solid var(--border);
  }
  .punkt.pass { background: var(--green); border-color: var(--green); }
  .punkt.fail { background: var(--red); border-color: var(--red); }
  .versteckt-stats {
    color: var(--fg-dim);
    font-size: var(--fs-sm);
  }

  .konsole {
    margin: 0;
    padding: var(--sp-2) var(--sp-3);
    background: var(--bg);
    border: 1px solid var(--border);
    font-family: var(--mono);
    font-size: var(--fs-xs);
    color: var(--fg);
    overflow-x: auto;
    white-space: pre-wrap;
    max-height: 200px;
    overflow-y: auto;
  }
  .konsole.stderr { color: var(--red); }

  .performance .metrik {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--sp-2);
    margin: 0;
  }
  .performance dt {
    color: var(--fg-mute);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .performance dd {
    margin: 2px 0 0;
    color: var(--fg);
    font-size: var(--fs-md);
  }
</style>
