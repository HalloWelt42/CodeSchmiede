<script lang="ts">
  /*
   * Streak-Heatmap im GitHub-Contribution-Style.
   * Zeigt ein ganzes Jahr (53 Wochen-Spalten x 7 Wochentage), mit
   * Pfeilen zum Vor- und Zurueck-Blaettern. Default: aktuelles Jahr.
   */
  import { onMount } from 'svelte';
  import { progressApi } from '../api/ProgressApi';
  import type { HeatmapTag } from '../api/ProgressApi';

  let tage = $state<HeatmapTag[]>([]);
  let geladen = $state(false);
  let aktuelles_jahr = $state(new Date().getFullYear());
  const HEUTE_JAHR = new Date().getFullYear();

  onMount(async () => {
    await ladeJahr(aktuelles_jahr);
  });

  async function ladeJahr(jahr: number): Promise<void> {
    geladen = false;
    try {
      const r = await progressApi.heatmapJahr(jahr);
      tage = r.tage;
    } catch {
      tage = [];
    } finally {
      geladen = true;
    }
  }

  function vorheriges_jahr(): void {
    aktuelles_jahr -= 1;
    void ladeJahr(aktuelles_jahr);
  }
  function naechstes_jahr(): void {
    if (aktuelles_jahr >= HEUTE_JAHR) return;
    aktuelles_jahr += 1;
    void ladeJahr(aktuelles_jahr);
  }
  function dieses_jahr(): void {
    if (aktuelles_jahr === HEUTE_JAHR) return;
    aktuelles_jahr = HEUTE_JAHR;
    void ladeJahr(aktuelles_jahr);
  }

  function formatiere_datum(d: Date): string {
    // 'en-CA' liefert YYYY-MM-DD im lokalen Timezone -- ohne UTC-Shift
    return d.toLocaleDateString('en-CA');
  }

  // Erzeugt fuer ein ganzes Jahr alle Tage mit Submission-Werten gemerged.
  let karte = $derived.by(() => {
    const map = new Map<string, HeatmapTag>();
    for (const t of tage) map.set(t.datum, t);
    const start = new Date(aktuelles_jahr, 0, 1);
    const ende = new Date(aktuelles_jahr, 11, 31);
    const ergebnisse: { datum: string; submissions: number; bestanden: number; wochentag: number; monat: number }[] = [];
    const d = new Date(start);
    while (d <= ende) {
      const iso = formatiere_datum(d);
      const t = map.get(iso);
      ergebnisse.push({
        datum: iso,
        submissions: t?.submissions ?? 0,
        bestanden: t?.bestanden ?? 0,
        wochentag: d.getDay(),
        monat: d.getMonth(),
      });
      d.setDate(d.getDate() + 1);
    }
    return ergebnisse;
  });

  // Gruppiere die Tage in Wochen-Spalten (Montag startet eine Spalte).
  type Zelle = { datum: string; submissions: number; bestanden: number; monat: number } | null;
  let spalten = $derived.by(() => {
    const sp: Zelle[][] = [];
    if (karte.length === 0) return sp;
    function montag_idx(wt: number): number {
      return (wt + 6) % 7;
    }
    let aktuelle: Zelle[] = [];
    for (let i = 0; i < montag_idx(karte[0].wochentag); i++) aktuelle.push(null);
    for (const t of karte) {
      aktuelle.push({
        datum: t.datum,
        submissions: t.submissions,
        bestanden: t.bestanden,
        monat: t.monat,
      });
      if (montag_idx(t.wochentag) === 6) {
        sp.push(aktuelle);
        aktuelle = [];
      }
    }
    if (aktuelle.length > 0) {
      while (aktuelle.length < 7) aktuelle.push(null);
      sp.push(aktuelle);
    }
    return sp;
  });

  // Monats-Label oberhalb des Rasters: nur einmal pro Monat zeigen,
  // an der Spalte wo der erste Tag des Monats erscheint.
  const MONATSNAMEN = ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez'];
  let monatslabels = $derived.by(() => {
    const labels: { spalte_idx: number; label: string }[] = [];
    let letzter_monat = -1;
    spalten.forEach((sp, i) => {
      // Erster nicht-null Eintrag der Spalte
      const erste = sp.find((z) => z !== null);
      if (!erste) return;
      if (erste.monat !== letzter_monat) {
        labels.push({ spalte_idx: i, label: MONATSNAMEN[erste.monat] });
        letzter_monat = erste.monat;
      }
    });
    return labels;
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

  let kann_vor = $derived(aktuelles_jahr < HEUTE_JAHR);
</script>

<div class="heatmap">
  <header class="kopf">
    <span class="titel">Aktivität {aktuelles_jahr}</span>
    <span class="zahlen">
      <span class="num">{aktive_tage}</span> aktive Tage,
      <span class="num">{bestanden_summe}</span> / <span class="num">{summe}</span> bestanden
    </span>
    <span class="nav">
      <button type="button" onclick={vorheriges_jahr} aria-label="Vorheriges Jahr" title="Vorheriges Jahr">
        <i class="fa-solid fa-chevron-left" aria-hidden="true"></i>
      </button>
      <button type="button" onclick={dieses_jahr} disabled={aktuelles_jahr === HEUTE_JAHR} class="heute-btn" title="Aktuelles Jahr">
        Heute
      </button>
      <button type="button" onclick={naechstes_jahr} disabled={!kann_vor} aria-label="Nächstes Jahr" title="Nächstes Jahr">
        <i class="fa-solid fa-chevron-right" aria-hidden="true"></i>
      </button>
    </span>
  </header>

  {#if geladen}
    <div class="raster-wrap">
      <div class="raster">
        <div class="spalte spalte-monate">
          {#each monatslabels as ml (ml.spalte_idx)}
            <span class="monat-label" style="left: {ml.spalte_idx * 15}px">{ml.label}</span>
          {/each}
        </div>
        <div class="raster-zeilen">
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
      </div>
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
    gap: var(--sp-3);
  }
  .titel {
    color: var(--fg-dim);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .zahlen {
    color: var(--fg-mute);
    flex: 1;
  }
  .zahlen .num {
    color: var(--fg);
  }
  .nav {
    display: inline-flex;
    gap: 4px;
    align-items: center;
  }
  .nav button {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--fg-dim);
    width: 28px;
    height: 24px;
    border-radius: var(--radius-sm);
    cursor: pointer;
    font-size: var(--fs-xs);
    padding: 0;
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }
  .nav button:hover:not(:disabled) {
    color: var(--accent);
    border-color: var(--accent);
  }
  .nav button:disabled {
    opacity: 0.4;
    cursor: not-allowed;
  }
  .nav .heute-btn {
    width: auto;
    padding: 0 8px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  .raster-wrap {
    overflow-x: auto;
    padding-bottom: 4px;
  }
  .raster {
    display: flex;
    flex-direction: column;
    gap: 4px;
    min-width: max-content;
  }
  .spalte-monate {
    position: relative;
    height: 14px;
    margin-left: 0;
  }
  .monat-label {
    position: absolute;
    color: var(--fg-mute);
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }
  .raster-zeilen {
    display: flex;
    gap: 3px;
  }
  .spalte:not(.spalte-monate) {
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
