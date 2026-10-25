<script lang="ts">
  /*
   * Ergebnis der Prüfung: Rahmen mit Bestanden und Trefferzahl, je
   * sichtbarem Test eine Zeile, die versteckten nur als Anzahl, dazu
   * Ausgaben, Kennzahlen und der Vergleich mit den Musterlösungen.
   */
  import type { SubmissionAntwort } from '../types/Submission';
  import BelohnungsBand from './spiel/BelohnungsBand.svelte';

  interface Props {
    ergebnis: SubmissionAntwort | null;
    fehler: string | null;
    laeuft: boolean;
    anzahl_versteckt: number;
    /** Programm-Aufgabe: Ausgaben Zeile für Zeile vergleichen statt Rückgaben */
    programm?: boolean;
    onWeiter: () => void;
  }

  let { ergebnis, fehler, laeuft, anzahl_versteckt, programm = false, onWeiter }: Props = $props();

  const wert = (w: unknown): string => JSON.stringify(w);
  const zeilenVon = (w: unknown): string[] => String(w ?? '').replace(/\s+$/, '').split('\n').map((z) => z.replace(/\s+$/, ''));
  /** erste Zeile (ab 1), in der die Ausgabe abweicht */
  function ersteAbweichung(erwartet: unknown, tatsaechlich: unknown): number {
    const a = zeilenVon(erwartet);
    const b = zeilenVon(tatsaechlich);
    for (let i = 0; i < Math.max(a.length, b.length); i++) if (a[i] !== b[i]) return i + 1;
    return 0;
  }
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
  {#if ergebnis.belohnung}<BelohnungsBand belohnung={ergebnis.belohnung} />{/if}
  <div class="ergebnis-kopf" class:nein={!ergebnis.bestanden}>
    <i class="fa-solid {ergebnis.bestanden ? 'fa-circle-check' : 'fa-circle-xmark'}" aria-hidden="true"></i>
    {ergebnis.bestanden ? 'Bestanden' : 'Noch nicht bestanden'}
    <span class="num">{bestandenSichtbar + p.versteckt_pass} / {p.sichtbar.length + anzahl_versteckt}</span>
  </div>

  {#each p.sichtbar as t (t.index)}
    {#if programm}
      {@const ab = t.bestanden ? 0 : ersteAbweichung(t.erwartet, t.tatsaechlich)}
      <div class="programm-ergebnis">
        <div class="test-zeile"><i class="fa-solid {t.bestanden ? 'fa-check ok' : 'fa-xmark nein'}" aria-hidden="true"></i>
          {#if t.eingabe.length}<span class="dim">Eingabe {t.eingabe.join(', ')}:</span>{/if}
          {t.bestanden ? 'Ausgabe stimmt' : t.fehler ? '' : `Ausgabe weicht ab Zeile ${ab} ab`}
          {#if t.fehler}<span class="fehlertext">{t.fehler}</span>{/if}
        </div>
        {#if !t.bestanden}
          <div class="vergleich-zeilen">
            <div><span class="etikett">Erwartet</span><pre>{#each zeilenVon(t.erwartet) as z, i (i)}<span class:ab={i + 1 === ab}>{z || ' '}</span>{'\n'}{/each}</pre></div>
            <div><span class="etikett">Deine Ausgabe</span><pre>{#each zeilenVon(t.tatsaechlich) as z, i (i)}<span class:ab={i + 1 === ab}>{z || ' '}</span>{'\n'}{/each}</pre></div>
          </div>
        {/if}
      </div>
    {:else}
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
    {/if}
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
    Laufzeit {p.laufzeit_ms.toFixed(0)} ms, {ergebnis.codelaenge_zeichen} Zeichen, {ergebnis.progress.versuche}. Versuch
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
  .vergleich-zeilen { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: var(--sp-2); margin: 4px 0 var(--sp-2); }
  .vergleich-zeilen .etikett { font-size: var(--fs-xs); text-transform: uppercase; letter-spacing: .05em; color: var(--fg-mute); }
  .vergleich-zeilen pre { margin: 2px 0 0; padding: var(--sp-2); background: var(--bg); border: 1px solid var(--border); font-family: var(--mono); font-size: 12px; white-space: pre-wrap; overflow-wrap: anywhere; }
  .vergleich-zeilen .ab { background: color-mix(in srgb, var(--red) 22%, transparent); }
</style>
