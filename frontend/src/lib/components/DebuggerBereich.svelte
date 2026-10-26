<script lang="ts">
  /*
   * Debugger in der rechten Spalte einer Aufgabe (nur am Rechner): Steuerleiste, Zeitleiste aller Schritte,
   * Aufrufstapel, Speicher und Ausgabe bis zum gezeigten Schritt. Der Lauf ist eine fertige Aufzeichnung, darum geht
   * jeder Schritt auch rückwärts. Die gezeigte Zeile meldet die Komponente nach außen, der Editor markiert sie.
   */
  import { untrack } from 'svelte';
  import type { DebugSitzung } from '../debugger/sitzung.svelte';
  import { aufrufstapel, istEintritt, istHalt, springe, start, tiefe, type Ziel } from '../debugger/steuerung';
  import KursFlaeche from './kurs/KursFlaeche.svelte';
  import Speicherbild from './kurs/Speicherbild.svelte';

  interface Props {
    sitzung: DebugSitzung;
    sprache: string;
    /** Code im Editor; weicht er vom aufgezeichneten ab, ist der Lauf veraltet */
    code: string;
    /** gezeigte Zeile, solange der Lauf zum Code passt */
    zeile?: number | null;
  }
  let { sitzung, sprache, code, zeile = $bindable(null) }: Props = $props();

  let i = $state(0);
  let lauf = $derived(sitzung.lauf);
  let schritte = $derived(lauf?.schritte ?? []);
  let halte = $derived(new Set(sitzung.haltepunkte));
  let veraltet = $derived(sitzung.veraltet(code));
  let aktuell = $derived(schritte[i] ?? null);
  let amEnde = $derived(i === schritte.length - 1);
  let eintritt = $derived(istEintritt(schritte, i));
  let stapel = $derived(aktuell ? aufrufstapel(schritte, i, sitzung.aufruf !== null) : []);
  let ausgabeBisher = $derived(schritte.slice(0, i + 1).map((s) => s.ausgabe).join(''));
  let treffer = $derived(schritte.flatMap((_, k) => (istHalt(schritte, k, halte) ? [k] : [])));
  let maxTiefe = $derived(Math.max(1, ...schritte.map(tiefe)));

  // neuer Lauf: am ersten Haltepunkt beginnen; spätere Änderungen an den Haltepunkten springen nicht
  $effect(() => {
    void sitzung.nummer;
    untrack(() => (i = start(sitzung.lauf?.schritte ?? [], new Set(sitzung.haltepunkte))));
  });
  $effect(() => {
    zeile = aktuell && !veraltet ? aktuell.zeile : null;
  });

  function gehe(ziel: Ziel) {
    if (schritte.length) i = springe(ziel, schritte, i, halte);
  }

  const KNOEPFE: { ziel: Ziel; icon: string; titel: string; halt?: boolean; trenner?: boolean }[] = [
    { ziel: 'anfang', icon: 'fa-backward-fast', titel: 'Zum Anfang' },
    { ziel: 'zurueckHalt', icon: 'fa-backward', titel: 'Zurück zum vorigen Haltepunkt', halt: true },
    { ziel: 'zurueck', icon: 'fa-backward-step', titel: 'Einen Schritt zurück', trenner: true },
    { ziel: 'hinein', icon: 'fa-arrow-turn-down', titel: 'Schritt hinein: die nächste Zeile, auch in eine Funktion' },
    { ziel: 'ueber', icon: 'fa-share', titel: 'Schritt über: Funktionsaufrufe in einem Zug' },
    { ziel: 'hinaus', icon: 'fa-arrow-turn-up', titel: 'Schritt hinaus: bis die Funktion zurückkehrt' },
    { ziel: 'weiterHalt', icon: 'fa-forward', titel: 'Weiter bis zum nächsten Haltepunkt', halt: true },
    { ziel: 'ende', icon: 'fa-forward-fast', titel: 'Zum Ende' },
  ];

  let leiste: HTMLDivElement | undefined = $state();
  function klickLeiste(e: MouseEvent) {
    if (!leiste || !schritte.length) return;
    const r = leiste.getBoundingClientRect();
    i = Math.min(schritte.length - 1, Math.max(0, Math.floor(((e.clientX - r.left) / r.width) * schritte.length)));
  }
  function tasteLeiste(e: KeyboardEvent) {
    const ziel: Partial<Record<string, Ziel>> = { ArrowLeft: 'zurueck', ArrowRight: 'hinein', Home: 'anfang', End: 'ende' };
    const z = ziel[e.key];
    if (!z) return;
    e.preventDefault();
    gehe(z);
  }
  const anteil = (k: number) => `${(k / Math.max(1, schritte.length)) * 100}%`;
  const rahmenName = (name: string) => (name === 'Modul' ? 'Hauptprogramm' : `${name}()`);
