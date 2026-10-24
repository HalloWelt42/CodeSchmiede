<script lang="ts">
  /*
   * Ergebnis der Prüfung: Rahmen mit Bestanden und Trefferzahl, je
   * sichtbarem Test eine Zeile, die versteckten nur als Anzahl, dazu
   * Ausgaben, Kennzahlen und der Vergleich mit den Musterlösungen.
   */
  import type { SubmissionAntwort } from '../types/Submission';

  interface Props {
    ergebnis: SubmissionAntwort | null;
    fehler: string | null;
    laeuft: boolean;
    anzahl_versteckt: number;
    schwierigkeit_score: number;
    onWeiter: () => void;
  }

  let { ergebnis, fehler, laeuft, anzahl_versteckt, schwierigkeit_score, onWeiter }: Props = $props();

  const wert = (w: unknown): string => JSON.stringify(w);
</script>

{#if laeuft}
  <p class="leer"><i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i><span>Code läuft in der Sandbox ...</span></p>
{:else if fehler}
  <p class="leer fehlertext"><i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i><span>{fehler}</span></p>
{:else if !ergebnis}
  <p class="leer"><i class="fa-solid fa-flask" aria-hidden="true"></i><span>Noch nicht geprüft. <strong>Prüfen</strong> startet den Lauf in der Sandbox.</span></p>
{:else}
  {@const p = ergebnis.pruefung}
  {@const bestandenSichtbar = p.sichtbar.filter((t) => t.bestanden).length}
  <div class="ergebnis-kopf" class:nein={!ergebnis.bestanden}>
    <i class="fa-solid {ergebnis.bestanden ? 'fa-circle-check' : 'fa-circle-xmark'}" aria-hidden="true"></i>
    {ergebnis.bestanden ? 'Bestanden' : 'Noch nicht bestanden'}
    <span class="num">{bestandenSichtbar + p.versteckt_pass} / {p.sichtbar.length + anzahl_versteckt}</span>
  </div>

  {#each p.sichtbar as t (t.index)}
    <div class="test-zeile">
      <i class="fa-solid {t.bestanden ? 'fa-check ok' : 'fa-xmark nein'}" aria-hidden="true"></i>
      <span class="aufruf">
        {t.eingabe.map(wert).join(', ')}
        {#if t.bestanden}
          -&gt; {wert(t.tatsaechlich)}
        {:else if t.fehler}
          <span class="fehlertext">{t.fehler}</span>
        {:else}
          -&gt; {wert(t.tatsaechlich)} <span class="fehlertext">statt {wert(t.erwartet)}</span>
        {/if}
      </span>
    </div>
  {/each}
  {#if anzahl_versteckt > 0}
    <div class="test-zeile">
      <i class="fa-solid {p.versteckt_fail === 0 ? 'fa-check ok' : 'fa-xmark nein'}" aria-hidden="true"></i>
      {p.versteckt_fail === 0
        ? `${anzahl_versteckt} versteckte Tests bestanden`
        : `${p.versteckt_pass} von ${anzahl_versteckt} versteckten Tests bestanden`}
    </div>
  {/if}

  {#if p.timeout}
    <p class="hinweis-box abstand"><i class="fa-solid fa-clock" aria-hidden="true"></i>Zeit überschritten: der Code lief länger als erlaubt.</p>
  {/if}
  {#if p.stdout}
    <div class="gruppe abstand">Standardausgabe</div>
    <pre class="konsole">{p.stdout}</pre>
  {/if}
  {#if p.stderr}
    <div class="gruppe abstand">Fehlerausgabe</div>
    <pre class="konsole fehlertext">{p.stderr}</pre>
  {/if}

  <p class="dim kennzahlen-text">
    Laufzeit {p.laufzeit_ms.toFixed(0)} ms, {ergebnis.codelaenge_zeichen} Zeichen, {ergebnis.progress.versuche}. Versuch{#if ergebnis.bestanden}, +{ergebnis.progress.punkte_erreicht} von {schwierigkeit_score} Punkten{/if}
  </p>
  {#if ergebnis.bestanden}
    <button class="knopf primaer" onclick={onWeiter}>
      <i class="fa-solid fa-forward" aria-hidden="true"></i>Nächste Aufgabe
    </button>
  {/if}

  {#if ergebnis.vergleich.length > 0}
    {@const maxZeit = Math.max(p.laufzeit_ms, ...ergebnis.vergleich.map((v) => v.laufzeit_ms))}
    {@const maxLaenge = Math.max(ergebnis.codelaenge_zeichen, ...ergebnis.vergleich.map((v) => v.codelaenge_zeichen))}
    {@const zeilen = [
      { name: 'deine Lösung', zeit: p.laufzeit_ms, laenge: ergebnis.codelaenge_zeichen, eigen: true },
      ...ergebnis.vergleich.map((v) => ({ name: v.variante, zeit: v.laufzeit_ms, laenge: v.codelaenge_zeichen, eigen: false })),
    ]}
    <div class="gruppe abstand">Vergleich mit den Musterlösungen</div>
    <div class="vergleich">
      <span class="spalte-titel"></span><span class="spalte-titel">Laufzeit</span><span class="spalte-titel">Zeichen</span>
      {#each zeilen as z (z.name)}
        <span class="name" class:eigen={z.eigen}>{z.name}</span>
        <span class="wert-zelle">
          <span class="balken"><span style:width="{maxZeit ? (z.zeit / maxZeit) * 100 : 0}%"></span></span>
          <span class="num">{z.zeit.toFixed(0)} ms</span>
        </span>
        <span class="wert-zelle">
          <span class="balken"><span style:width="{maxLaenge ? (z.laenge / maxLaenge) * 100 : 0}%"></span></span>
          <span class="num">{z.laenge}</span>
        </span>
      {/each}
    </div>
  {/if}
{/if}

<style>
  .leer {
    margin: var(--sp-4) 0;
    color: var(--fg-dim);
    font-family: var(--quick);
    font-size: var(--fs-sm);
    display: flex;
    gap: var(--sp-2);
    align-items: baseline;
  }
  .leer i { color: var(--fg-mute); }
  .fehlertext { color: var(--red); }
  .aufruf {
    min-width: 0;
    overflow-wrap: anywhere;
  }
  .abstand { margin-top: var(--sp-3); }
  .konsole {
    margin: 0;
    padding: var(--sp-2);
    background: var(--bg);
    border: 1px solid var(--border);
    font-family: var(--mono);
    font-size: 12px;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    max-height: 180px;
    overflow-y: auto;
  }
  .kennzahlen-text {
    font-size: var(--fs-sm);
    margin: var(--sp-2) 0;
  }
  .vergleich {
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr);
    gap: 4px var(--sp-2);
    align-items: center;
    font-size: var(--fs-xs);
  }
  .spalte-titel {
    color: var(--fg-mute);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .name {
    color: var(--fg-dim);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .name.eigen { color: var(--accent); }
  .wert-zelle {
    display: grid;
    grid-template-columns: minmax(0, 1fr) auto;
    gap: 6px;
    align-items: center;
  }
  .wert-zelle .num {
    font-weight: 500;
    min-width: 44px;
    text-align: right;
  }
</style>
