<script lang="ts">
  /*
   * Aufzugsteuerung im Schnitt: Haus mit Etagen, je Kabine ein Schacht mit Seilen, Kabinen mit Türblättern, die zur
   * Seite gleiten, Anzeigen über den Türen, Rufknöpfe und Wartende links, Leute, die durch die Tür gehen. Bei
   * Feueralarm ein rotes Band. Alles aus einem Bild der Wiedergabe; ohne Lauf steht alles im Erdgeschoss.
   */
  import type { AufzugAnsicht, AufzugWiedergabe, KabinenBild } from '../../types/Aufzug';

  interface Props {
    ansicht: AufzugAnsicht;
    wiedergabe: AufzugWiedergabe | null;
    bild: number;
  }
  let { ansicht, wiedergabe, bild }: Props = $props();

  const ETAGE_H = 46;
  const SCHACHT_B = 58;
  const SCHACHT_ABSTAND = 18;
  const SCHACHT_X = 150;
  const KB = 46;
  const KH = 34;

  let haus = $derived(ansicht.haus);
  let anzahl = $derived(haus.aufzuege.length);
  let breite = $derived(SCHACHT_X + anzahl * (SCHACHT_B + SCHACHT_ABSTAND) + 60);
  let hoehe = $derived(haus.etagen * ETAGE_H + 26);
  let oben = $derived(hoehe - 10 - haus.etagen * ETAGE_H);

  function boden(e: number): number {
    return hoehe - 10 - e * ETAGE_H;
  }
  function schacht(i: number): number {
    return SCHACHT_X + i * (SCHACHT_B + SCHACHT_ABSTAND);
  }
  function kabineX(i: number): number {
    return schacht(i) + (SCHACHT_B - KB) / 2;
  }

  let aufnahme = $derived(wiedergabe && bild >= 0 ? wiedergabe.bilder[bild] : null);
  let vorher = $derived(wiedergabe && bild > 0 ? wiedergabe.bilder[bild - 4] ?? wiedergabe.bilder[0] : null);
  let zeit = $derived(aufnahme?.[0] ?? 0);
  let kabinen = $derived<KabinenBild[]>(aufnahme?.[1] ?? haus.aufzuege.map(() => [0, 0, 0]));
  let wartende = $derived(aufnahme?.[2] ?? []);
  let laeufer = $derived(aufnahme?.[3] ?? []);
  let feuer = $derived(wiedergabe?.feuer != null && zeit >= wiedergabe.feuer);

  function richtung(i: number): number {
    const jetzt = kabinen[i]?.[0] ?? 0;
    const davor = vorher?.[1][i]?.[0] ?? jetzt;
    return Math.sign(jetzt - davor);
  }

  let jeEtage = $derived.by(() => {
    const liste: { etage: number; k: number; richtung: number }[] = [];
    const zaehler = new Map<number, number>();
    for (const [, etage, r] of wartende) {
      const k = zaehler.get(etage) ?? 0;
      zaehler.set(etage, k + 1);
      liste.push({ etage, k, richtung: r });
    }
    return liste;
  });

  function gerufen(e: number, r: number): boolean {
    return wartende.some(([, etage, ri]) => etage === e && ri === r);
  }
</script>

