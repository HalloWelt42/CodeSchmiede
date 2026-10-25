<script lang="ts">
  /*
   * Code ohne Editor im Farbschema des Editors, Zeile für Zeile: hervorgehobene Zeile beim Abspielen, anklickbare
   * Zeilen bei der Frage nach der Fehlerstelle, Lücken als Eingabefelder.
   */
  import { zeilen } from '../../kurs/hervorheben';

  interface Props {
    code: string;
    sprache: string;
    /** Zeile (ab 1), die gerade läuft */
    jetzt?: number | null;
    /** Klassen je Zeile (ab 1), etwa gewaehlt oder richtig */
    klassen?: Record<number, string>;
    /** Zeilen anklickbar (Fehlerstelle) */
    beiZeile?: (zeile: number) => void;
    /** Lücken ___ als Eingabefelder; die Werte liegen in `luecken` */
    luecken?: string[];
  }
  let { code, sprache, jetzt = null, klassen = {}, beiZeile, luecken = $bindable() }: Props = $props();

  const LUECKE = '___';
  let mitLuecken = $derived(luecken !== undefined);
  // Mit Lücken wird der Code als Text gezeigt: die Lücke zerreißt sonst die Hervorhebung
  let html = $derived(mitLuecken ? [] : zeilen(code, sprache));
  let roheZeilen = $derived(code.replace(/\n$/, '').split('\n'));

  function lueckenVor(zeile: number): number {
    return roheZeilen.slice(0, zeile).reduce((n, z) => n + z.split(LUECKE).length - 1, 0);
  }
</script>

<div class="code" class:klickbar={!!beiZeile}>
  {#each roheZeilen as roh, i (i)}
    {@const nr = i + 1}
    {#if beiZeile}
      <button type="button" class="zeile fehlerzeile {klassen[nr] ?? ''}" class:jetzt={jetzt === nr} onclick={() => beiZeile?.(nr)}>
        <span class="ln">{nr}</span><span>{@html html[i] ?? ''}</span>
      </button>
    {:else}
      <div class="{klassen[nr] ?? ''}" class:jetzt={jetzt === nr}>
        <span class="ln">{nr}</span>
        {#if mitLuecken && luecken}
          <span>{#each roh.split(LUECKE) as stueck, j (j)}{stueck}{#if j < roh.split(LUECKE).length - 1}<input class="luecke" spellcheck="false" aria-label="Lücke {lueckenVor(i) + j + 1}" bind:value={luecken[lueckenVor(i) + j]} />{/if}{/each}</span>
        {:else}
          <span>{@html html[i] ?? ''}</span>
        {/if}
      </div>
    {/if}
  {/each}
</div>

<style>
  .zeile {
    display: flex;
    width: 100%;
    min-height: 22px;
    padding: 0;
    border: 0;
    border-radius: 0;
    background: transparent;
    color: inherit;
    font: inherit;
    text-align: left;
  }
  .zeile:hover:not(:disabled) {
    background: var(--ed-zeile);
    color: inherit;
  }
</style>
