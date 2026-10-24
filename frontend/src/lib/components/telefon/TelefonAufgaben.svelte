<script lang="ts">
  /* Aufgaben am Telefon: Suche, Sprachchips, Liste mit großen Zeilen. */
  import { onMount } from 'svelte';
  import { aufgabenStore } from '../../stores/AufgabenStore.svelte';
  import { progressStore } from '../../stores/ProgressStore.svelte';
  import { konfig } from '../../stores/KonfigStore.svelte';
  import { route } from '../../stores/RouteStore.svelte';
  import { aufgabenFilter as f } from '../../stores/AufgabenFilterStore.svelte';
  import { statusIcon, statusKlasse } from '../../anzeige';
  import { farbeZuCss } from '../../types/Konfig';
  import EmptyState from '../EmptyState.svelte';

  onMount(async () => {
    await Promise.all([
      aufgabenStore.liste.length === 0 ? aufgabenStore.ladeListe() : null,
      progressStore.gesamt ? null : progressStore.ladeAlles(),
    ]);
  });

  let mehrFilter = $state(false);
  let treffer = $derived(f.treffer);

  $effect(() => {
    void [f.suche, f.sprache, f.schwierigkeit, f.status, f.pfad];
    f.speichern();
  });
</script>

<div class="seite">
  <header class="seiten-kopf">
    <div class="titelzeile">
      <h1>Aufgaben</h1>
      <span class="treffer rechts"><span class="num">{treffer.length}</span></span>
    </div>
    <label class="suche">
      <i class="fa-solid fa-magnifying-glass" aria-hidden="true"></i>
      <input type="search" placeholder="Suchen" bind:value={f.suche} />
    </label>
    <div class="t-chips">
      <button class="chip" class:akz={!f.sprache} onclick={() => (f.sprache = '')}>Alle</button>
      {#each konfig.daten.sprachen as s (s.id)}
        <button class="chip" class:akz={f.sprache === s.id} onclick={() => (f.sprache = s.id)}>{s.titel}</button>
      {/each}
      <button class="chip" class:akz={mehrFilter || f.schwierigkeit !== '' || f.status !== ''} onclick={() => (mehrFilter = !mehrFilter)}>
        <i class="fa-solid fa-sliders" aria-hidden="true"></i>Filter
      </button>
    </div>
    {#if mehrFilter}
      <div class="mehr">
        <select class="wahl" bind:value={f.schwierigkeit} aria-label="Stufe">
          <option value="">Alle Stufen</option>
          {#each konfig.daten.schwierigkeiten as s (s.id)}<option value={s.id}>{s.titel}</option>{/each}
        </select>
        <select class="wahl" bind:value={f.status} aria-label="Status">
          <option value="">Alle Status</option>
          <option value="neu">Neu</option>
          <option value="in_arbeit">In Arbeit</option>
          <option value="geloest">Gelöst</option>
        </select>
      </div>
    {/if}
  </header>
  <div class="rollfeld t-liste">
    {#if aufgabenStore.fehler}
      <EmptyState icon="fa-plug-circle-xmark" titel="Server nicht erreichbar" hinweis={aufgabenStore.fehler} ctaText="Erneut versuchen" ctaAction={() => aufgabenStore.ladeListe()} />
    {:else if !aufgabenStore.ladenListe && treffer.length === 0}
      <EmptyState icon="fa-magnifying-glass" titel="Kein Treffer" ctaText="Filter zurücksetzen" ctaAction={() => f.zuruecksetzen()} />
    {/if}
    {#each treffer as a (a.id)}
      {@const st = progressStore.status(a.id)}
      <button class="t-eintrag" onclick={() => route.setze('aufgabe', a.id)}>
        <i class="fa-solid {a.gesperrt ? 'fa-lock' : statusIcon(st)} status-i {statusKlasse(st)}" aria-hidden="true"></i>
        <span class="text">
          <b>{a.titel}</b>
          <span class="unter">
            <span class="badge" style:color={farbeZuCss(konfig.schwierigkeitFarbe(a.schwierigkeit))}>{konfig.schwierigkeitTitel(a.schwierigkeit)}</span>
            <span class="badge sprache">{konfig.sprache(a.sprache)?.titel ?? a.sprache}</span>
            <span>{a.schaetz_minuten} min</span>
            <span class="num">{progressStore.proAufgabe[a.id]?.punkte_erreicht ?? 0}/{a.schwierigkeit_score}</span>
          </span>
        </span>
        <i class="fa-solid fa-chevron-right" aria-hidden="true"></i>
      </button>
    {/each}
  </div>
</div>

<style>
  .rechts { margin-left: auto; }
  .suche { height: 44px; }
  .text { min-width: 0; }
  .mehr {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--sp-2);
  }
</style>