{#snippet mensch(cx: number, cy: number, klasse: string)}
  <g class={klasse}>
    <circle {cx} cy={cy - 9} r="3.2" />
    <rect x={cx - 3.4} y={cy - 6} width="6.8" height="9" rx="2.5" />
  </g>
{/snippet}

<svg class="szene haus" viewBox="0 0 {breite} {hoehe}" role="img" aria-label="Haus im Schnitt mit Aufzug">
  <rect class="gehweg" x="16" y={oben} width={breite - 32} height={haus.etagen * ETAGE_H} />
  {#each haus.aufzuege as name, i (name)}
    <rect class="schacht" x={schacht(i)} y={oben} width={SCHACHT_B} height={haus.etagen * ETAGE_H} />
  {/each}
  {#each Array.from({ length: haus.etagen }, (_, e) => e) as e (e)}
    <line class="etage" x1="16" y1={boden(e)} x2={breite - 16} y2={boden(e)} />
    <text class="beschriftung" x={breite - 40} y={boden(e) - 16}>{haus.namen[e]}</text>
    {#if e < haus.etagen - 1}<path class="ruf" class:an={gerufen(e, 1)} d="M {SCHACHT_X - 14} {boden(e) - 26} l 4 -6 l 4 6 z" />{/if}
    {#if e > 0}<path class="ruf" class:an={gerufen(e, -1)} d="M {SCHACHT_X - 14} {boden(e) - 20} l 4 6 l 4 -6 z" />{/if}
    {#each haus.aufzuege as name, i (name)}
      {@const kx = kabineX(i)}
      <rect class="rahmen-tuer" x={kx - 3} y={boden(e) - KH - 3} width={KB + 6} height={KH + 3} />
      <rect class="anzeige-feld" x={kx + KB / 2 - 12} y={boden(e) - KH - 13} width="24" height="8" rx="1.5" />
      <text class="anzeige" x={kx + KB / 2} y={boden(e) - KH - 6.6} text-anchor="middle">
        {richtung(i) > 0 ? '▲' : richtung(i) < 0 ? '▼' : ''}{haus.namen[Math.round(kabinen[i]?.[0] ?? 0)]}
      </text>
    {/each}
  {/each}

  {#each jeEtage as w, n (n)}
    {@render mensch(SCHACHT_X - 30 - w.k * 11, boden(w.etage) - 3, 'wartend')}
  {/each}

  {#each kabinen as [pos, tuer, drin], i (i)}
    {@const kx = kabineX(i)}
    {@const ky = boden(pos) - KH}
    <g class="seil">
      {#each [12, 23, 34] as dx (dx)}<line x1={kx + dx} y1={oben} x2={kx + dx} y2={ky} />{/each}
    </g>
    <clipPath id="kabine-{i}"><rect x={kx} y={ky} width={KB} height={KH} /></clipPath>
    <rect class="kabine-innen" x={kx} y={ky} width={KB} height={KH} />
    <line class="handlauf" x1={kx + 4} y1={ky + KH * 0.55} x2={kx + KB - 4} y2={ky + KH * 0.55} />
    {#each Array.from({ length: Math.min(drin, 4) }, (_, k) => k) as k (k)}
      {@render mensch(kx + 8 + k * 10, ky + KH - 3, 'drin')}
    {/each}
    <g clip-path="url(#kabine-{i})">
      <rect class="tuerblatt" x={kx - (KB / 2) * tuer} y={ky} width={KB / 2} height={KH} />
      <rect class="tuerblatt" x={kx + KB / 2 + (KB / 2) * tuer} y={ky} width={KB / 2} height={KH} />
      <line class="tuerkante" x1={kx + KB / 2 - (KB / 2) * tuer} y1={ky} x2={kx + KB / 2 - (KB / 2) * tuer} y2={ky + KH} />
    </g>
    <rect class="kabine" x={kx} y={ky} width={KB} height={KH} />
  {/each}

  {#each laeufer as [id, i, weg, anteil] (id)}
    {@const kx = kabineX(i)}
    {@const y = boden(Math.round(kabinen[i]?.[0] ?? 0)) - 3}
    {#if weg > 0}
      {@render mensch(SCHACHT_X - 30 + anteil * (kx + KB / 2 - SCHACHT_X + 30), y, 'wartend')}
    {:else}
      {@render mensch(kx + KB / 2 + anteil * (breite - 70 - kx), y, 'drin')}
    {/if}
  {/each}

  {#if feuer}
    <rect class="feuer-band" x="16" y="2" width={breite - 32} height="16" rx="2" />
    <text class="feuer-text" x={breite / 2} y="13.5" text-anchor="middle">Feueralarm: alle ins Erdgeschoss</text>
  {/if}
</svg>

<style>
  .haus {
    max-height: calc(100vh - 380px);
    min-height: 260px;
    width: auto;
    max-width: 100%;
    align-self: center;
  }
</style>
