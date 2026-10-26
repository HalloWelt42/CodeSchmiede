<script lang="ts">
  /*
   * Signalplan eines Ablaufs: je Gruppe eine Zeile mit dem Signal jeder Sekunde, darunter ein schmaler Strich, solange
   * dort jemand auf Grün wartet. Unfälle als rote Marken oben, Nacht schattiert, der Zeiger steht beim gezeigten
   * Bild. Ein Klick springt zur Sekunde.
   */
  import type { Gruppe, Wiedergabe } from '../../types/Ampel';

  interface Props {
    gruppen: Gruppe[];
    wiedergabe: Wiedergabe | null;
    dauer: number;
    zeit: number;
    onSpringe: (sekunde: number) => void;
  }
  let { gruppen, wiedergabe, dauer, zeit, onSpringe }: Props = $props();

  const BREITE = 480;
  const LINKS = 70;
  const ZEILE = 14;
  const ABSTAND = 8;
  const OBEN = 8;

  /** Folgen gleicher Werte als [Wert, Beginn, Dauer] */
  function phasen<T>(werte: T[]): [T, number, number][] {
    const folge: [T, number, number][] = [];
    werte.forEach((w, s) => {
      const letzte = folge[folge.length - 1];
      if (letzte && letzte[0] === w) letzte[2] += 1;
      else folge.push([w, s, 1]);
    });
    return folge;
  }

  let hoehe = $derived(OBEN + gruppen.length * (ZEILE + ABSTAND) + 16);
  let unten = $derived(OBEN + gruppen.length * (ZEILE + ABSTAND));
  let schritt = $derived(dauer > 120 ? 30 : dauer > 60 ? 20 : 10);
  let marken = $derived(Array.from({ length: Math.floor(dauer / schritt) + 1 }, (_, i) => i * schritt));

  function x(s: number): number {
    return LINKS + ((BREITE - LINKS - 6) * s) / dauer;
  }

  let svg: SVGSVGElement | undefined = $state();

  function klick(e: MouseEvent): void {
    if (!svg) return;
    const r = svg.getBoundingClientRect();
    const s = ((((e.clientX - r.left) / r.width) * BREITE - LINKS) * dauer) / (BREITE - LINKS - 6);
    onSpringe(Math.max(0, Math.min(dauer, s)));
  }
</script>

<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_noninteractive_element_interactions -->
<svg bind:this={svg} class="ablaufplan" viewBox="0 0 {BREITE} {hoehe}" role="img" aria-label="Signalplan" onclick={klick}>
  {#each wiedergabe?.nacht ?? [] as [von, bis], i (i)}
    <rect class="nachtzeit" x={x(von)} y={OBEN - 4} width={x(Math.min(bis, dauer)) - x(von)} height={unten - OBEN + 4} />
  {/each}
  {#each marken as s (s)}
    <line class="raster" x1={x(s)} y1={OBEN - 4} x2={x(s)} y2={unten} />
    <text x={x(s)} y={hoehe - 2} text-anchor={s === 0 ? 'start' : s + schritt > dauer ? 'end' : 'middle'}>{s}</text>
  {/each}
  {#each gruppen as g, k (g.name)}
    {@const y = OBEN + k * (ZEILE + ABSTAND)}
    <text x="0" y={y + ZEILE - 3}>{g.name}</text>
    {#if wiedergabe}
      {#each phasen(wiedergabe.signale.map((sig) => sig[g.name])) as [z, von, lang] (von)}
        <rect class={z} x={x(von)} {y} width={x(von + lang) - x(von)} height={ZEILE} />
      {/each}
      {#each phasen(wiedergabe.bedarf.map((b) => b.includes(g.name))).filter(([b]) => b) as [, von, lang] (von)}
        <rect class="bedarf" x={x(von)} y={y + ZEILE + 1.5} width={x(von + lang) - x(von)} height="3" />
      {/each}
    {/if}
  {/each}
  {#each wiedergabe?.unfaelle ?? [] as u, i (i)}
    <path class="unfall-marke" d="M {x(u.t)} {OBEN + 3} l 4 -7 l -8 0 z" />
  {/each}
  {#if wiedergabe}
    <line class="zeiger" x1={x(zeit)} y1={OBEN - 6} x2={x(zeit)} y2={unten} />
  {/if}
</svg>
