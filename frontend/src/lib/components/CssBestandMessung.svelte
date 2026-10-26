<script lang="ts">
  /*
   * Verwaltung: den CSS-Bestand im Browser messen (css/bestand.ts). Rendern kann nur der Browser, darum läuft die
   * Prüfung hier auf Knopfdruck statt beim Einlesen; das Ergebnis steht wie die Befunde der Bestandsprüfung da.
   */
  import { adminApi, type Befund } from '../api/AdminApi';
  import { messeBestand } from '../css/bestand';

  let gesamt = $state(0);
  let fertig = $state(0);
  let laeuft = $state(false);
  let befunde = $state<Befund[] | null>(null);
  let fehler = $state<string | null>(null);
  let offen = $state(false);

  async function messen(): Promise<void> {
    laeuft = true;
    fehler = null;
    befunde = null;
    fertig = 0;
    try {
      const bestand = await adminApi.cssBestand();
      gesamt = bestand.aufgaben.length;
      befunde = await messeBestand(bestand, (n) => (fertig = n));
      offen = befunde.length > 0;
    } catch (e) {
      fehler = e instanceof Error ? e.message : String(e);
    } finally {
      laeuft = false;
    }
  }
</script>

<div class="hinweis-box messung" class:fehler={!!befunde?.length || !!fehler} class:gut={befunde?.length === 0}>
  <i class="fa-solid fa-ruler-combined" aria-hidden="true"></i>
  <span>
    {#if laeuft}CSS-Bestand: {fertig} von {gesamt || '...'} gemessen
    {:else if fehler}CSS-Bestand: {fehler}
    {:else if befunde}CSS-Bestand: {gesamt} Nachbauten gemessen, {befunde.length} {befunde.length === 1 ? 'Befund' : 'Befunde'}
    {:else}CSS-Bestand: Musterlösungen decken voll, Startcode besteht nicht?{/if}
  </span>
  {#if befunde?.length}
    <button class="knopf-klein" onclick={() => (offen = !offen)}><i class="fa-solid {offen ? 'fa-chevron-up' : 'fa-chevron-down'}" aria-hidden="true"></i>Befunde</button>
  {/if}
  <button class="knopf-klein rechts" onclick={messen} disabled={laeuft}><i class="fa-solid {laeuft ? 'fa-spinner fa-spin' : 'fa-play'}" aria-hidden="true"></i>Messen</button>
</div>
{#if offen && befunde?.length}
  <ul class="befunde">
    {#each befunde as b, i (i)}<li><code>{b.ort}</code> {b.meldung}</li>{/each}
  </ul>
{/if}

<style>
  .messung { display: flex; align-items: center; gap: var(--sp-2); border-radius: 0; }
  .messung.gut { border-color: var(--green); color: var(--green); background: color-mix(in srgb, var(--green) 8%, transparent); }
  .rechts { margin-left: auto; }
  .befunde { margin: 0; padding: var(--sp-2) var(--sp-3) var(--sp-2) var(--sp-5); max-height: 160px; overflow-y: auto; font-size: var(--fs-sm); border: 1px solid var(--border); }
</style>
