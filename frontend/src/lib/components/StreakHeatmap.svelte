<script lang="ts">
  /*
   * Aktivitätsfeld: ein Kästchen je Tag, Spalten sind Wochen (Montag
   * oben). Am Rechner das ganze Jahr mit Blättern, am Telefon nur die
   * letzten Wochen. Rechtsbündig, damit bei wenig Platz die jüngsten
   * Wochen sichtbar bleiben.
   */
  import { onMount } from 'svelte';
  import { progressApi } from '../api/ProgressApi';
  import type { HeatmapTag } from '../api/ProgressApi';

  /** nur die letzten n Wochen bis heute statt des ganzen Jahres */
  let { wochen }: { wochen?: number } = $props();

  const HEUTE = new Date();
  const HEUTE_JAHR = HEUTE.getFullYear();

  let tage = $state<HeatmapTag[]>([]);
  let jahr = $state(HEUTE_JAHR);

  onMount(() => lade(jahr));

  async function lade(j: number): Promise<void> {
    try {
      tage = (await progressApi.heatmapJahr(j)).tage;
    } catch {
      tage = [];
    }
  }

  function blaettern(schritt: number): void {
    jahr += schritt;
    void lade(jahr);
  }

  // 'en-CA' liefert JJJJ-MM-TT in lokaler Zeit, ohne Verschiebung nach UTC
  const iso = (d: Date): string => d.toLocaleDateString('en-CA');

  interface Zelle {
    datum: string;
    submissions: number;
    bestanden: number;
  }

  let zeitraum = $derived.by(() => {
    if (wochen) {
      const start = new Date(HEUTE);
      start.setDate(start.getDate() - (wochen * 7 - 1));
      return { start, ende: new Date(HEUTE) };
    }
    const ende = jahr === HEUTE_JAHR ? new Date(HEUTE) : new Date(jahr, 11, 31);
    return { start: new Date(jahr, 0, 1), ende };
  });

  // null füllt die erste Woche bis zum Starttag auf
  let zellen = $derived.by(() => {
    const nachDatum = new Map(tage.map((t) => [t.datum, t]));
    const liste: (Zelle | null)[] = [];
    const d = new Date(zeitraum.start);
    for (let i = 0; i < (d.getDay() + 6) % 7; i++) liste.push(null);
    while (d <= zeitraum.ende) {
      const t = nachDatum.get(iso(d));
      liste.push({ datum: iso(d), submissions: t?.submissions ?? 0, bestanden: t?.bestanden ?? 0 });
      d.setDate(d.getDate() + 1);
    }
    return liste;
  });

  let echte = $derived(zellen.filter((z): z is Zelle => z !== null));
  let aktiveTage = $derived(echte.filter((z) => z.submissions > 0).length);
  let summe = $derived(echte.reduce((s, z) => s + z.submissions, 0));
  let bestanden = $derived(echte.reduce((s, z) => s + z.bestanden, 0));

  function stufe(n: number): number {
    if (n === 0) return 0;
    if (n === 1) return 1;
    if (n <= 3) return 2;
    if (n <= 6) return 3;
    return 4;
  }
</script>

<div class="block">
  <div class="block-kopf">
    <span>{wochen ? `Letzte ${wochen} Wochen` : `Aktivität ${jahr}`}</span>
    <span class="rechts">
      {aktiveTage} aktive {aktiveTage === 1 ? 'Tag' : 'Tage'}{wochen ? '' : `, ${bestanden} / ${summe} bestanden`}
      {#if !wochen}
        <button class="knopf-klein" onclick={() => blaettern(-1)} aria-label="Vorheriges Jahr">
          <i class="fa-solid fa-chevron-left" aria-hidden="true"></i>
        </button>
        <button class="knopf-klein" onclick={() => blaettern(1)} disabled={jahr >= HEUTE_JAHR} aria-label="Nächstes Jahr">
          <i class="fa-solid fa-chevron-right" aria-hidden="true"></i>
        </button>
      {/if}
    </span>
  </div>
  <div class="heat">
    {#each zellen as z, i (i)}
      {#if z}
        <span class="s{stufe(z.submissions)}" title="{z.datum}: {z.submissions} Submissions, {z.bestanden} bestanden"></span>
      {:else}
        <span class="leer"></span>
      {/if}
    {/each}
  </div>
</div>

<style>
  .rechts {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    text-transform: none;
    letter-spacing: 0;
  }
  .rechts .knopf-klein {
    height: 20px;
    padding: 0 6px;
  }
  .heat {
    display: grid;
    grid-auto-flow: column;
    grid-template-rows: repeat(7, 10px);
    grid-auto-columns: 10px;
    gap: 2px;
    justify-content: end;
    overflow: hidden;
  }
  .heat span {
    width: 10px;
    height: 10px;
    background: var(--bg);
    border: 1px solid var(--border);
  }
  .heat span.leer {
    background: transparent;
    border-color: transparent;
  }
  .heat span.s1 { background: color-mix(in srgb, var(--accent) 35%, var(--bg)); border-color: transparent; }
  .heat span.s2 { background: color-mix(in srgb, var(--accent) 60%, var(--bg)); border-color: transparent; }
  .heat span.s3 { background: color-mix(in srgb, var(--accent) 80%, var(--bg)); border-color: transparent; }
  .heat span.s4 { background: var(--accent); border-color: transparent; }
</style>
