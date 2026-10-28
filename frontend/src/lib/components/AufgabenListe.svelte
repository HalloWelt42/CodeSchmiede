<script lang="ts">
  /* Aufgabenliste am Rechner: Filter im festen Kopf, Tabelle mit fester Kopfzeile. */
  import { onMount } from 'svelte';
  import { aufgabenStore } from '../stores/AufgabenStore.svelte';
  import { pfadeStore } from '../stores/PfadeStore.svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { konfig } from '../stores/KonfigStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import { aufgabenFilter as f } from '../stores/AufgabenFilterStore.svelte';
  import { statusIcon, statusKlasse } from '../anzeige';
  import { farbeZuCss } from '../types/Konfig';
  import AufgabenFilter from './AufgabenFilter.svelte';
  import EmptyState from './EmptyState.svelte';
  import Seite from './Seite.svelte';

  onMount(async () => {
    await Promise.all([
      aufgabenStore.liste.length === 0 ? aufgabenStore.ladeListe() : null,
      progressStore.gesamt ? null : progressStore.ladeAlles(),
      pfadeStore.liste.length === 0 ? pfadeStore.ladeListe() : null,
    ]);
  });

  let treffer = $derived(f.treffer);

  let lead = $derived.by(() => {
    const g = progressStore.gesamt;
    const n = aufgabenStore.liste.length;
    const sprachen = new Set(aufgabenStore.liste.map((a) => a.sprache)).size;
    return g
      ? `${n} Aufgaben in ${sprachen} Sprachen, ${g.aufgaben_geloest} gelöst, ${g.aufgaben_in_arbeit} in Arbeit`
      : `${n} Aufgaben`;
  });

  function titelVon(id: string): string {
    return aufgabenStore.findeKurz(id)?.titel ?? id;
  }
</script>

<Seite titel="Aufgaben" lead={aufgabenStore.liste.length ? lead : undefined} ohneRand>
  {#snippet kopf()}
    {#if aufgabenStore.liste.length > 0}
      <AufgabenFilter treffer={treffer.length} />
    {/if}
  {/snippet}

  {#if aufgabenStore.ladenListe}
    <p class="leer-zeile">Lade Aufgaben ...</p>
  {:else if aufgabenStore.fehler}
    <EmptyState
      icon="fa-plug-circle-xmark"
      titel="Server nicht erreichbar"
      hinweis={`Die Aufgaben ließen sich nicht laden (${aufgabenStore.fehler}).`}
      ctaText="Erneut versuchen"
      ctaAction={() => aufgabenStore.ladeListe()}
    />
  {:else if aufgabenStore.liste.length === 0}
    <EmptyState icon="fa-folder-open" titel="Noch keine Aufgaben" hinweis="Lege ein Verzeichnis unter aufgaben/python/NNN-id/ an." />
  {:else if treffer.length === 0}
    <EmptyState
      icon="fa-magnifying-glass"
      titel="Kein Treffer"
      hinweis="Passe die Filter an oder setze sie zurück."
      ctaText="Filter zurücksetzen"
      ctaAction={() => f.zuruecksetzen()}
    />
  {:else}
    <div class="tabelle">
      <div class="t-kopf cols">
        <span></span><span>Aufgabe</span><span>Stufe</span><span>Sprache</span>
        <span class="rechts-b">Zeit</span><span class="rechts-b">Punkte</span><span>Tags</span>
      </div>
      {#each treffer as a (a.id)}
        {@const st = progressStore.status(a.id)}
        <div
          class="t-zeile cols {statusKlasse(st)}"
          class:gesperrt={a.gesperrt}
          role="button"
          tabindex="0"
          onclick={() => route.setze('aufgabe', a.id)}
          onkeydown={(e) => { if (e.key === 'Enter') route.setze('aufgabe', a.id); }}
        >
          <i class="fa-solid {a.gesperrt ? 'fa-lock' : statusIcon(st)} status-i {statusKlasse(st)}" aria-hidden="true"></i>
          <span class="zelle-titel">
            <b>{a.titel}</b>
            {#if a.gesperrt}
              <span>Erst lösen: {a.voraussetzungen_offen.map(titelVon).join(', ')}</span>
            {:else}
              <span>{a.id}</span>
            {/if}
          </span>
          <span><span class="badge" style:color={farbeZuCss(konfig.schwierigkeitFarbe(a.schwierigkeit))}>{konfig.schwierigkeitTitel(a.schwierigkeit)}</span></span>
          <span><span class="badge sprache">{konfig.sprache(a.sprache)?.titel ?? a.sprache}</span></span>
          <span class="rechts-b dim">{a.schaetz_minuten} min</span>
          <span class="rechts-b num">{progressStore.proAufgabe[a.id]?.punkte_erreicht ?? 0}/{a.schwierigkeit_score}</span>
          <span class="zelle-tags">
            {#each a.tags as tag (tag)}
              <button
                class="tag"
                class:aktiv={f.suche.trim() === `#${tag}`}
                onclick={(e) => { e.stopPropagation(); f.schlagwort(tag); }}
              >#{tag}</button>
            {/each}
          </span>
        </div>
      {/each}
    </div>
  {/if}
</Seite>

<style>
  /* feste Spalten wachsen mit der Schrift (--schrift-zoom), damit Kopf und Werte nicht über den Rand ragen */
  .cols {
    --z: var(--schrift-zoom, 1);
    grid-template-columns: calc(20px * var(--z)) minmax(0, 2.6fr) calc(124px * var(--z)) calc(96px * var(--z)) calc(52px * var(--z)) calc(56px * var(--z)) minmax(0, 1.4fr);
  }
  .zelle-tags .tag {
    border: 0;
    padding: 0;
    background: transparent;
    line-height: 18px;
  }
  .zelle-tags .tag:hover,
  .zelle-tags .tag.aktiv {
    color: var(--accent);
    background: transparent;
  }
</style>
