<script lang="ts">
  /*
   * Pfad-Editor als Modal.
   * Pfad = ID, Titel, Beschreibung, Reihenfolge (Liste von Aufgaben-IDs).
   * Reihenfolge: Drag-Sort + add/remove. Auswahl ueber Dropdown
   * der bestehenden Aufgaben-IDs.
   */
  import { adminApi } from '../api/AdminApi';
  import type { PfadEintrag } from '../api/AdminApi';
  import type { VerwaltungsEintrag } from '../types/Admin';

  interface Props {
    offen: boolean;
    bearbeiten: PfadEintrag | null;
    aufgaben: VerwaltungsEintrag[];
    onSchliessen: () => void;
    onGespeichert: () => void;
  }

  let { offen, bearbeiten, aufgaben, onSchliessen, onGespeichert }: Props = $props();

  let id = $state('');
  let titel = $state('');
  let beschreibung = $state('');
  let reihenfolge = $state<string[]>([]);
  let neue_aufgabe = $state('');
  let speichert = $state(false);
  let fehler = $state<string | null>(null);

  let ist_neu = $derived(bearbeiten === null);

  $effect(() => {
    if (offen) {
      if (bearbeiten) {
        id = bearbeiten.id;
        titel = bearbeiten.titel;
        beschreibung = bearbeiten.beschreibung;
        reihenfolge = [...bearbeiten.reihenfolge];
      } else {
        id = '';
        titel = '';
        beschreibung = '';
        reihenfolge = [];
      }
      fehler = null;
    }
  });

  let verfuegbare_aufgaben = $derived(
    aufgaben
      .filter((a) => !reihenfolge.includes(a.id))
      .sort((a, b) => a.id.localeCompare(b.id)),
  );

  function aufgabe_titel(id: string): string {
    return aufgaben.find((a) => a.id === id)?.titel ?? id;
  }

  function aufgabe_hinzufuegen(): void {
    if (neue_aufgabe.trim() && !reihenfolge.includes(neue_aufgabe)) {
      reihenfolge = [...reihenfolge, neue_aufgabe];
      neue_aufgabe = '';
    }
  }

  function aufgabe_entfernen(idx: number): void {
    reihenfolge = reihenfolge.filter((_, i) => i !== idx);
  }

  function nach_oben(idx: number): void {
    if (idx <= 0) return;
    const neu = [...reihenfolge];
    [neu[idx - 1], neu[idx]] = [neu[idx], neu[idx - 1]];
    reihenfolge = neu;
  }

  function nach_unten(idx: number): void {
    if (idx >= reihenfolge.length - 1) return;
    const neu = [...reihenfolge];
    [neu[idx + 1], neu[idx]] = [neu[idx], neu[idx + 1]];
    reihenfolge = neu;
  }

  async function speichern(): Promise<void> {
    speichert = true;
    fehler = null;
    try {
      const daten = { id, titel, beschreibung, reihenfolge };
      if (ist_neu) {
        await adminApi.pfadAnlegen(daten);
      } else {
        await adminApi.pfadAendern(bearbeiten!.id, daten);
      }
      onGespeichert();
    } catch (e) {
      const err = e as { body?: { detail?: string }; message: string };
      fehler = err.body?.detail ?? err.message;
    } finally {
      speichert = false;
    }
  }

  function tastenanschlag(e: KeyboardEvent): void {
    if (!offen) return;
    if (e.key === 'Escape' && !speichert) {
      e.preventDefault();
      onSchliessen();
    }
  }
</script>

<svelte:window on:keydown={tastenanschlag} />

