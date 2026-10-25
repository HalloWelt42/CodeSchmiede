<script lang="ts">
  /*
   * Lauf einer SQL-Abfrage: das Ergebnis und, Klausel für Klausel in der Reihenfolge der Abarbeitung, die
   * Zwischentabelle. Zeilen, die ein Filter behält oder aussortiert, Spalten, die SELECT fallen lässt, und Gruppen
   * nach GROUP BY sind markiert. Die Zeile der gewählten Klausel meldet die Komponente nach außen.
   */
  import type { SqlLauf, Zwischentabelle } from '../../api/KursApi';

  interface Props {
    lauf: SqlLauf;
    /** Zwischentabellen anbieten */
    ablauf: boolean;
    /** Zeile der gewählten Klausel im Code */
    zeile?: number | null;
  }
  let { lauf, ablauf, zeile = $bindable(null) }: Props = $props();

  let schritt = $state(0);
  let schritte = $derived(ablauf ? lauf.schritte : []);
  let aktuell = $derived(schritte[schritt] ?? null);

  // neuer Lauf: beim ersten Schritt beginnen, wie die Datenbank
  $effect(() => {
    void lauf;
    schritt = 0;
  });
  $effect(() => {
    zeile = aktuell?.zeile ?? null;
  });

  function wert(w: unknown): string {
    if (w === null) return 'NULL';
    return String(w);
  }

  function zeilenKlasse(t: Zwischentabelle, i: number): string {
    const gruppe = t.gruppe[i];
    return [t.zustand[i] ?? '', gruppe ? (gruppe % 2 ? 'gruppe-a' : 'gruppe-b') : ''].join(' ').trim();
  }

  const anzahl = (n: number, eins: string, viele: string) => `${n} ${n === 1 ? eins : viele}`;
</script>

{#snippet tabelle(t: Zwischentabelle)}
  <div class="tabellen-rollfeld">
    <table class="daten kurs-daten">
      <thead><tr>{#each t.spalten as s, i (i)}<th class:weg={t.weg[i]}>{s}</th>{/each}</tr></thead>
      <tbody>
        {#each t.zeilen as z, i (i)}
          <tr class={zeilenKlasse(t, i)}>{#each z as w, j (j)}<td class:weg={t.weg[j]} class:null={w === null}>{wert(w)}</td>{/each}</tr>
        {/each}
      </tbody>
    </table>
  </div>
{/snippet}

{#if lauf.fehler}
  <div class="erklaerung schlecht"><i class="fa-solid fa-bug" aria-hidden="true"></i><span>{lauf.fehler}</span></div>
{:else}
  <div class="block-kopf"><span>Ergebnis</span><span class="dim">{anzahl(lauf.zeilen.length, 'Zeile', 'Zeilen')}, {anzahl(lauf.spalten.length, 'Spalte', 'Spalten')}</span></div>
  {#if lauf.zeilen.length}
    {@render tabelle({ spalten: lauf.spalten, zeilen: lauf.zeilen, zustand: [], weg: [], gruppe: [] })}
  {:else}
    <pre class="ausgabe"><span class="leer">Keine Zeile passt</span></pre>
  {/if}

  {#if aktuell}
    <div class="block-kopf"><span>So arbeitet die Datenbank</span><span class="dim">Zwischentabelle je Schritt</span></div>
    <div class="klausel-leiste">
      {#each schritte as s, i (i)}
        <button class="klausel" class:jetzt={i === schritt} class:erledigt={i < schritt} onclick={() => (schritt = i)}>
          <small>{i + 1}</small>{s.klausel}{#if s.zeile}<small>Zeile {s.zeile}</small>{/if}
        </button>
      {/each}
    </div>
    <p class="klausel-text">{aktuell.text}</p>
    {@render tabelle(aktuell.tabelle)}
    <div class="werkbank-zeile">
      <button class="knopf" disabled={schritt === 0} onclick={() => (schritt -= 1)}><i class="fa-solid fa-backward-step" aria-hidden="true"></i>Zurück</button>
      <button class="knopf" disabled={schritt >= schritte.length - 1} onclick={() => (schritt += 1)}>Weiter<i class="fa-solid fa-forward-step" aria-hidden="true"></i></button>
    </div>
  {/if}
{/if}

<style>
  .tabellen-rollfeld { overflow-x: auto; max-width: 100%; }
  .kurs-daten { font-size: 15px; }
  .kurs-daten td.null { color: var(--fg-mute); font-style: italic; }
  .kurs-daten tr.gruppe-b td { background: color-mix(in srgb, var(--accent) 9%, transparent); }
  .klausel-text { margin: 0; font-size: var(--fs-md); color: var(--fg-dim); min-height: 2.6em; }
</style>
