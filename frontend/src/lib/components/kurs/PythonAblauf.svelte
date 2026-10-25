<script lang="ts">
  /*
   * Lauf eines Python-Beispiels: die Ausgabe bis zum aktuellen Schritt, der Abspieler und das Speicherbild nach
   * jeder Zeile. Die aktuelle Zeile meldet die Komponente nach außen, damit Code und Editor sie markieren.
   */
  import { onDestroy } from 'svelte';
  import type { Aufzeichnung } from '../../api/KursApi';
  import Speicherbild from './Speicherbild.svelte';

  interface Props {
    lauf: Aufzeichnung;
    /** Ablauf Schritt für Schritt anbieten */
    ablauf: boolean;
    /** gerade gezeigte Zeile im Code */
    zeile?: number | null;
  }
  let { lauf, ablauf, zeile = $bindable(null) }: Props = $props();

  let schritt = $state(0);
  let takt = $state<ReturnType<typeof setInterval> | null>(null);

  let schritte = $derived(lauf.schritte);
  let aktuell = $derived(schritt > 0 ? schritte[schritt - 1] : null);
  /** Speicherbild nur, wenn der Lauf überhaupt Namen anlegt */
  let mitSpeicher = $derived(schritte.some((s) => s.rahmen.some((r) => Object.keys(r.variablen).length > 0)));
  let ausgabeBisher = $derived(schritte.slice(0, schritt).map((s) => s.ausgabe).join(''));

  // neuer Lauf: ans Ende springen, dann ist die ganze Ausgabe zu sehen
  $effect(() => {
    schritt = lauf.schritte.length;
  });
  $effect(() => {
    zeile = aktuell?.zeile ?? null;
  });

  function anhalten() {
    if (takt) clearInterval(takt);
    takt = null;
  }

  function abspielen() {
    if (takt) return anhalten();
    if (schritt >= schritte.length) schritt = 0;
    takt = setInterval(() => {
      if (schritt >= schritte.length) return anhalten();
      schritt += 1;
    }, 1000);
  }

  onDestroy(anhalten);
</script>

<pre class="ausgabe">{#if ausgabeBisher}{ausgabeBisher}{:else}<span class="leer">Noch keine Ausgabe</span>{/if}</pre>
{#if lauf.fehler && schritt === schritte.length}
  <div class="erklaerung schlecht"><i class="fa-solid fa-bug" aria-hidden="true"></i><span>{lauf.fehler}{lauf.fehlerzeile ? ` (Zeile ${lauf.fehlerzeile})` : ''}</span></div>
{/if}
{#if ablauf && schritte.length}
  <div class="block-kopf"><span>Ablauf Schritt für Schritt</span><span class="dim">aus dem echten Lauf</span></div>
  <div class="abspieler">
    <button class="ikon" onclick={() => { anhalten(); schritt = Math.max(0, schritt - 1); }} aria-label="Schritt zurück"><i class="fa-solid fa-backward-step" aria-hidden="true"></i></button>
    <button class="ikon" onclick={abspielen} aria-label={takt ? 'Anhalten' : 'Abspielen'}><i class="fa-solid {takt ? 'fa-pause' : 'fa-play'}" aria-hidden="true"></i></button>
    <button class="ikon" onclick={() => { anhalten(); schritt = Math.min(schritte.length, schritt + 1); }} aria-label="Schritt vor"><i class="fa-solid fa-forward-step" aria-hidden="true"></i></button>
    <input class="regler" type="range" min="0" max={schritte.length} bind:value={schritt} oninput={anhalten} aria-label="Schritt" />
    <span class="num">{schritt} / {schritte.length}</span>
  </div>
  {#if lauf.gekuerzt}<span class="dim" style="font-size:var(--fs-xs)">Aufzeichnung nach {schritte.length} Schritten gekürzt; der Code lief trotzdem zu Ende.</span>{/if}
  {#if mitSpeicher}<Speicherbild schritt={aktuell} vorher={schritt > 1 ? schritte[schritt - 2] : null} />{/if}
{/if}
