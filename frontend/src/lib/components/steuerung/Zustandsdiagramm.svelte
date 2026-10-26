<script lang="ts">
  /*
   * Zustandsdiagramm aus der Übergangstabelle: Zustände im Kreis, Endzustände doppelt umrandet, ein Pfeil in den
   * Start. Regeln zwischen denselben Zuständen teilen sich einen Pfeil (Beschriftung liest/schreibt, geht); Regeln, die
   * im Zustand bleiben, sind Schleifen. Zustand und Regel des gezeigten Schritts leuchten.
   */
  import { regeln, type Zeile } from '../../steuerung/turingTabelle';

  interface Props {
    zeilen: Zeile[];
    start: string;
    ende: string[];
    aktiveZeile: number | null;
    aktiverZustand: string | null;
  }
  let { zeilen, start, ende, aktiveZeile, aktiverZustand }: Props = $props();

  const B = 460;
  const H = 320;
  const R = 26;

  let liste = $derived(regeln(zeilen));
  let zustaende = $derived.by(() => {
    const namen = [start];
    for (const { regel } of liste) {
      for (const n of [regel.zustand, regel.danach]) if (!namen.includes(n)) namen.push(n);
    }
    for (const e of ende) if (!namen.includes(e)) namen.push(e);
    return namen;
  });
  let lage = $derived.by(() => {
    const n = zustaende.length;
    const punkte = new Map<string, [number, number]>();
    zustaende.forEach((name, i) => {
      const w = Math.PI + (2 * Math.PI * i) / n;
      punkte.set(name, n === 1 ? [B / 2, H / 2] : [B / 2 + Math.cos(w) * (B / 2 - 70), H / 2 + Math.sin(w) * (H / 2 - 62)]);
    });
    return punkte;
  });

  interface Kante {
    von: string;
    nach: string;
    text: string;
    zeilen: number[];
  }
  let kanten = $derived.by(() => {
    const k = new Map<string, Kante>();
    for (const { regel, zeile } of liste) {
      const schluessel = `${regel.zustand}>${regel.danach}`;
      const eintrag = k.get(schluessel) ?? { von: regel.zustand, nach: regel.danach, text: '', zeilen: [] };
      const teil = `${regel.liest}/${regel.schreibt},${regel.geht}`;
      eintrag.zeilen.push(zeile);
      eintrag.text = eintrag.zeilen.length > 3 ? `${eintrag.text.split('  ').slice(0, 3).join('  ')}  ...` : eintrag.text ? `${eintrag.text}  ${teil}` : teil;
      k.set(schluessel, eintrag);
    }
    return [...k.values()];
  });

  function weg(k: Kante): { d: string; tx: number; ty: number } {
    const [x1, y1] = lage.get(k.von) ?? [0, 0];
    const [x2, y2] = lage.get(k.nach) ?? [0, 0];
    if (k.von === k.nach) {
      // Schleife oberhalb, nach außen gerichtet
      const ax = x1 - B / 2, ay = y1 - H / 2;
      const l = Math.hypot(ax, ay) || 1;
      const nx = ax / l, ny = ay / l || -1;
      const px = x1 + nx * R, py = y1 + ny * R;
      const d = `M ${px - ny * 10} ${py + nx * 10} C ${px + nx * 46 - ny * 26} ${py + ny * 46 + nx * 26}, ${px + nx * 46 + ny * 26} ${py + ny * 46 - nx * 26}, ${px + ny * 10} ${py - nx * 10}`;
      return { d, tx: x1 + nx * (R + 52), ty: y1 + ny * (R + 52) + 4 };
    }
    const dx = x2 - x1, dy = y2 - y1;
    const l = Math.hypot(dx, dy) || 1;
    const ux = dx / l, uy = dy / l;
    // gebogen, damit Hin und Zurück nebeneinander liegen
    const mx = (x1 + x2) / 2 - uy * 24, my = (y1 + y2) / 2 + ux * 24;
    const sx = x1 + ux * R, sy = y1 + uy * R, ex = x2 - ux * (R + 2), ey = y2 - uy * (R + 2);
    return { d: `M ${sx} ${sy} Q ${mx} ${my} ${ex} ${ey}`, tx: mx, ty: my - 4 };
  }
</script>

<svg class="diagramm" viewBox="0 0 {B} {H}" role="img" aria-label="Zustandsdiagramm">
  <defs>
    <marker id="pfeil-turing" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" class="spitze" />
    </marker>
  </defs>
  {#if lage.get(start)}
    {@const [sx, sy] = lage.get(start) ?? [0, 0]}
    <path class="kante" d="M {sx - R - 30} {sy} L {sx - R - 2} {sy}" marker-end="url(#pfeil-turing)" />
  {/if}
  {#each kanten as k (k.von + '>' + k.nach)}
    {@const w = weg(k)}
    <path class="kante" class:aktiv={aktiveZeile != null && k.zeilen.includes(aktiveZeile)} d={w.d} marker-end="url(#pfeil-turing)" />
    <text class="beschrift" x={w.tx} y={w.ty} text-anchor="middle">{k.text}</text>
  {/each}
  {#each zustaende as name (name)}
    {@const [x, y] = lage.get(name) ?? [0, 0]}
    <circle class="knoten" class:aktiv={name === aktiverZustand} cx={x} cy={y} r={R} />
    {#if ende.includes(name)}<circle class="ende" cx={x} cy={y} r={R - 5} />{/if}
    <text class="name" {x} y={y + 4} text-anchor="middle">{name.length > 9 ? `${name.slice(0, 8)}.` : name}</text>
  {/each}
</svg>

<style>
  .diagramm {
    display: block;
    width: 100%;
    height: auto;
    border: 1px solid var(--border);
    background: var(--bg);
  }
  .knoten { fill: var(--bg-card-2); stroke: var(--border-strong); stroke-width: 1.5; }
  .knoten.aktiv { stroke: var(--accent); stroke-width: 3; }
  .ende { fill: none; stroke: var(--border-strong); }
  .name { fill: var(--fg); font: 600 11px var(--mono); }
  .kante { fill: none; stroke: var(--fg-mute); stroke-width: 1.4; }
  .kante.aktiv { stroke: var(--accent); stroke-width: 2.4; }
  .spitze { fill: var(--fg-mute); }
  .beschrift { fill: var(--fg-dim); font: 500 10px var(--mono); paint-order: stroke; stroke: var(--bg); stroke-width: 4px; stroke-linejoin: round; }
</style>
