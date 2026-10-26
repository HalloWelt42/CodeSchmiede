<script lang="ts">
  /*
   * Fahrdiagramm eines Ablaufs: je Kabine eine Linie (Etage über Zeit), Punkte, wo jemand rief, rote Marken bei
   * Verstößen, eine rote Linie beim Feueralarm. Der Zeiger steht beim gezeigten Bild, ein Klick springt zur Sekunde.
   */
  import type { Haus, AufzugWiedergabe } from '../../types/Aufzug';

  interface Props {
    haus: Haus;
    wiedergabe: AufzugWiedergabe | null;
    dauer: number;
    zeit: number;
    onSpringe: (sekunde: number) => void;
  }
  let { haus, wiedergabe, dauer, zeit, onSpringe }: Props = $props();

  const BREITE = 480;
  const LINKS = 30;
  const OBEN = 8;

  let schritt = $derived(Math.max(10, Math.min(16, 140 / haus.etagen)));
  let unten = $derived(OBEN + (haus.etagen - 1) * schritt);
  let hoehe = $derived(unten + 18);
  let marken = $derived.by(() => {
    const abstand = dauer > 180 ? 40 : dauer > 90 ? 30 : 20;
    return Array.from({ length: Math.floor(dauer / abstand) + 1 }, (_, i) => i * abstand);
  });

  function x(t: number): number {
    return LINKS + ((BREITE - LINKS - 6) * t) / dauer;
  }
  function y(e: number): number {
    return unten - e * schritt;
  }

  let linien = $derived.by(() => {
    if (!wiedergabe) return [];
    return haus.aufzuege.map((_, i) =>
      wiedergabe.bilder
        .filter((_, n) => n % 4 === 0)
        .map(([t, kabinen]) => `${x(t).toFixed(1)},${y(kabinen[i][0]).toFixed(1)}`)
        .join(' '),
    );
  });

  let svg: SVGSVGElement | undefined = $state();

  function klick(e: MouseEvent): void {
    if (!svg) return;
    const r = svg.getBoundingClientRect();
    const s = ((((e.clientX - r.left) / r.width) * BREITE - LINKS) * dauer) / (BREITE - LINKS - 6);
    onSpringe(Math.max(0, Math.min(dauer, s)));
  }
</script>

<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_noninteractive_element_interactions -->
<svg bind:this={svg} class="ablaufplan" viewBox="0 0 {BREITE} {hoehe}" role="img" aria-label="Fahrdiagramm" onclick={klick}>
  {#each Array.from({ length: haus.etagen }, (_, e) => e) as e (e)}
    <line class="raster" x1={LINKS} y1={y(e)} x2={BREITE - 6} y2={y(e)} />
    <text x="0" y={y(e) + 4}>{haus.namen[e]}</text>
  {/each}
  {#each marken as s (s)}
    <text x={x(s)} y={hoehe - 2} text-anchor={s === 0 ? 'start' : s + 1 > dauer ? 'end' : 'middle'}>{s}</text>
  {/each}
  {#if wiedergabe}
    {#if wiedergabe.feuer != null}
      <line class="feuer-linie" x1={x(wiedergabe.feuer)} y1={OBEN - 6} x2={x(wiedergabe.feuer)} y2={unten} />
    {/if}
    {#each wiedergabe.fahrgaeste as f (f.id)}
      <circle class="marke" cx={x(f.ankunft)} cy={y(f.von)} r="2.4" />
    {/each}
    {#each linien as punkte, i (i)}
      <polyline class="fahrt" class:zweite={i > 0} points={punkte} />
    {/each}
    {#each wiedergabe.ereignisse.filter((e) => e.art === 'verstoss') as e, i (i)}
      <path class="unfall-marke" d="M {x(e.t)} {OBEN - 1} l 4 -6 l -8 0 z" />
    {/each}
    <line class="zeiger" x1={x(zeit)} y1={OBEN - 6} x2={x(zeit)} y2={unten} />
  {/if}
</svg>
