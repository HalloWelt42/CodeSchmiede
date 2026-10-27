<script lang="ts">
  /*
   * Schaltplan-Editor: links die Eingänge als Schalter und die festen Werte 0 und 1, in der Mitte die Bausteine,
   * rechts die Ausgänge als Lämpchen. Leitungen entstehen mit zwei Klicks: erst ein Ausgang (rechter Punkt an einem
   * Schalter oder Baustein), dann ein Eingang (linker Punkt an einem Baustein oder am Lämpchen); ein Klick auf einen
   * belegten Eingang nimmt die Leitung weg. Bausteine lassen sich ziehen; beim freien Bauen kommen sie aus der Leiste
   * dazu und lassen sich löschen. Alles schreibt den Text des Plans; Leitungen mit 1 leuchten in der gewählten Zeile.
   * Mit Takt kommen Flipflops dazu: unter den festen Werten steht der Takt T, gestrichelt zu jedem Flipflop; die
   * Eingänge stellt dann der Ablauf, sie lassen sich nicht umschalten.
   */
  import { EINGAENGE_JE_ART, OFFEN, SPEICHER, neuerName, zerlege, zusammen, type Baustein, type Zeile } from '../../steuerung/schaltplan';
  import type { SchaltungAnsicht } from '../../types/Schaltung';
  import type { CodeZugriff } from '../../types/Steuerung';
  import EditorBereich from '../EditorBereich.svelte';

  interface Props {
    ansicht: Pick<SchaltungAnsicht, 'eingaenge' | 'ausgaenge' | 'bausteine' | 'vorgabe'>;
    zugriff: CodeZugriff;
    /** Werte aller Signale in der gewählten Zeile, ohne gültigen Plan null */
    werte: Record<string, number> | null;
    zeile: number;
    waehle: (zeile: number) => void;
    /** Schaltung mit Takt: Takt T und Flipflops, Eingänge kommen aus dem Ablauf */
    takt?: boolean;
  }
  let { ansicht, zugriff, werte, zeile, waehle, takt = false }: Props = $props();

  const B = 600;
  const GW = 70;
  const GH = 46;
  const EIN_X = 18;
  const LAMPE_X = 566;
  const FEST = ['0', '1'];
  const BESCHREIBUNG: Record<string, string> = {
    UND: 'UND', ODER: 'ODER', XOR: 'XOR', NAND: 'NAND', NOR: 'NOR', NICHT: 'NICHT', FF: 'Flipflop',
  };

  let ansichtArt = $state<'plan' | 'text'>('plan');
  let auswahl = $state<string | null>(null);
  let markiert = $state<string | null>(null);
  let ziehen = $state<{ name: string; dx: number; dy: number; x: number; y: number; bewegt: boolean } | null>(null);
  let svg: SVGSVGElement | undefined = $state();

  let zeilen = $derived(zerlege(zugriff.code, ansicht.ausgaenge));
  let frei = $derived(ansicht.vorgabe.length === 0);
  let bausteine = $derived(
    zeilen.flatMap((z, i) => (z.art === 'baustein' ? [{ ...z, index: i }] : [])).map((b, k) => ({
      ...b,
      x: ziehen?.name === b.name ? ziehen.x : (b.x ?? 180 + (k % 3) * 120),
      y: ziehen?.name === b.name ? ziehen.y : (b.y ?? 30 + Math.floor(k / 3) * 80),
    })),
  );
  let quellen = $derived(new Map(zeilen.flatMap((z) => (z.art === 'ausgang' ? [[z.name, z.quelle] as const] : []))));

  let einAbstand = 70;
  let ausAbstand = $derived(ansicht.ausgaenge.length > 4 ? 48 : 70);
  let hoehe = $derived(
    Math.max(
      300,
      40 + ansicht.eingaenge.length * einAbstand + (takt ? 140 : 90),
      40 + ansicht.ausgaenge.length * ausAbstand,
      ...bausteine.map((b) => b.y + GH + 30),
    ),
  );

  function eingangY(i: number): number {
    return 40 + i * einAbstand;
  }
  function festY(i: number): number {
    return 40 + ansicht.eingaenge.length * einAbstand + 10 + i * 34;
  }
  /** Mitte des Takts T, unter den festen Werten */
  let taktY = $derived(festY(FEST.length) + 16);
  function taktLeitung(b: { x: number; y: number }): string {
    const [px, py] = taktPin(b);
    return `M ${EIN_X + 44} ${taktY} H ${b.x - 12} V ${py} H ${px}`;
  }
  function taktPin(b: { x: number; y: number }): [number, number] {
    return [b.x, b.y + GH - 9];
  }
  function ausgangY(j: number): number {
    return 40 + j * ausAbstand;
  }
  function pinEin(b: { x: number; y: number; typ: string }, i: number): [number, number] {
    const n = EINGAENGE_JE_ART[b.typ] ?? 2;
    return [b.x, b.y + (n === 1 ? GH / 2 : 13 + i * 20)];
  }
  function quellPunkt(name: string): [number, number] | null {
    const e = ansicht.eingaenge.indexOf(name);
    if (e >= 0) return [EIN_X + 52, eingangY(e)];
    const f = FEST.indexOf(name);
    if (f >= 0) return [EIN_X + 36, festY(f)];
    const b = bausteine.find((x) => x.name === name);
    return b ? [b.x + GW, b.y + GH / 2] : null;
  }
  /** Leitung im rechten Winkel; versatz schiebt den senkrechten Teil, damit Leitungen nicht aufeinander liegen */
  function leitung([sx, sy]: [number, number], [tx, ty]: [number, number], versatz = 0): string {
    const mx = sx < tx ? Math.min(tx - 8, Math.max(sx + 8, (sx + tx) / 2 + versatz)) : sx + 14;
    return sx < tx ? `M ${sx} ${sy} H ${mx} V ${ty} H ${tx}` : `M ${sx} ${sy} H ${mx} V ${(sy + ty) / 2} H ${tx - 14} V ${ty} H ${tx}`;
  }
  function an(name: string | undefined): boolean {
    return !!name && werte?.[name] === 1;
  }

  // --- Ändern -------------------------------------------------------------
  function schreibe(neu: Zeile[]): void {
    zugriff.code = zusammen(neu);
  }

  /** Zeilen ohne Leerzeilen am Ende, damit Angehängtes direkt anschließt */
  function ohneLeerEnde(liste: Zeile[]): Zeile[] {
    let ende = liste.length;
    while (ende > 0 && liste[ende - 1].art === 'text' && !(liste[ende - 1] as { text: string }).text.trim()) ende -= 1;
    return liste.slice(0, ende);
  }

  function verbinde(ziel: string, i: number | null): void {
    const vorher = i == null ? quellen.get(ziel) : bausteine.find((b) => b.name === ziel)?.eingaenge[i];
    const quelle = auswahl ?? (vorher && vorher !== OFFEN ? OFFEN : null);
    if (quelle == null) return;
    auswahl = null;
    if (i == null) {
      const da = zeilen.some((z) => z.art === 'ausgang' && z.name === ziel);
      schreibe(da ? zeilen.map((z) => (z.art === 'ausgang' && z.name === ziel ? { ...z, quelle } : z)) : [...ohneLeerEnde(zeilen), { art: 'ausgang', name: ziel, quelle }]);
      return;
    }
    schreibe(zeilen.map((z) => (z.art === 'baustein' && z.name === ziel ? { ...z, eingaenge: z.eingaenge.map((e, k) => (k === i ? quelle : e)) } : z)));
  }

  function waehleQuelle(name: string): void {
    auswahl = auswahl === name ? null : name;
  }

  function dazu(typ: string): void {
    const name = neuerName(zeilen, typ, [...ansicht.eingaenge, ...ansicht.ausgaenge]);
    const k = bausteine.length;
    const neu: Baustein = {
      art: 'baustein', name, typ, eingaenge: Array(EINGAENGE_JE_ART[typ] ?? 2).fill(OFFEN),
      x: 180 + (k % 3) * 120, y: 30 + Math.floor(k / 3) * 80,
    };
    schreibe([...ohneLeerEnde(zeilen), neu]);
    markiert = name;
  }

  function loesche(name: string): void {
    schreibe(
      zeilen
        .filter((z) => !(z.art === 'baustein' && z.name === name))
        .map((z) => {
          if (z.art === 'baustein') return { ...z, eingaenge: z.eingaenge.map((e) => (e === name ? OFFEN : e)) };
          if (z.art === 'ausgang' && z.quelle === name) return { ...z, quelle: OFFEN };
          return z;
        }),
    );
    markiert = null;
  }

  function punkt(e: PointerEvent): [number, number] {
    const m = svg?.getScreenCTM();
    if (!svg || !m) return [0, 0];
    const p = new DOMPoint(e.clientX, e.clientY).matrixTransform(m.inverse());
    return [p.x, p.y];
  }

  function greife(e: PointerEvent, b: { name: string; x: number; y: number }): void {
    const [px, py] = punkt(e);
    ziehen = { name: b.name, dx: px - b.x, dy: py - b.y, x: b.x, y: b.y, bewegt: false };
    (e.currentTarget as Element).setPointerCapture(e.pointerId);
  }
  function bewege(e: PointerEvent): void {
    if (!ziehen) return;
    const [px, py] = punkt(e);
    const x = Math.max(90, Math.min(B - GW - 60, px - ziehen.dx));
    const y = Math.max(4, py - ziehen.dy);
    ziehen = { ...ziehen, x, y, bewegt: ziehen.bewegt || Math.hypot(x - ziehen.x, y - ziehen.y) > 3 };
  }
  function lasse(): void {
    if (!ziehen) return;
    const { name, x, y, bewegt } = ziehen;
    ziehen = null;
    if (!bewegt) {
      markiert = markiert === name ? null : name;
      return;
    }
    schreibe(zeilen.map((z) => (z.art === 'baustein' && z.name === name ? { ...z, x: Math.round(x / 10) * 10, y: Math.round(y / 10) * 10 } : z)));
  }

  function schalte(i: number): void {
    if (zeile < 0) return;
    waehle(zeile ^ (1 << (ansicht.eingaenge.length - 1 - i)));
  }
