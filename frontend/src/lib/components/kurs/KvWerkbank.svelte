<script lang="ts">
  /*
   * Werkbank der Digitaltechnik: eine Funktion als Würfel der Belegungen (bei drei Eingängen; mit Regler klappt er zum
   * KV-Raster auf) oder als Raster, dazu die Wahrheitstabelle und die Formeln. Ein Klick auf eine Ecke oder ein Feld
   * zeigt ihre Nachbarn, ein Klick auf einen Term seinen Block, in allen Sichten zugleich. Nur zum Anschauen; gerechnet
   * hat der Server beim Einlesen (jede Formel stimmt mit der Funktion).
   */
  import type { KvTeil } from '../../api/KursApi';
  import { felder, raster, rechtecke, zerlege, type Stellen } from '../../steuerung/kv';

  let { teil }: { teil: KvTeil } = $props();

  const S = 90;
  const X0 = 70;
  const Y0 = 64;

  let n = $derived(teil.eingaenge.length);
  let r = $derived(raster(teil.eingaenge));
  let mitWuerfel = $derived(n === 3);
  // svelte-ignore state_referenced_locally
  let t = $state(teil.start === 'wuerfel' ? 0 : 1);
  let formelNr = $state(0);
  let hell = $state<number | null>(null);
  let gewaehlt = $state<number | null>(null);

  let formel = $derived(teil.formeln[formelNr]);
  let terme = $derived(((zerlege(`f = ${formel.formel}`, teil.eingaenge, ['f'])[0] as { terme?: Stellen[] }).terme ?? []));
  let imBlock = $derived(hell != null && terme[hell] ? new Set(felder(terme[hell])) : null);
  let nachbarn = $derived(gewaehlt != null ? new Set(Array.from({ length: n }, (_, i) => gewaehlt! ^ (1 << i))) : null);
  let breite = $derived(Math.max(460, X0 + r.spalten * S + 30));
  let hoehe = $derived(mitWuerfel ? 300 : Y0 + r.zeilen * S + 24);
  let paare = $derived.by(() => {
    const p: [number, number][] = [];
    for (let a = 0; a < 2 ** n; a++) for (let i = 0; i < n; i++) if ((a ^ (1 << i)) > a) p.push([a, a ^ (1 << i)]);
    return p;
  });

  const bit = (b: number, i: number) => (b >> (n - 1 - i)) & 1;
  const bits = (b: number) => b.toString(2).padStart(n, '0');
  // Würfel: C nach rechts, B nach hinten, A nach unten
  const wuerfel = (b: number): [number, number] => [120 + bit(b, 2) * 150 + bit(b, 1) * 80, 70 + bit(b, 0) * 150 - bit(b, 1) * 50];
  function imRaster(b: number): [number, number] {
    const [z, s] = r.feld(b);
    return [X0 + s * S + S / 2, Y0 + z * S + S / 2];
  }
  function lage(b: number): [number, number] {
    if (!mitWuerfel) return imRaster(b);
    const [wx, wy] = wuerfel(b);
    const [rx, ry] = imRaster(b);
    return [wx + (rx - wx) * t, wy + (ry - wy) * t];
  }
  /** Kante zwischen erster und letzter Spalte: wölbt sich beim Aufklappen über das Raster, dort war geklebt */
  function kante(a: number, b: number): { d: string; klebt: boolean } {
    const [x1, y1] = lage(a);
    const [x2, y2] = lage(b);
    const sa = r.feld(a)[1];
    const sb = r.feld(b)[1];
    const klebt = Math.abs(sa - sb) === r.spalten - 1 && r.spalten > 2;
    return { d: klebt ? `M ${x1} ${y1} Q ${(x1 + x2) / 2} ${(y1 + y2) / 2 - 150 * t} ${x2} ${y2}` : `M ${x1} ${y1} L ${x2} ${y2}`, klebt };
  }
  function waehleFeld(b: number): void {
    gewaehlt = gewaehlt === b ? null : b;
    hell = null;
  }
  function waehleTerm(i: number): void {
    hell = hell === i ? null : i;
    gewaehlt = null;
  }
</script>