{#if offen}
  <div class="overlay" onclick={onSchliessen} role="presentation">
    <div class="dialog" onclick={(e) => e.stopPropagation()} role="dialog" aria-modal="true">
      <header class="dlg-kopf">
        <h2>{ist_neu ? 'Neuer Pfad' : `Bearbeiten: ${bearbeiten?.id}`}</h2>
        <button class="schliessen" onclick={onSchliessen} aria-label="Schließen" disabled={speichert}>
          <i class="fa-solid fa-xmark" aria-hidden="true"></i>
        </button>
      </header>

      {#if fehler}
        <div class="fehler-box">
          <i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i>
          <pre>{fehler}</pre>
        </div>
      {/if}

      <div class="body">
        <fieldset>
          <legend>Pfad-Daten</legend>
          <div class="grid">
            <label>
              <span>ID <small>(kleinbuchstaben + underscore)</small></span>
              <input type="text" bind:value={id} placeholder="python_einsteiger" disabled={!ist_neu} />
            </label>
            <label class="weit">
              <span>Titel</span>
              <input type="text" bind:value={titel} placeholder="Sprechender Pfad-Titel" />
            </label>
            <label class="ganzzeile">
              <span>Beschreibung</span>
              <textarea rows="4" bind:value={beschreibung} placeholder="Worum geht es in diesem Pfad?"></textarea>
            </label>
          </div>
        </fieldset>

        <fieldset>
          <legend>Reihenfolge ({reihenfolge.length} Aufgaben)</legend>
          {#if reihenfolge.length === 0}
            <p class="leer">Noch keine Aufgaben im Pfad.</p>
          {:else}
            <ol class="reihen-liste">
              {#each reihenfolge as aid, idx (aid)}
                <li>
                  <span class="r-pos num">{idx + 1}.</span>
                  <span class="r-id">{aid}</span>
                  <span class="r-titel">{aufgabe_titel(aid)}</span>
                  <span class="r-actions">
                    <button type="button" class="mini" onclick={() => nach_oben(idx)} disabled={idx === 0} aria-label="Nach oben">
                      <i class="fa-solid fa-arrow-up" aria-hidden="true"></i>
                    </button>
                    <button type="button" class="mini" onclick={() => nach_unten(idx)} disabled={idx === reihenfolge.length - 1} aria-label="Nach unten">
                      <i class="fa-solid fa-arrow-down" aria-hidden="true"></i>
                    </button>
                    <button type="button" class="mini danger" onclick={() => aufgabe_entfernen(idx)} aria-label="Entfernen">
                      <i class="fa-solid fa-xmark" aria-hidden="true"></i>
                    </button>
                  </span>
                </li>
              {/each}
            </ol>
          {/if}

          <div class="hinzufuegen">
            <select bind:value={neue_aufgabe}>
              <option value="">-- Aufgabe wählen --</option>
              {#each verfuegbare_aufgaben as a (a.id)}
                <option value={a.id}>{a.id} -- {a.titel}</option>
              {/each}
            </select>
            <button type="button" class="add" onclick={aufgabe_hinzufuegen} disabled={!neue_aufgabe}>
              <i class="fa-solid fa-plus" aria-hidden="true"></i> Anhängen
            </button>
          </div>
        </fieldset>
      </div>

      <footer class="dlg-fuss">
        <button class="abbrechen" onclick={onSchliessen} disabled={speichert}>Abbrechen</button>
        <button class="primaer" onclick={speichern} disabled={speichert || !id || !titel}>
          {#if speichert}
            <i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i> speichert ...
          {:else}
            <i class="fa-solid fa-floppy-disk" aria-hidden="true"></i>
            {ist_neu ? 'Anlegen' : 'Speichern'}
          {/if}
        </button>
      </footer>
    </div>
  </div>
{/if}

<style>
  .overlay {
    position: fixed; inset: 0;
    background: rgba(0, 0, 0, 0.6);
    display: flex; align-items: center; justify-content: center;
    z-index: 1000; backdrop-filter: blur(2px);
    padding: var(--sp-3);
  }
  .dialog {
    background: var(--bg-card);
    border: 1px solid var(--border);
    width: 100%; max-width: 720px;
    max-height: 92vh;
    display: flex; flex-direction: column;
    box-shadow: var(--shadow-lg);
  }
  .dlg-kopf {
    display: flex; align-items: center; justify-content: space-between;
    padding: var(--sp-3) var(--sp-4);
    border-bottom: 1px solid var(--border);
    background: var(--bg-card-2);
    flex-shrink: 0;
  }
  .dlg-kopf h2 { margin: 0; font-size: var(--fs-md); font-weight: 600; }
  .schliessen {
    background: transparent; border: 1px solid var(--border);
    color: var(--fg-dim); width: 32px; height: 32px;
    border-radius: var(--radius-sm); cursor: pointer;
  }
  .schliessen:hover { color: var(--red); border-color: var(--red); }
  .body {
    overflow-y: auto;
    padding: var(--sp-3) var(--sp-4);
    display: flex; flex-direction: column;
    gap: var(--sp-3); flex: 1;
  }
  .dlg-fuss {
    display: flex; justify-content: flex-end; gap: var(--sp-2);
    padding: var(--sp-3) var(--sp-4);
    border-top: 1px solid var(--border);
    background: var(--bg-card-2);
    flex-shrink: 0;
  }
  fieldset {
    margin: 0;
    padding: var(--sp-3);
    border: 1px solid var(--border);
    background: var(--bg);
    border-radius: var(--radius-sm);
  }
  legend {
    padding: 0 var(--sp-2);
    font-size: var(--fs-xs);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--accent);
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: var(--sp-2);
  }
  .grid label.weit { grid-column: span 2; }
  .grid label.ganzzeile { grid-column: 1/-1; }
  label { display: flex; flex-direction: column; gap: 4px; }
  label span {
    font-size: var(--fs-xs);
    color: var(--fg-dim);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  label small {
    text-transform: none; letter-spacing: 0;
    color: var(--fg-mute);
  }
  input, select, textarea {
    background: var(--bg-card);
    border: 1px solid var(--border);
    color: var(--fg);
    padding: 6px 8px;
    font-family: var(--sans);
    font-size: var(--fs-sm);
    border-radius: var(--radius-sm);
    width: 100%;
    box-sizing: border-box;
  }
  input:disabled { opacity: 0.6; }
  textarea { font-family: var(--quick); resize: vertical; }
  .leer { color: var(--fg-mute); margin: 0; font-family: var(--quick); }

  .reihen-liste {
    list-style: none;
    padding: 0;
    margin: 0 0 var(--sp-2);
    display: flex; flex-direction: column;
    gap: 4px;
  }
  .reihen-liste li {
    display: grid;
    grid-template-columns: 32px 160px 1fr auto;
    gap: var(--sp-2);
    align-items: center;
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: 4px var(--sp-2);
    font-size: var(--fs-xs);
  }
  .r-pos { color: var(--fg-mute); text-align: right; }
  .r-id { font-family: var(--mono); color: var(--accent); }
  .r-titel { color: var(--fg); }
  .r-actions { display: flex; gap: 4px; }
  .mini {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--fg-dim);
    width: 28px; height: 28px;
    border-radius: var(--radius-sm);
    cursor: pointer;
    font-size: var(--fs-xs);
  }
  .mini:hover:not(:disabled) {
    color: var(--accent);
    border-color: var(--accent);
  }
  .mini.danger:hover { color: var(--red); border-color: var(--red); }
  .mini:disabled { opacity: 0.4; cursor: not-allowed; }

  .hinzufuegen {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: var(--sp-2);
    margin-top: var(--sp-2);
  }
  .add {
    background: transparent;
    border: 1px dashed var(--accent);
    color: var(--accent);
    padding: 4px 12px;
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: var(--radius-sm);
    cursor: pointer;
  }
  .add:hover:not(:disabled) {
    background: color-mix(in srgb, var(--accent) 14%, transparent);
  }
  .add:disabled { opacity: 0.5; cursor: not-allowed; }

  .primaer, .abbrechen {
    cursor: pointer;
    font-family: inherit;
    border-radius: var(--radius-sm);
    padding: 8px 16px;
    font-size: var(--fs-sm);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-weight: 600;
  }
  .primaer {
    background: color-mix(in srgb, var(--accent) 14%, transparent);
    border: 1px solid var(--accent);
    color: var(--accent);
    display: inline-flex; align-items: center; gap: 6px;
  }
  .primaer:hover:not(:disabled) {
    background: color-mix(in srgb, var(--accent) 22%, transparent);
  }
  .primaer:disabled { opacity: 0.5; cursor: not-allowed; }
  .abbrechen {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--fg-dim);
    font-weight: 500;
  }
  .abbrechen:hover:not(:disabled) {
    color: var(--fg);
    border-color: var(--fg);
  }

  .fehler-box {
    margin: var(--sp-3) var(--sp-4) 0;
    background: color-mix(in srgb, var(--red) 12%, transparent);
    border: 1px solid var(--red);
    color: var(--fg);
    padding: var(--sp-2) var(--sp-3);
    border-radius: var(--radius-sm);
    display: flex; gap: var(--sp-2);
    align-items: flex-start;
  }
  .fehler-box i { color: var(--red); margin-top: 4px; }
  .fehler-box pre {
    margin: 0;
    font-family: var(--mono);
    font-size: var(--fs-xs);
    white-space: pre-wrap;
    flex: 1;
  }
</style>
