<script lang="ts">
  /*
   * Streak-Heatmap im GitHub-Contribution-Style.
   * Zeigt die letzten ~90 Tage als Raster: 7 Zeilen (Wochentage),
   * Spalten = Wochen. Farbintensitaet = Anzahl Submissions.
   */
  import { onMount } from 'svelte';
  import { progressApi } from '../api/ProgressApi';
  import type { HeatmapTag } from '../api/ProgressApi';

  let tage = $state<HeatmapTag[]>([]);
  let geladen = $state(false);

  const ANZAHL_TAGE = 91; // 13 Wochen

  onMount(async () => {
    try {
      const r = await progressApi.heatmap(ANZAHL_TAGE);
      tage = r.tage;
    } catch {
      tage = [];
    } finally {
      geladen = true;
    }
  });

  function formatiere_datum(d: Date): string {
    // 'en-CA' liefert YYYY-MM-DD im lokalen Timezone -- ohne UTC-Shift
    return d.toLocaleDateString('en-CA');
  }

  let karte = $derived.by(() => {
    const map = new Map<string, HeatmapTag>();
    for (const t of tage) map.set(t.datum, t);
    const heute = new Date();
    heute.setHours(0, 0, 0, 0);
    const ergebnisse: { datum: string; submissions: number; bestanden: number; wochentag: number }[] = [];
    for (let i = ANZAHL_TAGE - 1; i >= 0; i--) {
      const d = new Date(heute);
      d.setDate(heute.getDate() - i);
      const iso = formatiere_datum(d);
      const t = map.get(iso);
      ergebnisse.push({
        datum: iso,
        submissions: t?.submissions ?? 0,
        bestanden: t?.bestanden ?? 0,
        wochentag: d.getDay(), // 0=So, 1=Mo, ..., 6=Sa
      });
    }
    return ergebnisse;
  });

  let spalten = $derived.by(() => {
    // Gruppiere in Wochen-Spalten (Mo-So). Erstes Padding nach Wochentag.
    const sp: ({ datum: string; submissions: number; bestanden: number } | null)[][] = [];
    let aktuelle_spalte: ({ datum: string; submissions: number; bestanden: number } | null)[] = [];
    let erster_wt = karte[0]?.wochentag ?? 1;
    // Wir wollen Mo=0, ..., So=6 -> shift
    function montag_idx(wt: number): number {
      return (wt + 6) % 7;
    }
    for (let i = 0; i < montag_idx(erster_wt); i++) aktuelle_spalte.push(null);
    for (const t of karte) {
      aktuelle_spalte.push({ datum: t.datum, submissions: t.submissions, bestanden: t.bestanden });
      if (montag_idx(t.wochentag) === 6) {
        sp.push(aktuelle_spalte);
        aktuelle_spalte = [];
      }
    }
    if (aktuelle_spalte.length > 0) {
      while (aktuelle_spalte.length < 7) aktuelle_spalte.push(null);
      sp.push(aktuelle_spalte);
    }
    return sp;
  });

  function intensitaet(submissions: number): number {
    if (submissions === 0) return 0;
    if (submissions === 1) return 1;
    if (submissions <= 3) return 2;
    if (submissions <= 6) return 3;
    return 4;
  }

  let summe = $derived(karte.reduce((s, t) => s + t.submissions, 0));
  let bestanden_summe = $derived(karte.reduce((s, t) => s + t.bestanden, 0));
  let aktive_tage = $derived(karte.filter((t) => t.submissions > 0).length);
</script>

<div class="heatmap">
  <header class="kopf">
    <span class="titel">Aktivität letzte {ANZAHL_TAGE} Tage</span>
    <span class="zahlen">
      <span class="num">{aktive_tage}</span> aktive Tage,
      <span class="num">{bestanden_summe}</span> / <span class="num">{summe}</span> bestanden
    </span>
  </header>

  {#if geladen}
    <div class="raster">
      {#each spalten as spalte, sp_idx (sp_idx)}
        <div class="spalte">
          {#each spalte as zelle, zi (zi)}
            {#if zelle}
              <span
                class="zelle stufe-{intensitaet(zelle.submissions)}"
                title={`${zelle.datum}: ${zelle.submissions} Submissions, ${zelle.bestanden} bestanden`}
              ></span>
            {:else}
              <span class="zelle leer"></span>
            {/if}
          {/each}
        </div>
      {/each}
    </div>
    <div class="legende">
      <span>weniger</span>
      <span class="zelle stufe-0"></span>
      <span class="zelle stufe-1"></span>
      <span class="zelle stufe-2"></span>
      <span class="zelle stufe-3"></span>
      <span class="zelle stufe-4"></span>
      <span>mehr</span>
    </div>
  {/if}
</div>

<style>
  .heatmap {
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: var(--sp-3);
    border-radius: var(--radius-sm);
  }
  .kopf {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: var(--sp-2);
    font-size: var(--fs-xs);
  }
  .titel {
    color: var(--fg-dim);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .zahlen {
    color: var(--fg-mute);
  }
  .zahlen .num {
    color: var(--fg);
  }

  .raster {
    display: flex;
    gap: 3px;
    overflow-x: auto;
  }
  .spalte {
    display: flex;
    flex-direction: column;
    gap: 3px;
  }
  .zelle {
    width: 12px;
    height: 12px;
    border-radius: 2px;
    background: var(--bg-elev);
    border: 1px solid var(--border);
    box-sizing: border-box;
  }
  .zelle.leer {
    background: transparent;
    border: none;
  }
  .zelle.stufe-0 { background: var(--bg-elev); }
  .zelle.stufe-1 { background: color-mix(in srgb, var(--accent) 28%, var(--bg-elev)); border-color: color-mix(in srgb, var(--accent) 28%, transparent); }
  .zelle.stufe-2 { background: color-mix(in srgb, var(--accent) 50%, var(--bg-elev)); border-color: color-mix(in srgb, var(--accent) 50%, transparent); }
  .zelle.stufe-3 { background: color-mix(in srgb, var(--accent) 75%, var(--bg-elev)); border-color: color-mix(in srgb, var(--accent) 75%, transparent); }
  .zelle.stufe-4 { background: var(--accent); border-color: var(--accent); }

  .legende {
    margin-top: var(--sp-2);
    display: flex;
    align-items: center;
    gap: 4px;
    font-size: var(--fs-xs);
    color: var(--fg-mute);
    justify-content: flex-end;
  }
</style>
