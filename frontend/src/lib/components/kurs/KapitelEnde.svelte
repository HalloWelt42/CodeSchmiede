<script lang="ts">
  /*
   * Ende der Einführung: was man jetzt kann, die Sammelkarte (verdeckt, bis auch die Übungen geschafft sind), die
   * Übungen des Kapitels der Reihe nach, das Stück des Kapitelprojekts und die freiwillige Vertiefung.
   */
  import type { EinfuehrungSicht, KapitelSicht, UebungSicht } from '../../api/KursApi';
  import { route } from '../../stores/RouteStore.svelte';
  import { kursStore } from '../../stores/KursStore.svelte';
  import Sammelkarte from './Sammelkarte.svelte';

  interface Props {
    einfuehrung: EinfuehrungSicht;
    kapitel: KapitelSicht | null;
  }
  let { einfuehrung, kapitel }: Props = $props();

  let naechste = $derived(kapitel ? [...kapitel.uebungen, ...kapitel.projekt].find((u) => !u.geloest) ?? null : null);
</script>

{#snippet liste(titel: string, uebungen: UebungSicht[])}
  {#if uebungen.length}
    <div class="block">
      <div class="block-kopf"><span>{titel}</span><span class="num">{uebungen.filter((u) => u.geloest).length} / {uebungen.length}</span></div>
      <div class="schritt-liste">
        {#each uebungen as u, i (u.id)}
          <button class="schritt uebung" class:jetzt={u.id === naechste?.id} onclick={() => route.setze('aufgabe', u.id)}>
            <span class="nr">{i + 1}</span><span class="t">{u.titel}</span>
            <i class="fa-solid {u.geloest ? 'fa-circle-check' : 'fa-circle'}" style={u.geloest ? 'color:var(--green)' : ''} aria-hidden="true"></i>
          </button>
        {/each}
      </div>
    </div>
  {/if}
{/snippet}

<div class="kapitel-ende">
  <div><div class="dachzeile">Einführung geschafft</div><h2>{einfuehrung.titel}</h2></div>
  <div class="ende-raster">
    <div class="block">
      <div class="block-kopf"><span>Das kannst du jetzt</span></div>
      <ul class="lernziele">{#each einfuehrung.lernziele as z (z)}<li><i class="fa-solid fa-check" aria-hidden="true"></i><span>{z}</span></li>{/each}</ul>
    </div>
    {#if kapitel}
      <Sammelkarte {kapitel} sprache={einfuehrung.sprache} sprachTitel={kursStore.sprachTitel(einfuehrung.sprache)} breite={170} mitSatz />
    {/if}
  </div>
  {#if kapitel}
    {@render liste('Übungen', kapitel.uebungen)}
    {@render liste('Kapitelprojekt', kapitel.projekt)}
    {#if kapitel.vertiefung.length}
      <div class="block">
        <div class="block-kopf"><span>Vertiefung, freiwillig</span></div>
        <div class="chips">{#each kapitel.vertiefung as v (v.id)}<button class="chip" onclick={() => route.setze('aufgabe', v.id)}>{v.titel}</button>{/each}</div>
      </div>
    {/if}
    <div class="weiter-zeile">
      <button class="knopf" onclick={() => route.setze('merkblatt', einfuehrung.id)}><i class="fa-solid fa-note-sticky" aria-hidden="true"></i>Merkblatt</button>
      {#if naechste}
        <button class="knopf voll" onclick={() => naechste && route.setze('aufgabe', naechste.id)}><i class="fa-solid fa-code" aria-hidden="true"></i>Üben: {naechste.titel}</button>
      {:else}
        <button class="knopf voll" onclick={() => route.setze('kurs')}><i class="fa-solid fa-arrow-right" aria-hidden="true"></i>Zur Kursübersicht</button>
      {/if}
    </div>
  {/if}
</div>

<style>
  .kapitel-ende { display: flex; flex-direction: column; gap: var(--sp-3); font-family: var(--sans); font-size: var(--fs-md); }
  .ende-raster { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: var(--sp-3); align-items: start; }
  .uebung { width: 100%; border: 1px solid transparent; background: transparent; color: var(--fg); cursor: pointer; text-align: left; }
  .uebung:hover:not(:disabled) { background: var(--bg-card-2); color: var(--fg); }
  .chip { cursor: pointer; background: transparent; }
</style>
