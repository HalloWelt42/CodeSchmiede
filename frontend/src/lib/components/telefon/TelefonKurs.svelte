<script lang="ts">
  /* Kurs am Telefon: Sprachwahl, Karte "Weiter hier" und die Kapitel; ein Tipp öffnet die Einführung. */
  import { onMount } from 'svelte';
  import type { KapitelSicht } from '../../api/KursApi';
  import { route } from '../../stores/RouteStore.svelte';
  import { kursStore } from '../../stores/KursStore.svelte';
  import { oeffneKapitel, weiterText } from '../../kurs/weiter';

  onMount(() => {
    void kursStore.laden(true);
  });

  const MARKE: Record<KapitelSicht['stand'], [string, string]> = {
    fertig: ['fa-circle-check', 'Fertig'],
    uebersprungen: ['fa-forward', 'Per Kurztest'],
    aktuell: ['fa-circle-play', 'Weiter hier'],
    offen: ['fa-circle', 'Offen'],
    zu: ['fa-lock', 'Noch zu'],
  };
  let alle = $derived(kursStore.alleKapitel());
  let weiter = $derived(kursStore.weiter);
  let geschafft = $derived(alle.filter((k) => k.stand === 'fertig' || k.stand === 'uebersprungen').length);
</script>

<div class="seite" data-sprache={kursStore.sprache}>
  <header class="seiten-kopf">
    <div class="titelzeile"><h1>Kurs</h1><span class="treffer" style="margin-left:auto"><span class="num">{geschafft}</span> / {alle.length} Kapitel</span></div>
    <div class="t-chips">
      {#each kursStore.kurse as k (k.sprache)}
        <button class="chip" class:akz={k.sprache === kursStore.sprache} onclick={() => kursStore.waehleSprache(k.sprache)}>{k.titel}</button>
      {/each}
    </div>
  </header>
  <div class="rollfeld">
    {#if weiter}
      <button class="weiter-karte" onclick={() => oeffneKapitel(weiter)}>
        <span class="mini-karte"><i class="fa-solid fa-graduation-cap" aria-hidden="true"></i></span>
        <span class="text"><small>Weiter hier, Kapitel {weiter.nr}</small><b>{weiter.titel}</b><small>{weiterText(weiter)}</small></span>
      </button>
    {/if}
    {#each kursStore.kurs?.bloecke ?? [] as b (b.titel)}
      <div class="gruppe">{b.titel}</div>
      {#each b.kapitel as k (k.einfuehrung)}
        <button class="kapitel" class:zu={k.stand === 'zu'} disabled={k.stand === 'zu'} onclick={() => route.setze('einfuehrung', k.einfuehrung)}>
          <span class="mini-karte" class:leer={k.stand === 'zu'}><i class="fa-solid {k.stand === 'zu' ? 'fa-lock' : 'fa-graduation-cap'}" aria-hidden="true"></i></span>
          <span class="kapitel-text"><b><span class="nr">{k.nr}</span>{k.titel}</b>
            <span class="kapitel-stand"><span class="kapitel-marke {k.stand}"><i class="fa-solid {MARKE[k.stand][0]}" aria-hidden="true"></i>{MARKE[k.stand][1]}</span></span></span>
          <i class="fa-solid fa-chevron-right" style="color:var(--fg-mute)" aria-hidden="true"></i>
        </button>
      {/each}
    {/each}
  </div>
</div>

<style>
  .weiter-karte { width: 100%; margin-bottom: var(--sp-3); color: var(--fg); text-align: left; font: inherit; }
  .weiter-karte .text { min-width: 0; display: flex; flex-direction: column; }
  .kapitel { width: 100%; color: var(--fg); text-align: left; font: inherit; }
  .chip { background: transparent; cursor: pointer; }
</style>
