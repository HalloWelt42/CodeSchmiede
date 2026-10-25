<script lang="ts">
  /*
   * Belohnungsmoment nach dem Bestehen: Punkte, Fortschritt der Stufe,
   * neue Bestwerte und Erfolge, Stand des Tagesauftrags. Der Balken der
   * Stufe läuft vom alten zum neuen Stand.
   */
  import { onMount } from 'svelte';
  import type { Belohnung, Bestwert } from '../../api/SpielApi';
  import { stufenAnteil } from '../../stores/SpielStore.svelte';
  import { medaille, RANG_NAME, zahl } from '../../spielanzeige';

  let { belohnung: b }: { belohnung: Belohnung } = $props();

  let grund = $derived.by(() => {
    if (b.aufgegeben) return 'Musterlösung vorher angesehen';
    if (b.wiederholung && b.punkte === 0) return 'Wiederholung, Punkte schon gutgeschrieben';
    if (b.hinweise === 0) return b.erster_versuch ? 'ohne Hinweis, im ersten Versuch' : 'ohne Hinweis';
    return b.hinweise === 1 ? 'mit einem Hinweis' : `mit ${b.hinweise} Hinweisen`;
  });

  let erledigt = $derived(b.auftrag.ziele.filter((z) => z.erledigt).length);
  let aufgestiegen = $derived(b.stufe.stufe > b.stufe_vorher);

  // Balken startet beim alten Stand (bei neuer Stufe bei null) und läuft zum neuen
  let anteil = $state(0);
  onMount(() => {
    const vorher = { ...b.stufe, punkte: b.stufe.punkte - b.punkte - b.auftrag_bonus };
    anteil = aufgestiegen ? 0 : stufenAnteil(vorher);
    requestAnimationFrame(() => requestAnimationFrame(() => (anteil = stufenAnteil(b.stufe))));
  });

  function bestwertText(w: Bestwert): { icon: string; text: string } {
    if (w.art === 'zeichen') return { icon: 'fa-compress', text: `Neuer Bestwert: ${w.neu} Zeichen, vorher ${w.vorher}` };
    if (w.art === 'laufzeit') {
      return { icon: 'fa-gauge-high', text: `Neuer Bestwert: ${Math.round(w.neu)} ms, vorher ${Math.round(w.vorher)} ms` };
    }
    return { icon: 'fa-star', text: `Mehr Sterne: ${w.neu}, vorher ${w.vorher}` };
  }
</script>

<div class="belohnung">
  <div class="belohnung-kopf">
    <span class="plus">+{b.punkte}</span>
    <span>von {b.punkte_moeglich} Punkten, {grund}</span>
    {#if b.sterne !== null}
      <span class="sterne gross" title="{b.sterne} von 3 Sternen">
        {#each [1, 2, 3] as s (s)}<i class="fa-solid fa-star" class:aus={s > (b.sterne ?? 0)} aria-hidden="true"></i>{/each}
      </span>
    {/if}
  </div>
  <div class="zeile">
    <i class="fa-solid {aufgestiegen ? 'fa-arrow-up' : 'fa-hammer'}" aria-hidden="true"></i>
    {#if aufgestiegen}
      Neue Stufe {b.stufe.stufe}, {b.stufe.titel}: <span class="num">{zahl(b.stufe.punkte)}</span> / <span class="num">{zahl(b.stufe.bis)}</span>
    {:else}
      Stufe {b.stufe.stufe}: <span class="num">{zahl(b.stufe.punkte)}</span> / <span class="num">{zahl(b.stufe.bis)}</span>
    {/if}
  </div>
  <div class="balken"><span style:width="{anteil}%"></span></div>
  {#each b.bestwerte as w (w.art)}
    {@const t = bestwertText(w)}
    <div class="zeile"><i class="fa-solid {t.icon}" aria-hidden="true"></i>{t.text}</div>
  {/each}
  {#each b.neue_erfolge as e (e.id)}
    <div class="zeile">
      <span class="medaille {medaille(e.rang)}"><i class="fa-solid {e.icon}" aria-hidden="true"></i></span>
      Erfolg: {e.titel}{#if e.rang}, {RANG_NAME[e.rang]}{/if}
    </div>
  {/each}
  {#if b.auftrag_bonus > 0}
    <div class="zeile"><i class="fa-solid fa-bullseye" aria-hidden="true"></i>Tagesauftrag erledigt, +{b.auftrag_bonus} Punkte</div>
  {:else if !b.auftrag.gutgeschrieben && b.auftrag.ziele.length > 0}
    <div class="zeile dim"><i class="fa-solid fa-bullseye" aria-hidden="true"></i>Tagesauftrag: {erledigt} von {b.auftrag.ziele.length} erledigt</div>
  {/if}
</div>

<style>
  .belohnung-kopf .sterne { margin-left: auto; }
</style>
