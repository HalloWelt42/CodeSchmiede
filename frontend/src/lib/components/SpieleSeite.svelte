<script lang="ts">
  /* Spielebereich am Rechner: je Spiel eine Karte mit Stand, Level-Leiste und Weiter. */
  import { onMount } from 'svelte';
  import type { LevelStand, SpielUebersicht } from '../api/SpielApi';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import { spielStore } from '../stores/SpielStore.svelte';
  import { zahl } from '../spielanzeige';
  import Seite from './Seite.svelte';
  import SpielBild from './spiel/SpielBild.svelte';

  onMount(() => {
    void progressStore.ladeAlles();
  });

  let spiele = $derived(spielStore.spiele);
  let summe = $derived({
    levels: spiele.reduce((s, x) => s + x.levels.length, 0),
    geschafft: spiele.reduce((s, x) => s + x.geschafft, 0),
    sterne: spiele.reduce((s, x) => s + x.sterne, 0),
    sterneMoeglich: spiele.reduce((s, x) => s + x.sterne_moeglich, 0),
    punkte: spiele.reduce((s, x) => s + x.punkte, 0),
  });

  /** Sterne eines Spiels auf drei verdichtet: Anteil der möglichen Sterne */
  const sterneVon = (s: SpielUebersicht) => (s.sterne_moeglich ? Math.round((3 * s.sterne) / s.sterne_moeglich) : 0);
  const oeffne = (l: LevelStand | null | undefined) => l && route.setze('aufgabe', l.id);
  const ziel = (s: SpielUebersicht) => s.naechstes ?? s.levels[0];
</script>

<Seite titel="Spiele" lead="Jedes Level zählt in Punkte, Serie und Tagesauftrag">
  {#snippet kopf()}
    {#if spiele.length}
      <div class="kennzahlen">
        <div class="kennzahl"><span class="num">{summe.geschafft} / {summe.levels}</span><small>Level</small></div>
        <div class="kennzahl"><span class="num">{summe.sterne} / {summe.sterneMoeglich}</span><small>Sterne</small></div>
        <div class="kennzahl"><span class="num">{zahl(summe.punkte)}</span><small>Punkte aus Spielen</small></div>
      </div>
    {/if}
  {/snippet}

  <div class="spiel-raster">
    {#each spiele as s (s.id)}
      {@const naechstes = s.naechstes}
      {@const weiterText = naechstes ? `Weiter: Level ${naechstes.nummer}, ${naechstes.titel}` : 'Alle Level geschafft; mehr Sterne holen?'}
      <div class="spiel-karte">
        <button class="spiel-bild" onclick={() => oeffne(ziel(s))} aria-label="{s.titel} spielen"><SpielBild id={s.id} /></button>
        <div class="spiel-text">
          <h2><i class="fa-solid {s.icon}" aria-hidden="true"></i>{s.titel}</h2>
          <p>{s.beschreibung}</p>
          <div class="spiel-stand">
            <span class="num">{s.geschafft} / {s.levels.length}</span>
            <span class="balken"><span style:width="{s.levels.length ? (s.geschafft / s.levels.length) * 100 : 0}%"></span></span>
            <span class="sterne" title="{s.sterne} von {s.sterne_moeglich} Sternen">
              {#each [1, 2, 3] as n (n)}<i class="fa-solid fa-star" class:aus={n > sterneVon(s)} aria-hidden="true"></i>{/each}
            </span>
          </div>
          <div class="level-leiste">
            {#each s.levels as l (l.id)}
              <button
                class="level-punkt"
                class:fertig={l.geloest}
                class:aktuell={naechstes?.id === l.id}
                class:zu={!l.geloest && naechstes !== null && l.nummer > naechstes.nummer}
                title="Level {l.nummer}: {l.titel}{l.sterne ? `, ${l.sterne} ${l.sterne === 1 ? 'Stern' : 'Sterne'}` : ''}"
                onclick={() => oeffne(l)}
              >{l.nummer}</button>
            {/each}
          </div>
          <div class="spiel-weiter">
            <span class="naechstes dim" title={weiterText}>{weiterText}</span>
            <button class="knopf primaer" onclick={() => oeffne(ziel(s))}><i class="fa-solid fa-play" aria-hidden="true"></i>Spielen</button>
          </div>
        </div>
      </div>
    {/each}
  </div>
</Seite>

<style>
  .spiel-weiter .knopf { margin-left: auto; }
</style>
