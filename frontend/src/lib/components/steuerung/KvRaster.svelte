<script lang="ts">
  /*
   * KV-Diagramm als Editor: Blöcke ziehen (auch über den Rand, dann geht es auf der anderen Seite weiter), mit einem
   * Klick löschen, oder die Formel als Text schreiben. Jeder Block ist ein Term; alles schreibt den Text der Formel.
   * Mehrere Ausgänge haben je ein Raster, oben wählbar. Ein Feld zeigt 1, 0 oder x (egal); Felder in einem Block sind
   * hinterlegt, das gewählte Feld ist weiß umrandet.
   */
  import { felder, mitTermen, raster, rechtecke, spanne, termText, zerlege, zusammen, blockAus, type Stellen } from '../../steuerung/kv';
  import type { KvAnsicht } from '../../types/Kv';
  import type { CodeZugriff } from '../../types/Steuerung';
  import EditorBereich from '../EditorBereich.svelte';

  interface Props {
    ansicht: KvAnsicht;
    zugriff: CodeZugriff;
    /** gewählte Belegung */
    gewaehlt: number;
    waehle: (belegung: number) => void;
  }
  let { ansicht, zugriff, gewaehlt, waehle }: Props = $props();

  const S = 76;
  const X0 = 86;
  const Y0 = 64;
  const FARBEN = ['#34d399', '#f472b6', '#60a5fa', '#f59e0b', '#a78bfa', '#f87171', '#2dd4bf', '#facc15'];

  // svelte-ignore state_referenced_locally
  let ausgang = $state(ansicht.ausgaenge[0]);
  let art = $state<'ziehen' | 'loeschen' | 'text'>('ziehen');
  let zug = $state<{ z0: number; s0: number; z1: number; s1: number } | null>(null);
  let svg: SVGSVGElement | undefined = $state();

  let r = $derived(raster(ansicht.eingaenge));
  let zeilen = $derived(zerlege(zugriff.code, ansicht.eingaenge, ansicht.ausgaenge));
  let terme = $derived((zeilen.find((z) => z.art === 'formel' && z.name === ausgang) as { terme: Stellen[] } | undefined)?.terme ?? []);
  let abgedeckt = $derived(new Set(terme.flatMap((t) => felder(t))));
  let breite = $derived(X0 + r.spalten * S + 40);
  let hoehe = $derived(Y0 + r.zeilen * S + 40);
  let werte = $derived(ansicht.werte[ausgang]);

  /** Felder des gezogenen Bereichs, null wenn keine Zweierpotenz */
  let auswahl = $derived.by(() => {
    if (!zug) return null;
    const zs = spanne(zug.z0, zug.z1, r.zeilen);
    const ss = spanne(zug.s0, zug.s1, r.spalten);
    return zs && ss ? zs.flatMap((z) => ss.map((s) => r.belegung(z, s))) : null;
  });
  /** alle überstrichenen Felder, auch wenn der Bereich nicht erlaubt ist (dann rot) */
  let ueberstrichen = $derived.by(() => {
    if (!zug) return new Set<number>();
    const roh = (a: number, b: number, l: number) =>
      Array.from({ length: Math.min(Math.abs(b - a) + 1, l) }, (_, k) => (((a + k * (b >= a ? 1 : -1)) % l) + l) % l);
    const z = zug;
    return new Set(roh(z.z0, z.z1, r.zeilen).flatMap((zi) => roh(z.s0, z.s1, r.spalten).map((si) => r.belegung(zi, si))));
  });

  function lage(e: PointerEvent): [number, number] {
    const m = svg?.getScreenCTM();
    if (!svg || !m) return [0, 0];
    const p = new DOMPoint(e.clientX, e.clientY).matrixTransform(m.inverse());
    const z = Math.max(-1, Math.min(r.zeilen, Math.floor((p.y - Y0) / S)));
    const s = Math.max(-1, Math.min(r.spalten, Math.floor((p.x - X0) / S)));
    return [z, s];
  }

  function schreibe(neu: Stellen[]): void {
    zugriff.code = zusammen(mitTermen(zeilen, ausgang, neu), ansicht.eingaenge);
  }

  function runter(e: PointerEvent): void {
    const [z, s] = lage(e);
    if (z < 0 || s < 0 || z >= r.zeilen || s >= r.spalten) return;
    waehle(r.belegung(z, s));
    if (art !== 'ziehen') return;
    zug = { z0: z, s0: s, z1: z, s1: s };
    svg?.setPointerCapture(e.pointerId);
  }
  function bewege(e: PointerEvent): void {
    if (!zug) return;
    const [z, s] = lage(e);
    zug = { ...zug, z1: z, s1: s };
  }
  function los(): void {
    if (!zug) return;
    const feld = auswahl;
    zug = null;
    if (!feld) return;
    const neu = blockAus(feld, ansicht.eingaenge.length);
    if (!terme.some((t) => termText(t, ansicht.eingaenge) === termText(neu, ansicht.eingaenge))) schreibe([...terme, neu]);
  }
  function loesche(i: number): void {
    schreibe(terme.filter((_, k) => k !== i));
  }

  function zeichen(w: string): string {
    return w === 'x' ? 'x' : w;
  }
