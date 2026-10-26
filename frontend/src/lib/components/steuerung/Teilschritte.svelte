<script lang="ts">
  /*
   * Teilschritte eines Steuerungsspiels mit Umschalter "Schritt für Schritt" | "Alles auf einmal".
   *
   * Schritt für Schritt zeigt die Ziele bis zum ersten offenen, dieses als aktuelles mit seinen Befunden; danach
   * nichts. Alles auf einmal zeigt jedes Ziel mit Haken oder Kreuz. Ohne Lauf sind alle Ziele noch offen.
   * Den Stand liefert jede Auswertung neu (geprüft wird immer alles); gespeichert wird nur die Wahl der Ansicht.
   */
  import type { TeilschrittStand } from '../../types/Steuerung';

  type Modus = 'schritte' | 'alle';
  const SCHLUESSEL = 'codeschmiede.steuerung.modus';

  interface Props {
    vorgaben: { titel: string; text: string }[];
    staende: TeilschrittStand[] | null;
  }
  let { vorgaben, staende }: Props = $props();

  function gemerkt(): Modus {
    try {
      return localStorage.getItem(SCHLUESSEL) === 'alle' ? 'alle' : 'schritte';
    } catch {
      return 'schritte';
    }
  }
  let modus = $state<Modus>(gemerkt());

  function waehle(neu: Modus): void {
    modus = neu;
    try {
      localStorage.setItem(SCHLUESSEL, neu);
    } catch {
      // nur für diese Sitzung
    }
  }

  let zeilen = $derived(
    vorgaben.map((v, i) => ({ ...v, stand: staende?.[i] ?? null, nr: i + 1 })),
  );
  // erstes Ziel, das noch nicht erfüllt ist (oder nur beim Prüfen geprüft wird)
  let aktuell = $derived(zeilen.findIndex((z) => !z.stand || !z.stand.erfuellt || !z.stand.geprueft));
  let sichtbar = $derived(modus === 'alle' || aktuell < 0 ? zeilen : zeilen.slice(0, aktuell + 1));
</script>

<div class="modus" role="group" aria-label="Ansicht der Teilschritte">
  <button class:aktiv={modus === 'schritte'} onclick={() => waehle('schritte')}>Schritt für Schritt</button>
  <button class:aktiv={modus === 'alle'} onclick={() => waehle('alle')}>Alles auf einmal</button>
</div>
<div class="teilschritte">
  {#each sichtbar as z, i (z.nr)}
    {@const erledigt = !!z.stand?.erfuellt && z.stand.geprueft}
    {@const ist_aktuell = modus === 'schritte' && i === aktuell}
    {@const offen = modus === 'alle' && !!z.stand && !z.stand.erfuellt}
    <div class="teilschritt" class:erledigt class:aktuell={ist_aktuell} class:offen>
      <i
        class="fa-solid {erledigt ? 'fa-circle-check' : ist_aktuell ? 'fa-crosshairs' : offen ? 'fa-circle-xmark' : 'fa-circle'}"
        aria-hidden="true"
      ></i>
      <div>
        <b>{z.nr}. {z.titel}</b>
        <small>{z.text}</small>
        {#if z.stand && !z.stand.erfuellt && (ist_aktuell || modus === 'alle') && z.stand.befunde.length}
          <div class="stand">
            {#each z.stand.befunde as b (b)}<div><i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i> {b}</div>{/each}
          </div>
        {:else if z.stand?.erfuellt && !z.stand.geprueft && (ist_aktuell || modus === 'alle')}
          <div class="stand dim">Im sichtbaren Ablauf erfüllt; die versteckten Abläufe kommen beim Prüfen.</div>
        {/if}
      </div>
    </div>
  {/each}
  {#if modus === 'schritte' && aktuell >= 0 && aktuell < zeilen.length - 1}
    <p class="dim weiter">Noch {zeilen.length - aktuell - 1} {zeilen.length - aktuell - 1 === 1 ? 'Schritt' : 'Schritte'} danach.</p>
  {/if}
</div>

<style>
  .weiter {
    margin: 0;
    font-size: var(--fs-sm);
  }
  .stand.dim { color: var(--fg-dim); }
</style>
