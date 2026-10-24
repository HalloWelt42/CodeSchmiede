<script lang="ts">
  /* Erfolge als schmale Liste: erreichte mit Akzent, offene mit Stand. */
  import { onMount } from 'svelte';
  import { progressApi } from '../api/ProgressApi';
  import type { Achievement } from '../api/ProgressApi';

  let liste = $state<Achievement[]>([]);
  let erreicht = $state(0);
  let gesamt = $state(0);

  onMount(async () => {
    try {
      const r = await progressApi.achievements();
      liste = r.eintraege;
      erreicht = r.erreicht_anzahl;
      gesamt = r.gesamt_anzahl;
    } catch {
      liste = [];
    }
  });
</script>

<div class="block">
  <div class="block-kopf"><span>Erfolge</span><span class="num">{erreicht} / {gesamt}</span></div>
  {#each liste as a (a.id)}
    <div class="erfolg" class:da={a.erreicht} title={a.beschreibung}>
      <i class="fa-solid {a.icon}" aria-hidden="true"></i>
      <span class="name">{a.titel}</span>
      <span class="dim num">{Math.min(a.fortschritt, a.ziel)} / {a.ziel}</span>
    </div>
  {/each}
</div>

<style>
  .erfolg {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    padding: 5px 0;
    border-bottom: 1px solid var(--border);
    font-size: var(--fs-sm);
  }
  .erfolg:last-child { border-bottom: 0; }
  .erfolg i {
    width: 20px;
    text-align: center;
    color: var(--fg-mute);
  }
  .erfolg.da i { color: var(--orange); }
  .name {
    min-width: 0;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .erfolg .dim {
    margin-left: auto;
    font-size: var(--fs-xs);
  }
</style>