</script>

<div class="plan-rahmen">
  <div class="leiste">
    <div class="modus kurz" role="group" aria-label="Ansicht des Plans">
      <button class:aktiv={ansichtArt === 'plan'} onclick={() => (ansichtArt = 'plan')}>Plan</button>
      <button class:aktiv={ansichtArt === 'text'} onclick={() => (ansichtArt = 'text')}>Text</button>
    </div>
    {#if frei}
      {#each ansicht.bausteine as typ (typ)}
        <button class="baustein-knopf" onclick={() => dazu(typ)} title="{BESCHREIBUNG[typ] ?? typ} dazu"><i class="fa-solid fa-plus" aria-hidden="true"></i>{typ}</button>
      {/each}
      {#if markiert}
        <button class="baustein-knopf weg" onclick={() => markiert && loesche(markiert)}><i class="fa-solid fa-trash" aria-hidden="true"></i>{markiert} löschen</button>
      {/if}
    {:else}
      <span class="dim klein">Verdrahten: die Bausteine stehen fest</span>
    {/if}
  </div>
  {#if ansichtArt === 'text'}
    <div class="text-host"><EditorBereich sprache="plaintext" bind:code={zugriff.code} /></div>
  {:else}
    <p class="hinweis dim">
      {#if auswahl}Von <b>{auswahl}</b>: jetzt einen Eingang anklicken (links an einem Baustein oder am Lämpchen).
      {:else if takt}Klick auf einen Ausgangspunkt, dann auf einen Eingang. Die Eingänge stellt der Ablauf, T gibt den Takt.
      {:else}Klick auf einen Ausgangspunkt, dann auf einen Eingang. Schalter A, B ... wählen die Zeile.{/if}
    </p>
    <!-- svelte-ignore a11y_no_static_element_interactions -->
    <svg bind:this={svg} class="plan" viewBox="0 0 {B} {hoehe}" role="img" aria-label="Schaltplan" onpointermove={bewege} onpointerup={lasse}>
      {#if takt}
        {#each bausteine.filter((b) => b.typ === SPEICHER) as b (b.name)}<path class="draht takt-draht" d={taktLeitung(b)} />{/each}
      {/if}
      {#each bausteine as b (b.name)}
        {#each b.eingaenge as e, i (i)}
          {@const von = e !== OFFEN ? quellPunkt(e) : null}
          {#if von}<path class="draht" class:an={an(e)} d={leitung(von, pinEin(b, i), (i - 0.5) * 10)} />{/if}
        {/each}
      {/each}
      {#each ansicht.ausgaenge as name, j (name)}
        {@const q = quellen.get(name)}
        {@const von = q && q !== OFFEN ? quellPunkt(q) : null}
        {#if von}<path class="draht" class:an={an(q)} d={leitung(von, [LAMPE_X - 22, ausgangY(j)], (j - ansicht.ausgaenge.length / 2) * 7)} />{/if}
      {/each}

      {#each ansicht.eingaenge as name, i (name)}
        {@const wert = werte?.[name] ?? (zeile >= 0 ? (zeile >> (ansicht.eingaenge.length - 1 - i)) & 1 : 0)}
        <g class="schalter" class:an={wert === 1} class:fest-gestellt={takt} onclick={() => schalte(i)} role="button" tabindex="-1" onkeydown={() => {}}>
          <rect x={EIN_X} y={eingangY(i) - 16} width="44" height="32" rx="6" />
          <text x={EIN_X + 22} y={eingangY(i) + 5} text-anchor="middle">{name} {wert}</text>
        </g>
        <circle class="pin quelle" class:gewaehlt={auswahl === name} cx={EIN_X + 52} cy={eingangY(i)} r="6" onclick={() => waehleQuelle(name)} role="button" tabindex="-1" onkeydown={() => {}} />
      {/each}
      {#each FEST as name, i (name)}
        <rect class="fest" x={EIN_X + 8} y={festY(i) - 11} width="22" height="22" rx="3" />
        <text class="fest-text" x={EIN_X + 19} y={festY(i) + 5} text-anchor="middle">{name}</text>
        <circle class="pin quelle" class:gewaehlt={auswahl === name} cx={EIN_X + 36} cy={festY(i)} r="5" onclick={() => waehleQuelle(name)} role="button" tabindex="-1" onkeydown={() => {}} />
      {/each}

      {#if takt}
        <rect class="takt-quelle" x={EIN_X} y={taktY - 14} width="44" height="28" rx="6" />
        <text class="takt-text" x={EIN_X + 22} y={taktY + 5} text-anchor="middle">T</text>
      {/if}

      {#each bausteine as b (b.name)}
        <g class="baustein" class:ff={b.typ === SPEICHER} class:markiert={markiert === b.name} class:an={an(b.name)} onpointerdown={(e) => greife(e, b)} role="button" tabindex="-1">
          <rect x={b.x} y={b.y} width={GW} height={GH} rx={b.typ === SPEICHER ? 3 : 8} />
          {#if b.typ === SPEICHER}<path class="takt-pin" d="M {b.x} {b.y + GH - 15} l 8 6 l -8 6" />{/if}
          <text class="typ" x={b.x + GW / 2} y={b.y + 21} text-anchor="middle">{b.typ}</text>
          <text class="name-b" x={b.x + GW / 2} y={b.y + 36} text-anchor="middle">{b.name}</text>
        </g>
        {#each b.eingaenge as e, i (i)}
          {@const [px, py] = pinEin(b, i)}
          <circle class="pin ziel" class:offen={e === OFFEN} cx={px} cy={py} r="5" onclick={() => verbinde(b.name, i)} role="button" tabindex="-1" onkeydown={() => {}} />
        {/each}
        <circle class="pin quelle" class:gewaehlt={auswahl === b.name} cx={b.x + GW} cy={b.y + GH / 2} r="6" onclick={() => waehleQuelle(b.name)} role="button" tabindex="-1" onkeydown={() => {}} />
      {/each}

      {#each ansicht.ausgaenge as name, j (name)}
        {@const q = quellen.get(name)}
        <circle class="pin ziel" class:offen={!q || q === OFFEN} cx={LAMPE_X - 22} cy={ausgangY(j)} r="5" onclick={() => verbinde(name, null)} role="button" tabindex="-1" onkeydown={() => {}} />
        <circle class="lampe" class:an={an(name)} cx={LAMPE_X} cy={ausgangY(j)} r="13" />
        <text class="name-a" x={LAMPE_X} y={ausgangY(j) + 30} text-anchor="middle">{name}</text>
      {/each}
    </svg>
  {/if}
</div>

<style>
  .plan-rahmen {
    height: 100%;
    overflow-y: auto;
    padding: var(--sp-2) var(--sp-3) var(--sp-3);
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
  }
  .leiste {
    display: flex;
    flex-wrap: wrap;
    gap: 4px;
    align-items: center;
  }
  .modus.kurz { margin: 0; width: 140px; }
  .baustein-knopf {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    height: 30px;
    padding: 0 var(--sp-2);
    border: 1px solid var(--border);
    background: var(--bg-card-2);
    color: var(--fg);
    font: 600 12px var(--mono);
    cursor: pointer;
  }
  .baustein-knopf.weg { color: var(--red); border-color: var(--red); }
  .klein { font-size: var(--fs-sm); }
  .hinweis {
    margin: 0;
    font-size: var(--fs-sm);
  }
  .text-host {
    height: 320px;
    border: 1px solid var(--border);
  }
  .plan {
    display: block;
    width: 100%;
    height: auto;
    background: var(--bg);
    border: 1px solid var(--border);
    touch-action: none;
  }
  .draht { fill: none; stroke: var(--fg-mute); stroke-width: 2.4; stroke-linejoin: round; }
  .draht.an { stroke: var(--accent); filter: drop-shadow(0 0 3px color-mix(in srgb, var(--accent) 60%, transparent)); }
  .schalter { cursor: pointer; }
  .schalter.fest-gestellt { cursor: default; }
  .schalter rect { fill: var(--bg-card-2); stroke: var(--border-strong); stroke-width: 1.4; }
  .schalter.an rect { fill: color-mix(in srgb, var(--accent) 30%, var(--bg-card-2)); stroke: var(--accent); }
  .schalter text { fill: var(--fg); font: 700 13px var(--mono); pointer-events: none; }
  .fest { fill: var(--bg-card-2); stroke: var(--border); }
  .fest-text { fill: var(--fg-dim); font: 700 12px var(--mono); pointer-events: none; }
  .baustein { cursor: grab; }
  .baustein rect { fill: var(--bg-card-2); stroke: var(--border-strong); stroke-width: 1.6; }
  .baustein.an rect { stroke: var(--accent); }
  .baustein.markiert rect { stroke: var(--gold); stroke-width: 2.4; }
  .baustein.ff rect { stroke: var(--accent); stroke-width: 1.8; }
  .baustein.ff.an rect { fill: color-mix(in srgb, var(--accent) 24%, var(--bg-card-2)); }
  .baustein.ff.markiert rect { stroke: var(--gold); }
  .takt-pin { fill: none; stroke: var(--fg-dim); stroke-width: 1.4; pointer-events: none; }
  .takt-draht { stroke-dasharray: 5 4; stroke-width: 1.6; }
  .takt-quelle { fill: var(--bg-card-2); stroke: var(--border-strong); stroke-width: 1.4; }
  .takt-text { fill: var(--fg); font: 700 13px var(--mono); }
  .typ { fill: var(--fg); font: 700 12px var(--mono); pointer-events: none; }
  .name-b { fill: var(--fg-mute); font: 500 10px var(--mono); pointer-events: none; }
  .pin { stroke-width: 1.6; cursor: pointer; }
  .pin.quelle { fill: var(--bg); stroke: var(--fg-dim); }
  .pin.quelle.gewaehlt { fill: var(--gold); stroke: var(--gold); }
  .pin.ziel { fill: var(--fg-mute); stroke: var(--fg-mute); }
  .pin.ziel.offen { fill: var(--bg); stroke: var(--orange); }
  .lampe { fill: #2b3038; stroke: var(--border-strong); stroke-width: 1.4; }
  .lampe.an { fill: #fbbf24; filter: drop-shadow(0 0 6px #fbbf24); }
  .name-a { fill: var(--fg-dim); font: 600 12px var(--mono); }
</style>