</script>

<div class="kv-rahmen">
  {#if ansicht.ausgaenge.length > 1}
    <div class="ausgaenge" role="group" aria-label="Ausgang wählen">
      {#each ansicht.ausgaenge as a (a)}
        {@const zahl = (zeilen.find((z) => z.art === 'formel' && z.name === a) as { terme: Stellen[] } | undefined)?.terme.length ?? 0}
        <button class="chip" class:gewaehlt={a === ausgang} onclick={() => (ausgang = a)}>{a}<small>{zahl}</small></button>
      {/each}
    </div>
  {/if}
  <div class="leiste">
    <button class="werkzeug" class:aktiv={art === 'ziehen'} onclick={() => (art = 'ziehen')}><i class="fa-solid fa-vector-square" aria-hidden="true"></i>Block ziehen</button>
    <button class="werkzeug" class:aktiv={art === 'loeschen'} onclick={() => (art = 'loeschen')}><i class="fa-solid fa-eraser" aria-hidden="true"></i>Block löschen</button>
    <button class="werkzeug" class:aktiv={art === 'text'} onclick={() => (art = 'text')}><i class="fa-solid fa-font" aria-hidden="true"></i>Formel als Text</button>
  </div>

  {#if art === 'text'}
    <div class="text-host"><EditorBereich sprache="plaintext" bind:code={zugriff.code} /></div>
    <p class="hinweis dim">Je Ausgang eine Zeile, etwa <code>{ausgang} = !B !D + C !D</code>: ein Buchstabe heißt 1, <code>!</code> davor 0.</p>
  {:else}
    <p class="hinweis dim">
      {art === 'ziehen' ? 'Von einem Feld zum anderen ziehen; über den Rand geht es auf der anderen Seite weiter. Erlaubt sind 1, 2 oder 4 Felder je Richtung.' : 'Klick auf einen Block löscht ihn.'}
    </p>
    <!-- svelte-ignore a11y_no_static_element_interactions -->
    <svg bind:this={svg} class="kv" class:loeschen={art === 'loeschen'} viewBox="0 0 {breite} {hoehe}" role="img" aria-label="KV-Diagramm für {ausgang}"
      onpointerdown={runter} onpointermove={bewege} onpointerup={los} onpointercancel={() => (zug = null)}>
      <text class="achse ecke" x={X0 - 10} y={Y0 - 14} text-anchor="end">{r.zeilenEin.join('')}\{r.spaltenEin.join('')}</text>
      {#each Array.from({ length: r.spalten }, (_, s) => s) as s (s)}
        <text class="achse" x={X0 + s * S + S / 2} y={Y0 - 14} text-anchor="middle">{r.spaltenText(s)}</text>
      {/each}
      {#each Array.from({ length: r.zeilen }, (_, z) => z) as z (z)}
        <text class="achse" x={X0 - 12} y={Y0 + z * S + S / 2 + 5} text-anchor="end">{r.zeilenText(z)}</text>
        {#each Array.from({ length: r.spalten }, (_, s) => s) as s (s)}
          {@const b = r.belegung(z, s)}
          <rect class="feld" class:bedeckt={abgedeckt.has(b)} class:gewaehlt={b === gewaehlt} class:in-zug={ueberstrichen.has(b)} class:falsch-zug={!!zug && !auswahl}
            x={X0 + s * S} y={Y0 + z * S} width={S} height={S} />
          <text class="wert" class:eins={werte[b] === '1'} class:egal={werte[b] === 'x'} x={X0 + s * S + S / 2} y={Y0 + z * S + S / 2 + 8} text-anchor="middle">{zeichen(werte[b])}</text>
          <text class="nr" x={X0 + s * S + 6} y={Y0 + z * S + 14}>{ansicht.namen[b] ?? b}</text>
        {/each}
      {/each}
      {#each terme as t, i (termText(t, ansicht.eingaenge))}
        {#each rechtecke(t, r) as [s, z, bs, bz], k (k)}
          {@const einzug = 5 + (i % 4) * 4}
          <rect class="block" style:--farbe={FARBEN[i % FARBEN.length]} x={X0 + s * S + einzug} y={Y0 + z * S + einzug}
            width={bs * S - 2 * einzug} height={bz * S - 2 * einzug} rx="14"
            onpointerdown={(e) => { if (art === 'loeschen') { e.stopPropagation(); loesche(i); } }} role="button" tabindex="-1" />
        {/each}
      {/each}
    </svg>
  {/if}

  <div class="formel">
    {ausgang} =
    {#each terme as t, i (termText(t, ansicht.eingaenge))}
      {#if i > 0}<span class="plus">+</span>{/if}
      <span class="term" style:--farbe={FARBEN[i % FARBEN.length]}>
        {#each t as s, k (k)}{#if s != null}<span class="lit" class:ol={s === 0}>{ansicht.eingaenge[k]}</span>{/if}{/each}{#if t.every((s) => s == null)}1{/if}
      </span>
    {:else}<span class="dim">noch kein Block</span>{/each}
  </div>
  <div class="block-liste">
    {#each terme as t, i (termText(t, ansicht.eingaenge))}
      <div class="block-zeile">
        <span class="farbe" style:background={FARBEN[i % FARBEN.length]}></span>
        <code>{termText(t, ansicht.eingaenge)}</code>
        <span class="dim">{felder(t).length} {felder(t).length === 1 ? 'Feld' : 'Felder'}</span>
        <button class="knopf-klein" onclick={() => loesche(i)} title="Block löschen"><i class="fa-solid fa-xmark" aria-hidden="true"></i></button>
      </div>
    {/each}
  </div>
</div>

<style>
  .kv-rahmen {
    height: 100%;
    overflow-y: auto;
    padding: var(--sp-2) var(--sp-3) var(--sp-3);
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
  }
  .kv-rahmen > * { flex-shrink: 0; }
  .ausgaenge, .leiste {
    display: flex;
    flex-wrap: wrap;
    gap: 4px;
  }
  .ausgaenge small { margin-left: 6px; color: var(--fg-mute); }
  .werkzeug {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    height: 32px;
    padding: 0 var(--sp-2);
    border: 1px solid var(--border);
    background: var(--bg-card-2);
    color: var(--fg);
    font: 600 13px var(--mono);
    cursor: pointer;
  }
  .werkzeug.aktiv { color: var(--accent); border-color: var(--accent); }
  .hinweis { margin: 0; font-size: var(--fs-sm); }
  .text-host { height: 260px; border: 1px solid var(--border); }
  .kv {
    display: block;
    width: 100%;
    max-width: 560px;
    height: auto;
    margin: 0 auto;
    touch-action: none;
    user-select: none;
  }
  .kv.loeschen .block { cursor: pointer; }
  .achse { fill: var(--fg-dim); font: 600 15px var(--mono); }
  .feld { fill: var(--bg-card-2); stroke: var(--border-strong); stroke-width: 1.2; cursor: crosshair; }
  .feld.bedeckt { fill: color-mix(in srgb, var(--accent) 8%, var(--bg-card-2)); }
  .feld.in-zug { fill: color-mix(in srgb, var(--gold) 26%, var(--bg-card-2)); }
  .feld.in-zug.falsch-zug { fill: color-mix(in srgb, var(--red) 26%, var(--bg-card-2)); }
  .feld.gewaehlt { stroke: var(--fg); stroke-width: 2.4; }
  .wert { fill: var(--fg-mute); font: 700 24px var(--mono); pointer-events: none; }
  .wert.eins { fill: var(--gold); }
  .wert.egal { fill: #60a5fa; }
  .nr { fill: var(--fg-mute); font: 500 11px var(--mono); pointer-events: none; }
  .block {
    fill: color-mix(in srgb, var(--farbe) 10%, transparent);
    stroke: var(--farbe);
    stroke-width: 3;
    pointer-events: none;
  }
  .kv.loeschen .block { pointer-events: all; }
  .formel {
    font: 600 20px var(--mono);
    padding: var(--sp-2) var(--sp-3);
    border: 1px solid var(--border);
    background: var(--bg);
    overflow-wrap: anywhere;
  }
  .term { border-bottom: 3px solid var(--farbe); padding: 0 2px; }
  .plus { margin: 0 6px; color: var(--fg-dim); }
  /* jeder Buchstabe ein eigener Strich: zwei Striche dürfen nicht verschmelzen (das hieße NICHT über beide) */
  .lit { display: inline-block; margin: 0 2px; }
  .lit.ol { text-decoration: overline; }
  .block-liste { display: flex; flex-direction: column; gap: 4px; }
  .block-zeile {
    display: grid;
    grid-template-columns: 14px minmax(0, 1fr) auto auto;
    gap: var(--sp-2);
    align-items: center;
    padding: 4px var(--sp-2);
    border: 1px solid var(--border);
    background: var(--bg-card-2);
    font-size: var(--fs-sm);
  }
  .farbe { width: 12px; height: 12px; border-radius: 3px; }
</style>