</script>

<KursFlaeche>
  <div class="debugger" data-sprache={sprache}>
    {#if sitzung.laeuft}
      <p class="dim"><i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i> Zeichne den Lauf auf ...</p>
    {:else if sitzung.fehler}
      <div class="erklaerung schlecht"><i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i><span>{sitzung.fehler}</span></div>
    {/if}

    {#if lauf && !sitzung.laeuft}
      {#if veraltet}
        <div class="veraltet">
          <i class="fa-solid fa-pen" aria-hidden="true"></i><span>Code geändert: die Aufzeichnung zeigt den alten Stand.</span>
          <button class="knopf" onclick={() => sitzung.neu(code)}><i class="fa-solid fa-rotate-right" aria-hidden="true"></i>Neu</button>
        </div>
      {/if}

      {#if schritte.length}
        <div class="steuer">
          {#each KNOEPFE as k (k.ziel)}
            <button class="ikon" class:halt-ikon={k.halt} onclick={() => gehe(k.ziel)} title={k.titel} aria-label={k.titel}><i class="fa-solid {k.icon}" aria-hidden="true"></i></button>
            {#if k.trenner}<span class="trenn"></span>{/if}
          {/each}
          <button class="ikon stopp" onclick={() => sitzung.beenden()} title="Debugger beenden" aria-label="Debugger beenden"><i class="fa-solid fa-stop" aria-hidden="true"></i></button>
        </div>

        <div class="stand">
          <span>Schritt <b class="num">{i + 1}</b> von <span class="num">{schritte.length}</span></span>
          {#if aktuell && eintritt}<span>Zeile <b class="num">{aktuell.zeile}</b> ruft {rahmenName(stapel[0].name)} auf</span>
          {:else if aktuell && amEnde && lauf.fehler && lauf.fehlerzeile === aktuell.zeile}<span class="fehler-text">Zeile <b class="num">{aktuell.zeile}</b> bricht mit einem Fehler ab</span>
          {:else if aktuell}<span>Zeile <b class="num">{aktuell.zeile}</b> ausgeführt</span>{/if}
          {#if treffer.includes(i)}<span class="halt-text"><i class="fa-solid fa-circle" aria-hidden="true"></i> Haltepunkt</span>{/if}
        </div>
        {#if halte.size && !treffer.length}<p class="hinweis dim">Kein Haltepunkt wurde erreicht, der Debugger steht am Ende.</p>{/if}

        <div class="zeitleiste" bind:this={leiste} onclick={klickLeiste} onkeydown={tasteLeiste} role="slider" tabindex="0"
             aria-label="Schritt in der Zeitleiste" aria-valuemin={1} aria-valuemax={schritte.length} aria-valuenow={i + 1}
             title="Jeder Strich ist ein Schritt; je höher, desto tiefer im Aufruf">
          <svg viewBox="0 0 {schritte.length} {maxTiefe + 1}" preserveAspectRatio="none" aria-hidden="true">
            {#each schritte as s, k (k)}
              <rect x={k + 0.15} width={0.7} y={maxTiefe - tiefe(s)} height={tiefe(s) + 1} class:war={k < i} />
            {/each}
          </svg>
          {#each treffer as k (k)}<span class="treffer" style:left="calc({anteil(k + 0.5)} - 3px)"></span>{/each}
          <span class="jetzt" style:left={anteil(i)} style:width="max(3px, {anteil(1)})"></span>
        </div>
        <div class="legende-dbg">
          <span><i class="fa-solid fa-circle halt-farbe" aria-hidden="true"></i>hält am Haltepunkt</span>
          <span><i class="fa-solid fa-square jetzt-farbe" aria-hidden="true"></i>jetzt</span>
          <span>höher heißt tiefer im Aufruf</span>
        </div>

        <div class="block-kopf"><span>Aufrufstapel</span></div>
        <div class="stapel">
          {#each stapel as r, n (n)}
            <div><span>{rahmenName(r.name)}</span><span>{n === 0 && eintritt ? 'wird aufgerufen' : r.zeile === null ? '' : n === 0 ? `Zeile ${r.zeile}` : `wartet in Zeile ${r.zeile}`}</span></div>
          {/each}
        </div>

        <Speicherbild schritt={aktuell} vorher={i > 0 ? schritte[i - 1] : null} innenZuerst />

        <div class="block-kopf"><span>Ausgabe bis hier</span></div>
        <pre class="ausgabe konsole">{#if ausgabeBisher}{ausgabeBisher}{:else}<span class="leer">Noch keine Ausgabe</span>{/if}</pre>
      {/if}

      {#if lauf.gekuerzt}<p class="hinweis dim">Aufzeichnung nach {schritte.length} Schritten gekürzt; der Code lief trotzdem zu Ende.</p>{/if}
      {#if lauf.zeitueberschreitung}<p class="hinweis dim">Zeit überschritten: der Lauf wurde abgebrochen.</p>{/if}
      {#if lauf.fehler && (amEnde || !schritte.length)}
        <div class="erklaerung schlecht"><i class="fa-solid fa-bug" aria-hidden="true"></i><span>{lauf.fehler}{lauf.fehlerzeile ? ` (Zeile ${lauf.fehlerzeile})` : ''}</span></div>
      {:else if amEnde && lauf.rueckgabe && sitzung.aufruf}
        <div class="rueckgabe-zeile"><i class="fa-solid fa-flag-checkered" aria-hidden="true"></i><span>{sitzung.aufruf} gibt <b>{lauf.rueckgabe.darstellung}</b> zurück</span></div>
      {/if}
    {/if}
  </div>
</KursFlaeche>

<style>
  .debugger { display: flex; flex-direction: column; gap: var(--sp-3); }
  .debugger > * { flex-shrink: 0; }
  .debugger :global(.block-kopf) { margin-bottom: calc(-1 * var(--sp-2)); }
  .steuer { display: flex; flex-wrap: wrap; gap: 3px; align-items: center; }
  .steuer .ikon { width: 30px; height: 30px; }
  .halt-ikon i, .halt-text, .halt-farbe { color: var(--ed-haltepunkt); }
  .trenn { width: 1px; height: 22px; background: var(--border); margin: 0 3px; }
  .stopp { margin-left: auto; }
  .stand { display: flex; flex-wrap: wrap; gap: var(--sp-2) var(--sp-3); align-items: baseline; font-size: var(--fs-sm); color: var(--fg-dim); }
  .stand b { color: var(--fg); }
  .stand .fehler-text, .stand .fehler-text b { color: var(--orange); }
  .hinweis { margin: 0; font-size: var(--fs-xs); }
  .zeitleiste { position: relative; height: 46px; padding-top: 10px; border-bottom: 1px solid var(--border); cursor: pointer; }
  .zeitleiste:focus-visible { outline: 1px solid var(--accent); outline-offset: 2px; }
  .zeitleiste svg { display: block; width: 100%; height: 100%; }
  .zeitleiste rect { fill: color-mix(in srgb, var(--accent) 35%, transparent); }
  .zeitleiste rect.war { fill: color-mix(in srgb, var(--accent) 70%, transparent); }
  .zeitleiste .jetzt { position: absolute; top: 10px; bottom: 0; background: var(--gold); pointer-events: none; }
  .zeitleiste .treffer { position: absolute; top: 0; width: 6px; height: 6px; border-radius: 50%; background: var(--ed-haltepunkt); pointer-events: none; }
  .legende-dbg { display: flex; flex-wrap: wrap; gap: var(--sp-3); margin-top: calc(-1 * var(--sp-2)); font-size: var(--fs-xs); color: var(--fg-mute); }
  .legende-dbg i { margin-right: 4px; }
  .jetzt-farbe { color: var(--gold); }
  .stapel { display: flex; flex-direction: column; border: 1px solid var(--border); }
  .stapel div { display: flex; justify-content: space-between; gap: var(--sp-2); padding: 4px var(--sp-2); font-family: var(--mono); font-size: 13px; border-top: 1px solid var(--border); }
  .stapel div:first-child { border-top: 0; background: color-mix(in srgb, var(--accent) 10%, transparent); color: var(--fg); }
  .stapel div span:last-child { color: var(--fg-mute); font-family: var(--sans); font-size: var(--fs-xs); white-space: nowrap; }
  .konsole { border-top: 1px solid var(--border); max-height: 200px; overflow-y: auto; }
  .veraltet { display: flex; align-items: center; gap: var(--sp-2); padding: var(--sp-2); border: 1px solid var(--orange); color: var(--orange); font-size: var(--fs-sm); }
  .veraltet .knopf { margin-left: auto; height: 26px; }
  .rueckgabe-zeile { display: flex; align-items: center; gap: var(--sp-2); padding: var(--sp-2); border: 1px solid var(--accent); background: color-mix(in srgb, var(--accent) 8%, transparent); font-family: var(--mono); font-size: 14px; overflow-wrap: anywhere; }
  .rueckgabe-zeile i { color: var(--accent); }
  /* die rechte Spalte ist schmaler als die Kursseite */
  .debugger :global(.fach span) { min-width: 40px; }
  .debugger :global(.speicher-name) { overflow-wrap: anywhere; }
</style>