<div class="kv-werkbank">
  <svg class="kv-svg" viewBox="0 0 {breite} {hoehe}" role="img" aria-label={mitWuerfel ? 'Würfel der Belegungen, der sich zum KV-Raster aufklappt' : 'KV-Raster'}>
    {#each Array.from({ length: r.zeilen }, (_, z) => z) as z (z)}
      {#each Array.from({ length: r.spalten }, (_, s) => s) as s (s)}
        <rect class="zelle" x={X0 + s * S} y={Y0 + z * S} width={S} height={S} opacity={t} />
      {/each}
      <text class="achse" x={X0 - 14} y={Y0 + z * S + S / 2 + 5} text-anchor="end" opacity={t}>{r.zeilenText(z)}</text>
    {/each}
    {#each Array.from({ length: r.spalten }, (_, s) => s) as s (s)}
      <text class="achse" x={X0 + s * S + S / 2} y={Y0 - 14} text-anchor="middle" opacity={t}>{r.spaltenText(s)}</text>
    {/each}
    <text class="achse" x={X0 - 14} y={Y0 - 14} text-anchor="end" opacity={t}>{r.zeilenEin.join('')}\{r.spaltenEin.join('')}</text>

    {#if imBlock && t > 0.5}
      {#each rechtecke(terme[hell!], r) as [s, z, bs, bz], k (k)}
        <rect class="block" x={X0 + s * S + 7} y={Y0 + z * S + 7} width={bs * S - 14} height={bz * S - 14} rx="14" opacity={(t - 0.5) * 2} />
      {/each}
    {/if}

    {#if mitWuerfel}
      {#each paare as [a, b] (`${a}-${b}`)}
        {@const k = kante(a, b)}
        <path class="kante" class:im-block={!!imBlock?.has(a) && !!imBlock?.has(b)} class:nachbar={gewaehlt === a || gewaehlt === b}
          d={k.d} stroke-dasharray={k.klebt && t > 0.3 ? '6 5' : null} />
      {/each}
    {/if}

    {#each Array.from({ length: 2 ** n }, (_, b) => b) as b (b)}
      {@const [x, y] = lage(b)}
      <g class="ecke-g" onclick={() => waehleFeld(b)} role="button" tabindex="-1" onkeydown={() => {}}>
        <circle class="ecke" class:eins={teil.werte[b] === '1'} class:egal={teil.werte[b] === 'x'} class:gewaehlt={b === gewaehlt}
          class:nachbar={!!nachbarn?.has(b)} class:blass={!!imBlock && !imBlock.has(b)} cx={x} cy={y} r={mitWuerfel ? 17 : 20} />
        {#if teil.werte[b] === 'x'}<text class="x-zeichen" {x} y={y + 6} text-anchor="middle">x</text>{/if}
        <text class="bits" {x} y={y + (mitWuerfel ? 34 : 36)} text-anchor="middle">{bits(b)}</text>
      </g>
    {/each}
  </svg>

  {#if teil.regler && mitWuerfel}
    <label class="regler-zeile">
      <i class="fa-solid fa-cube" aria-hidden="true"></i>
      <input type="range" min="0" max="100" value={Math.round(t * 100)} oninput={(e) => (t = +e.currentTarget.value / 100)} aria-label="Würfel aufklappen" />
      <i class="fa-solid fa-table-cells" aria-hidden="true"></i>
      <span class="num stand">{t < 0.05 ? 'Würfel' : t > 0.95 ? 'Raster' : '...'}</span>
    </label>
  {/if}

  {#if teil.formeln.length > 1}
    <div class="formel-knoepfe" role="group" aria-label="Formel wählen">
      {#each teil.formeln as f, i (f.titel)}
        <button class="knopf-klein" class:aktiv={i === formelNr} onclick={() => { formelNr = i; hell = null; }}>{f.titel}</button>
      {/each}
    </div>
  {/if}
  <div class="formel">
    f =
    {#each terme as term, i (i)}
      {#if i > 0}<span class="plus">+</span>{/if}
      <button class="term" class:hell={i === hell} onclick={() => waehleTerm(i)}>
        {#each term as s, k (k)}{#if s != null}<span class="lit" class:ol={s === 0}>{teil.eingaenge[k]}</span>{/if}{/each}{#if term.every((s) => s == null)}1{/if}
      </button>
    {/each}
  </div>
  <div class="zahlen">
    <span><b class="num">{terme.length}</b> {terme.length === 1 ? 'Term' : 'Terme'}</span>
    <span><b class="num">{formel.bausteine}</b> Bausteine</span>
    <span class="dim">Klick auf einen Term zeigt seinen Block, auf {mitWuerfel ? 'eine Ecke' : 'ein Feld'} ihre Nachbarn</span>
  </div>
  {#if teil.plan}<pre class="plan">{formel.plan}</pre>{/if}

  <table class="kv-tabelle">
    <thead><tr>{#each teil.eingaenge as e (e)}<th>{e}</th>{/each}<th>f</th></tr></thead>
    <tbody>
      {#each Array.from({ length: 2 ** n }, (_, b) => b) as b (b)}
        <tr class:hell={!!imBlock?.has(b) || b === gewaehlt} class:nachbar={!!nachbarn?.has(b)} onclick={() => waehleFeld(b)}>
          {#each teil.eingaenge as _, i (i)}<td>{bit(b, i)}</td>{/each}<td>{teil.werte[b]}</td>
        </tr>
      {/each}
    </tbody>
  </table>
</div>

<style>
  .kv-werkbank {
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
  }
  .kv-werkbank > * { flex-shrink: 0; }
  .kv-svg {
    display: block;
    width: 100%;
    height: auto;
    background: var(--bg);
    border: 1px solid var(--border);
  }
  .zelle { fill: var(--bg-card-2); stroke: var(--border-strong); stroke-width: 1.4; }
  .achse { fill: var(--fg-dim); font: 600 14px var(--mono); }
  .block { fill: color-mix(in srgb, var(--s-a) 20%, transparent); stroke: var(--s-a); stroke-width: 2.4; }
  .kante { stroke: var(--border-strong); stroke-width: 2; fill: none; }
  .kante.im-block { stroke: var(--s-a); stroke-width: 4; }
  .kante.nachbar { stroke: var(--s-b); stroke-width: 3.5; }
  .ecke-g { cursor: pointer; }
  .ecke { stroke: var(--fg-mute); stroke-width: 2; fill: var(--bg-card); }
  .ecke.eins { fill: var(--s-a); stroke: var(--s-a); }
  .ecke.egal { stroke: var(--s-b); stroke-dasharray: 3 3; }
  .ecke.gewaehlt { stroke: var(--fg); stroke-width: 3.5; }
  .ecke.nachbar { stroke: var(--s-b); stroke-width: 3.5; }
  .ecke.blass { opacity: 0.3; }
  .x-zeichen { fill: var(--s-b); font: 700 16px var(--mono); pointer-events: none; }
  .bits { fill: var(--fg); font: 700 13px var(--mono); pointer-events: none; }
  .regler-zeile {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    font-size: var(--fs-sm);
  }
  .regler-zeile input { flex: 1; accent-color: var(--s-a); }
  .stand { min-width: 5ch; }
  .formel-knoepfe { display: flex; flex-wrap: wrap; gap: 4px; }
  .knopf-klein.aktiv { color: var(--s-a); border-color: var(--s-a); }
  .formel {
    font: 600 18px var(--mono);
    padding: var(--sp-2) var(--sp-3);
    border: 1px solid var(--border);
    background: var(--bg-card-2);
    overflow-wrap: anywhere;
  }
  .plus { margin: 0 4px; color: var(--fg-dim); }
  .term {
    font: inherit;
    color: inherit;
    background: transparent;
    border: 0;
    border-radius: 3px;
    padding: 1px 3px;
    cursor: pointer;
  }
  .term.hell { background: color-mix(in srgb, var(--s-a) 28%, transparent); }
  /* jeder Buchstabe ein eigener Strich: zwei Striche dürfen nicht verschmelzen (das hieße NICHT über beide) */
  .lit { display: inline-block; margin: 0 2px; }
  .lit.ol { text-decoration: overline; }
  .zahlen {
    display: flex;
    flex-wrap: wrap;
    gap: var(--sp-3);
    font-size: var(--fs-sm);
    color: var(--fg-dim);
  }
  .zahlen b { color: var(--fg); }
  .plan {
    margin: 0;
    padding: var(--sp-2);
    background: var(--bg);
    border: 1px solid var(--border);
    font-family: var(--mono);
    font-size: 12px;
    max-height: 180px;
    overflow: auto;
  }
  .kv-tabelle {
    width: 100%;
    border-collapse: collapse;
    font: 13px var(--mono);
    text-align: center;
  }
  .kv-tabelle th { color: var(--fg-dim); font-weight: 600; padding: 3px; border-bottom: 1px solid var(--border); }
  .kv-tabelle td { padding: 3px; border-bottom: 1px solid var(--border); cursor: pointer; }
  .kv-tabelle tr.hell td { background: color-mix(in srgb, var(--s-a) 16%, transparent); }
  .kv-tabelle tr.nachbar td { background: color-mix(in srgb, var(--s-b) 16%, transparent); }
</style>
