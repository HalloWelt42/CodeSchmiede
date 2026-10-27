<script lang="ts">
  /*
   * Zeitverlauf einer Schaltung mit Takt: oben der Takt, darunter je Eingang seine Folge und je Ausgang Soll
   * (gestrichelt, gold) und Ist; Takte, in denen ein Ausgang abweicht, sind rot hinterlegt. Ein Klick wählt den Takt.
   */
  interface Props {
    eingaenge: string[];
    ausgaenge: string[];
    takte: number;
    eingaben: Record<string, string>;
    soll: Record<string, string>;
    /** je Takt die Werte, ohne Lauf null */
    ist: Record<string, number>[] | null;
    /** gezeigter Takt */
    jetzt: number;
    waehle: (takt: number) => void;
  }
  let { eingaenge, ausgaenge, takte, eingaben, soll, ist, jetzt, waehle }: Props = $props();

  const B = 480;
  const X0 = 50;
  const H = 34;
  const OBEN = 8;

  let schritt = $derived((B - X0 - 6) / Math.max(1, takte));
  let spuren = $derived([{ name: 'T', art: 'takt' as const }, ...eingaenge.map((name) => ({ name, art: 'eingang' as const })), ...ausgaenge.map((name) => ({ name, art: 'ausgang' as const }))]);
  let hoehe = $derived(OBEN + spuren.length * H + 20);

  function x(i: number): number {
    return X0 + i * schritt;
  }
  function mitte(k: number): number {
    return OBEN + k * H + H / 2;
  }
  /** Rechteckwelle einer Folge von 0 und 1 (x bleibt auf der Höhe davor) */
  function welle(folge: (number | null)[], k: number): string {
    const y = (w: number) => mitte(k) + (w ? -9 : 9);
    let letzter = folge.find((w) => w != null) ?? 0;
    let d = `M ${x(0)} ${y(letzter)}`;
    folge.forEach((w, i) => {
      if (w != null) letzter = w;
      d += ` V ${y(letzter)} H ${x(i + 1)}`;
    });
    return d;
  }
  function taktWelle(k: number): string {
    let d = `M ${x(0)} ${mitte(k) + 9}`;
    for (let i = 0; i < takte; i++) d += ` H ${x(i) + 0.01} V ${mitte(k) - 9} H ${x(i) + schritt / 3} V ${mitte(k) + 9} H ${x(i + 1)}`;
    return d;
  }
  function sollFolge(name: string): (number | null)[] {
    return [...(soll[name] ?? '')].map((c) => (c === 'x' ? null : Number(c)));
  }
  function falsch(name: string, i: number): boolean {
    const s = soll[name]?.[i];
    return !!ist && s != null && s !== 'x' && String(ist[i]?.[name]) !== s;
  }
</script>

<svg class="verlauf" viewBox="0 0 {B} {hoehe}" role="img" aria-label="Zeitverlauf je Takt">
  <rect class="zeiger" x={x(Math.max(0, jetzt))} y={OBEN - 4} width={schritt} height={spuren.length * H + 4} />
  {#each spuren as s, k (s.name)}
    <text class="spur-name" class:ausgang={s.art === 'ausgang'} x="4" y={mitte(k) + 5}>{s.name}</text>
    <line class="trenn" x1={X0} y1={OBEN + (k + 1) * H} x2={x(takte)} y2={OBEN + (k + 1) * H} />
    {#if s.art === 'takt'}
      <path class="takt" d={taktWelle(k)} />
    {:else if s.art === 'eingang'}
      <path class="eingang" d={welle([...(eingaben[s.name] ?? '0'.repeat(takte))].map(Number), k)} />
    {:else}
      {#each Array.from({ length: takte }, (_, i) => i) as i (i)}
        {#if falsch(s.name, i)}<rect class="fehler" x={x(i)} y={mitte(k) - 15} width={schritt} height="30" />{/if}
      {/each}
      <path class="soll" d={welle(sollFolge(s.name), k)} />
      {#if ist}<path class="ist" d={welle(ist.map((w) => w[s.name] ?? 0), k)} />{/if}
    {/if}
  {/each}
  {#each Array.from({ length: takte }, (_, i) => i) as i (i)}
    {#if takte <= 16 || i % 2 === 0}<text class="zahl" x={x(i) + schritt / 2} y={hoehe - 4} text-anchor="middle">{i}</text>{/if}
    <rect class="klick" x={x(i)} y="0" width={schritt} height={hoehe} onclick={() => waehle(i)} role="button" tabindex="-1" onkeydown={() => {}} aria-label="Takt {i}" />
  {/each}
</svg>
<div class="legende">
  <span class="l-ist">ist</span><span class="l-soll">soll</span><span class="l-fehler">weicht ab</span>
</div>

<style>
  .verlauf {
    display: block;
    flex-shrink: 0;
    width: 100%;
    height: auto;
  }
  .spur-name { fill: var(--fg-dim); font: 600 13px var(--mono); }
  .spur-name.ausgang { fill: var(--fg); }
  .zahl { fill: var(--fg-mute); font: 600 12px var(--mono); }
  .trenn { stroke: var(--border); }
  .takt { fill: none; stroke: var(--fg-dim); stroke-width: 1.4; }
  .eingang { fill: none; stroke: var(--fg-dim); stroke-width: 2; }
  .soll { fill: none; stroke: var(--gold); stroke-width: 1.6; stroke-dasharray: 4 3; }
  .ist { fill: none; stroke: var(--accent); stroke-width: 2.4; }
  .fehler { fill: color-mix(in srgb, var(--red) 24%, transparent); }
  .zeiger { fill: color-mix(in srgb, var(--accent) 12%, transparent); stroke: var(--accent); stroke-width: 1; }
  .klick { fill: transparent; cursor: pointer; }
  .legende {
    display: flex;
    flex-shrink: 0;
    flex-wrap: wrap;
    gap: var(--sp-3);
    font-size: var(--fs-xs);
    color: var(--fg-dim);
  }
  .legende span::before {
    content: '';
    display: inline-block;
    width: 16px;
    height: 0;
    margin-right: 6px;
    vertical-align: 3px;
    border-top: 2px solid var(--accent);
  }
  .legende .l-soll::before { border-top: 2px dashed var(--gold); }
  .legende .l-fehler::before {
    height: 10px;
    border: 0;
    background: color-mix(in srgb, var(--red) 35%, transparent);
    vertical-align: -1px;
  }
</style>
