<script lang="ts">
  /* Pfade am Telefon: Sprachchips, Zeilen mit Stand; Antippen klappt die Schritte auf. */
  import { onMount } from 'svelte';
  import { aufgabenStore } from '../../stores/AufgabenStore.svelte';
  import { pfadeStore } from '../../stores/PfadeStore.svelte';
  import { progressStore } from '../../stores/ProgressStore.svelte';
  import { konfig } from '../../stores/KonfigStore.svelte';
  import { route } from '../../stores/RouteStore.svelte';
  import { statusIcon, statusKlasse } from '../../anzeige';
  import { pfadGeloest, pfadProzent, pfadSprache } from '../../pfade.svelte';

  onMount(async () => {
    await Promise.all([
      pfadeStore.liste.length === 0 ? pfadeStore.ladeListe() : null,
      aufgabenStore.liste.length === 0 ? aufgabenStore.ladeListe() : null,
      progressStore.gesamt ? null : progressStore.ladeAlles(),
    ]);
  });

  let sprache = $state('');
  let offen = $state<string | null>(null);
  let liste = $derived(pfadeStore.liste.filter((p) => !sprache || pfadSprache(p) === sprache));
</script>

<div class="seite">
  <header class="seiten-kopf">
    <div class="titelzeile">
      <h1>Pfade</h1>
      <span class="treffer rechts"><span class="num">{liste.length}</span></span>
    </div>
    <div class="t-chips">
      <button class="chip" class:akz={!sprache} onclick={() => (sprache = '')}>Alle</button>
      {#each konfig.daten.sprachen as s (s.id)}
        <button class="chip" class:akz={sprache === s.id} onclick={() => (sprache = s.id)}>{s.titel}</button>
      {/each}
    </div>
  </header>
  <div class="rollfeld t-liste">
    {#each liste as p (p.id)}
      {@const auf = offen === p.id}
      <button class="t-eintrag" onclick={() => (offen = auf ? null : p.id)} aria-expanded={auf}>
        <i class="fa-solid fa-route akzent" aria-hidden="true"></i>
        <span class="text">
          <b>{p.titel}</b>
          <span class="unter">
            <span class="badge sprache">{konfig.sprache(pfadSprache(p))?.titel ?? '-'}</span>
            <span class="num">{pfadGeloest(p)} / {p.reihenfolge.length}</span>
            <span class="balken breit"><span style:width="{pfadProzent(p)}%"></span></span>
          </span>
        </span>
        <i class="fa-solid {auf ? 'fa-chevron-down' : 'fa-chevron-right'}" aria-hidden="true"></i>
      </button>
      {#if auf}
        <div class="schritte">
          {#each p.reihenfolge as id, i (id)}
            {@const st = progressStore.status(id)}
            <button class="schritt {statusKlasse(st)}" onclick={() => route.setze('aufgabe', id)}>
              <span class="nr num">{i + 1}</span>
              <span class="t">{aufgabenStore.findeKurz(id)?.titel ?? id}</span>
              <i class="fa-solid {statusIcon(st)}" aria-hidden="true"></i>
            </button>
          {/each}
        </div>
      {/if}
    {/each}
  </div>
</div>

<style>
  .rechts { margin-left: auto; }
  .text { min-width: 0; }
  .akzent { color: var(--accent); }
  .breit { flex: 1; min-width: 60px; }
  .schritte {
    display: flex;
    flex-direction: column;
    padding: 0 0 var(--sp-2) 34px;
    border-bottom: 1px solid var(--border);
  }
  .schritt {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    min-height: 44px;
    padding: 0;
    border: 0;
    border-radius: 0;
    background: transparent;
    color: var(--fg);
    font-size: var(--fs-sm);
    text-align: left;
  }
  .schritt:hover:not(:disabled) { background: transparent; }
  .nr { width: 22px; text-align: right; color: var(--fg-mute); font-size: var(--fs-xs); flex: none; }
  .t { min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .schritt i { margin-left: auto; color: var(--fg-mute); }
  .schritt.geloest i { color: var(--green); }
  .schritt.arbeit i { color: var(--orange); }
</style>
