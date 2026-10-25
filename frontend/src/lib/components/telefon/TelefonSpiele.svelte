<script lang="ts">
  /* Spielebereich am Telefon: je Spiel eine Zeile, ein Tipp öffnet das nächste Level. */
  import { onMount } from 'svelte';
  import type { SpielUebersicht } from '../../api/SpielApi';
  import { progressStore } from '../../stores/ProgressStore.svelte';
  import { route } from '../../stores/RouteStore.svelte';
  import { spielStore } from '../../stores/SpielStore.svelte';
  import Seite from '../Seite.svelte';

  onMount(() => {
    void progressStore.ladeAlles();
  });

  let spiele = $derived(spielStore.spiele);
  let sterne = $derived(spiele.reduce((s, x) => s + x.sterne, 0));
  let moeglich = $derived(spiele.reduce((s, x) => s + x.sterne_moeglich, 0));
  const sterneVon = (s: SpielUebersicht) => (s.sterne_moeglich ? Math.round((3 * s.sterne) / s.sterne_moeglich) : 0);
  const oeffne = (s: SpielUebersicht) => {
    const ziel = s.naechstes ?? s.levels[0];
    if (ziel) route.setze('aufgabe', ziel.id);
  };
</script>

<Seite titel="Spiele" lead="{sterne} von {moeglich} Sternen">
  <div class="t-liste">
    {#each spiele as s (s.id)}
      <button class="t-eintrag" onclick={() => oeffne(s)}>
        <i class="fa-solid {s.icon} spiel-icon" aria-hidden="true"></i>
        <div class="text">
          <b>{s.titel}</b>
          <div class="unter">
            <span class="num">{s.geschafft} / {s.levels.length}</span>
            <span class="balken"><span style:width="{s.levels.length ? (s.geschafft / s.levels.length) * 100 : 0}%"></span></span>
            <span class="sterne">{#each [1, 2, 3] as n (n)}<i class="fa-solid fa-star" class:aus={n > sterneVon(s)} aria-hidden="true"></i>{/each}</span>
          </div>
        </div>
        <i class="fa-solid fa-chevron-right" aria-hidden="true"></i>
      </button>
    {/each}
  </div>
</Seite>

<style>
  .spiel-icon {
    color: var(--accent);
    font-size: 20px;
  }
  .text { min-width: 0; }
  .balken {
    flex: 1;
    min-width: 60px;
  }
</style>
