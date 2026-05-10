<script lang="ts">
  /*
   * Aufgaben-Editor als Modal. Anlegen oder Bearbeiten einer Aufgabe
   * inkl. Tests, Hints, Tags, Pfade, Quelle, Musterloesungen.
   *
   * Tests + Hints + Quiz-Optionen werden mit add/remove gepflegt.
   * Test-Werte (input + expected) sind JSON-Strings, damit Booleans,
   * Listen und Dicts gehen. Validierung beim Speichern.
   */
  import { onMount } from 'svelte';
  import { adminApi } from '../api/AdminApi';
  import type {
    MusterloesungEintrag,
    ValidierungsErgebnis,
  } from '../api/AdminApi';
  import { konfig } from '../stores/KonfigStore.svelte';
  import type { VerwaltungsEintrag } from '../types/Admin';

  interface Props {
    offen: boolean;
    bearbeiten: VerwaltungsEintrag | null;
    onSchliessen: () => void;
    onGespeichert: (id: string) => void;
  }

  let { offen, bearbeiten, onSchliessen, onGespeichert }: Props = $props();

  // Form-State
  let id = $state('');
  let titel = $state('');
  let sprache = $state('python');
  let task_type = $state('code_schreiben');
  let runner_type = $state('docker_python');
  let schwierigkeit = $state('anfaenger');
  let schwierigkeit_score = $state(10);
  let schaetz_minuten = $state(5);
  let zeitlimit_sekunden = $state(5);
  let funktion = $state('');
  let tags_text = $state('');
  let pfade_text = $state('');
  let voraussetzungen_text = $state('');
  let lizenz = $state('eigen');
  let autor = $state('HalloWelt42');
  let erstellt_am = $state('');
  let quelle_url = $state('');
  let quelle_notiz = $state('');
  let starter_code = $state('');
  let beschreibung_md = $state('');
  let hints = $state<{ kosten: number; text: string }[]>([]);
  let tests_sichtbar_text = $state<{ input: string; expected: string }[]>([]);
  let tests_versteckt_text = $state<{ input: string; expected: string }[]>([]);

  // Quiz-Felder (nur wenn task_type=output_quiz)
  let quiz_code = $state('');
  let quiz_optionen = $state<string[]>([]);
  let quiz_richtig_index = $state(0);

  let speichert = $state(false);
  let fehler = $state<string | null>(null);

  let musterloesungen = $state<MusterloesungEintrag[]>([]);
  let neue_variante = $state('');
  let neuer_solution_code = $state('');
  let validierung = $state<ValidierungsErgebnis | null>(null);
  let validiert_laeuft = $state(false);

  let ist_neu = $derived(bearbeiten === null);
  let titel_modal = $derived(ist_neu ? 'Neue Aufgabe' : `Bearbeiten: ${bearbeiten?.id}`);

  $effect(() => {
    if (offen) {
      void initialisieren();
    }
  });

  async function initialisieren(): Promise<void> {
    fehler = null;
    validierung = null;
    if (bearbeiten) {
      const a = bearbeiten;
      id = a.id;
      titel = a.titel;
      sprache = a.sprache;
      task_type = a.task_type;
      runner_type = a.runner_type;
      schwierigkeit = a.schwierigkeit;
      schwierigkeit_score = a.schwierigkeit_score;
      schaetz_minuten = a.schaetz_minuten;
      zeitlimit_sekunden = a.zeitlimit_sekunden;
      funktion = a.funktion ?? '';
      tags_text = a.tags.join(', ');
      pfade_text = a.pfade.join(', ');
      voraussetzungen_text = a.voraussetzungen.join(', ');
      lizenz = a.lizenz;
      autor = a.autor ?? '';
      erstellt_am = a.erstellt_am ?? '';
      quelle_url = a.quelle?.url ?? '';
      quelle_notiz = a.quelle?.notiz ?? '';
      starter_code = a.starter_code;
      beschreibung_md = a.beschreibung_md;
      hints = a.hints.map((h) => ({ kosten: h.kosten, text: h.text }));
      tests_sichtbar_text = a.tests_sichtbar.map((t) => ({
        input: JSON.stringify(t.input),
        expected: JSON.stringify(t.expected),
      }));
      tests_versteckt_text = a.tests_versteckt.map((t) => ({
        input: JSON.stringify(t.input),
        expected: JSON.stringify(t.expected),
      }));
      // Quiz-Felder aus dem extra-Feld -- gibt es nur fuer output_quiz
      const extra = (a as unknown as { extra?: Record<string, unknown> }).extra ?? {};
      const quiz = extra['quiz'] as { code?: string; optionen?: string[]; richtig_index?: number } | undefined;
      quiz_code = quiz?.code ?? '';
      quiz_optionen = quiz?.optionen ? [...quiz.optionen] : [];
      quiz_richtig_index = quiz?.richtig_index ?? 0;
      await ladeMusterloesungen();
    } else {
      id = '';
      titel = '';
      sprache = 'python';
      task_type = 'code_schreiben';
      runner_type = 'docker_python';
      schwierigkeit = 'anfaenger';
      schwierigkeit_score = 10;
      schaetz_minuten = 5;
      zeitlimit_sekunden = 5;
      funktion = '';
      tags_text = '';
      pfade_text = '';
      voraussetzungen_text = '';
      lizenz = 'eigen';
      autor = 'HalloWelt42';
      erstellt_am = new Date().toISOString().slice(0, 10);
      quelle_url = '';
      quelle_notiz = '';
      starter_code = '';
      beschreibung_md = '';
      hints = [];
      tests_sichtbar_text = [];
      tests_versteckt_text = [];
      quiz_code = '';
      quiz_optionen = [];
      quiz_richtig_index = 0;
      musterloesungen = [];
    }
  }

  async function ladeMusterloesungen(): Promise<void> {
    if (!bearbeiten) return;
    try {
      musterloesungen = await adminApi.musterloesungen(bearbeiten.id);
    } catch (e) {
      fehler = (e as Error).message;
    }
  }

  function liste_aus_text(text: string): string[] {
    return text
      .split(',')
      .map((s) => s.trim())
      .filter((s) => s.length > 0);
  }

  function parse_json_oder_string(text: string): unknown {
    const t = text.trim();
    if (t === '') return null;
    try {
      return JSON.parse(t);
    } catch {
      // Fallback: als String belassen
      return t;
    }
  }

  function frontmatter_zusammenbauen(): Record<string, unknown> {
    const fm: Record<string, unknown> = {
      schema_version: 1,
      id,
      revision: bearbeiten ? bearbeiten.revision : 1,
      titel,
      sprache,
      task_type,
      runner_type,
      schwierigkeit,
      schwierigkeit_score,
      schaetz_minuten,
      tags: liste_aus_text(tags_text),
      pfade: liste_aus_text(pfade_text),
      voraussetzungen: liste_aus_text(voraussetzungen_text),
      quelle: {
        url: quelle_url.trim() || null,
        notiz: quelle_notiz.trim() || null,
      },
      lizenz,
      autor: autor.trim() || null,
      erstellt_am: erstellt_am.trim() || null,
      zeitlimit_sekunden,
      hints: hints.map((h) => ({ kosten: h.kosten, text: h.text })),
    };
    if (task_type === 'output_quiz') {
      fm['quiz'] = {
        code: quiz_code,
        optionen: quiz_optionen,
        richtig_index: quiz_richtig_index,
      };
    } else {
      fm['funktion'] = funktion.trim() || null;
      fm['tests_sichtbar'] = tests_sichtbar_text.map((t) => ({
        input: parse_json_oder_string(t.input),
        expected: parse_json_oder_string(t.expected),
      }));
      fm['tests_versteckt'] = tests_versteckt_text.map((t) => ({
        input: parse_json_oder_string(t.input),
        expected: parse_json_oder_string(t.expected),
      }));
      fm['starter_code'] = starter_code;
    }
    return fm;
  }

  async function speichern(): Promise<void> {
    speichert = true;
    fehler = null;
    try {
      const fm = frontmatter_zusammenbauen();
      if (ist_neu) {
        const erg = await adminApi.aufgabeAnlegen({
          frontmatter: fm,
          beschreibung_md,
        });
        onGespeichert(erg.id);
      } else {
        const erg = await adminApi.aufgabeAendern(bearbeiten!.id, {
          frontmatter: fm,
          beschreibung_md,
        });
        onGespeichert(erg.id);
      }
    } catch (e) {
      const err = e as { body?: { detail?: string }; message: string };
      fehler = err.body?.detail ?? err.message;
    } finally {
      speichert = false;
    }
  }

  async function musterloesung_speichern_neu(): Promise<void> {
    if (!bearbeiten || !neue_variante.trim() || !neuer_solution_code.trim()) return;
    try {
      await adminApi.musterloesungSpeichern(
        bearbeiten.id,
        neue_variante.trim(),
        neuer_solution_code,
      );
      neue_variante = '';
      neuer_solution_code = '';
      await ladeMusterloesungen();
    } catch (e) {
      fehler = (e as Error).message;
    }
  }

  async function musterloesung_loeschen(variante: string): Promise<void> {
    if (!bearbeiten) return;
    try {
      await adminApi.musterloesungLoeschen(bearbeiten.id, variante);
      await ladeMusterloesungen();
    } catch (e) {
      fehler = (e as Error).message;
    }
  }

  async function musterloesung_aktualisieren(variante: string, code: string): Promise<void> {
    if (!bearbeiten) return;
    try {
      await adminApi.musterloesungSpeichern(bearbeiten.id, variante, code);
    } catch (e) {
      fehler = (e as Error).message;
    }
  }

  async function validieren(): Promise<void> {
    if (!bearbeiten) return;
    validiert_laeuft = true;
    validierung = null;
    try {
      validierung = await adminApi.validieren(bearbeiten.id);
    } catch (e) {
      fehler = (e as Error).message;
    } finally {
      validiert_laeuft = false;
    }
  }

  function hint_hinzufuegen(): void {
    hints = [...hints, { kosten: 0, text: '' }];
  }
  function hint_entfernen(idx: number): void {
    hints = hints.filter((_, i) => i !== idx);
  }

  function test_hinzufuegen(versteckt: boolean): void {
    const eintrag = { input: '[]', expected: 'null' };
    if (versteckt) tests_versteckt_text = [...tests_versteckt_text, eintrag];
    else tests_sichtbar_text = [...tests_sichtbar_text, eintrag];
  }
  function test_entfernen(versteckt: boolean, idx: number): void {
    if (versteckt)
      tests_versteckt_text = tests_versteckt_text.filter((_, i) => i !== idx);
    else
      tests_sichtbar_text = tests_sichtbar_text.filter((_, i) => i !== idx);
  }

  function quiz_option_hinzufuegen(): void {
    quiz_optionen = [...quiz_optionen, ''];
  }
  function quiz_option_entfernen(idx: number): void {
    quiz_optionen = quiz_optionen.filter((_, i) => i !== idx);
    if (quiz_richtig_index >= quiz_optionen.length) {
      quiz_richtig_index = Math.max(0, quiz_optionen.length - 1);
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
        <h2>{titel_modal}</h2>
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
          <legend>Grunddaten</legend>
          <div class="grid">
            <label>
              <span>ID <small>(nnn-slug)</small></span>
              <input type="text" bind:value={id} placeholder="070-mein-wurf" disabled={!ist_neu} />
            </label>
            <label class="weit">
              <span>Titel</span>
              <input type="text" bind:value={titel} placeholder="Sprechender Titel" />
            </label>
            <label>
              <span>Sprache</span>
              <select bind:value={sprache}>
                {#each konfig.daten.sprachen as s (s.id)}
                  <option value={s.id}>{s.titel}</option>
                {/each}
              </select>
            </label>
            <label>
              <span>Aufgabentyp</span>
              <select bind:value={task_type}>
                {#each konfig.daten.aufgabentypen as t (t.id)}
                  <option value={t.id}>{t.titel}</option>
                {/each}
              </select>
            </label>
            <label>
              <span>Schwierigkeit</span>
              <select bind:value={schwierigkeit}>
                {#each konfig.daten.schwierigkeiten as s (s.id)}
                  <option value={s.id}>{s.titel}</option>
                {/each}
              </select>
            </label>
            <label>
              <span>Score (1-100)</span>
              <input type="number" min="1" max="100" bind:value={schwierigkeit_score} />
            </label>
            <label>
              <span>Geschätzte Min.</span>
              <input type="number" min="1" bind:value={schaetz_minuten} />
            </label>
            <label>
              <span>Timeout (Sek.)</span>
              <input type="number" min="1" max="60" bind:value={zeitlimit_sekunden} />
            </label>
            {#if task_type !== 'output_quiz'}
              <label class="weit">
                <span>Funktionsname</span>
                <input type="text" bind:value={funktion} placeholder="meine_funktion" />
              </label>
            {/if}
            <label class="weit">
              <span>Tags <small>(Komma-getrennt)</small></span>
              <input type="text" bind:value={tags_text} placeholder="schleifen, listen" />
            </label>
            <label class="weit">
              <span>Pfade <small>(Komma-getrennt, IDs)</small></span>
              <input type="text" bind:value={pfade_text} placeholder="python_grundlagen" />
            </label>
            <label class="weit">
              <span>Voraussetzungen <small>(Aufgaben-IDs)</small></span>
              <input type="text" bind:value={voraussetzungen_text} placeholder="001-fizzbuzz" />
            </label>
          </div>
        </fieldset>

        <fieldset>
          <legend>Quelle &amp; Lizenz</legend>
          <div class="grid">
            <label class="weit">
              <span>Quelle URL</span>
              <input type="url" bind:value={quelle_url} />
            </label>
            <label class="weit">
              <span>Quelle Notiz</span>
              <input type="text" bind:value={quelle_notiz} />
            </label>
            <label>
              <span>Lizenz</span>
              <input type="text" bind:value={lizenz} />
            </label>
            <label>
              <span>Autor</span>
              <input type="text" bind:value={autor} />
            </label>
            <label>
              <span>Erstellt am</span>
              <input type="date" bind:value={erstellt_am} />
            </label>
          </div>
        </fieldset>

        <fieldset>
          <legend>Beschreibung (Markdown)</legend>
          <textarea rows="10" bind:value={beschreibung_md} placeholder="# Titel...&#10;&#10;Aufgabentext..."></textarea>
        </fieldset>

        {#if task_type === 'output_quiz'}
          <fieldset>
            <legend>Quiz-Inhalt</legend>
            <label>
              <span>Code-Snippet</span>
              <textarea rows="6" bind:value={quiz_code}></textarea>
            </label>
            <div class="opt-liste">
              <span class="opt-label">Optionen <small>(eine pro Zeile reicht aus)</small></span>
              {#each quiz_optionen as _, idx (idx)}
                <div class="opt-zeile">
                  <input type="radio" name="richtig" value={idx} bind:group={quiz_richtig_index} aria-label="richtig" />
                  <input type="text" bind:value={quiz_optionen[idx]} placeholder="Antwort-Option" />
                  <button type="button" class="entf" onclick={() => quiz_option_entfernen(idx)} aria-label="Entfernen">
                    <i class="fa-solid fa-xmark" aria-hidden="true"></i>
                  </button>
                </div>
              {/each}
              <button type="button" class="add" onclick={quiz_option_hinzufuegen}>
                <i class="fa-solid fa-plus" aria-hidden="true"></i> Option hinzufügen
              </button>
            </div>
          </fieldset>
        {:else}
          <fieldset>
            <legend>Starter-Code</legend>
            <textarea rows="6" class="mono" bind:value={starter_code} placeholder="def meine_funktion(...):&#10;    pass"></textarea>
          </fieldset>

          <fieldset>
            <legend>Sichtbare Tests</legend>
            <p class="lead">Werte als JSON: <code>[1, 2]</code>, <code>true</code>, <code>"hallo"</code>, <code>null</code></p>
            {#each tests_sichtbar_text as _, idx (idx)}
              <div class="test-zeile">
                <input type="text" bind:value={tests_sichtbar_text[idx].input} placeholder="[3, 4]" class="mono" />
                <span class="zeichen">→</span>
                <input type="text" bind:value={tests_sichtbar_text[idx].expected} placeholder="7" class="mono" />
                <button type="button" class="entf" onclick={() => test_entfernen(false, idx)} aria-label="Entfernen">
                  <i class="fa-solid fa-xmark" aria-hidden="true"></i>
                </button>
              </div>
            {/each}
            <button type="button" class="add" onclick={() => test_hinzufuegen(false)}>
              <i class="fa-solid fa-plus" aria-hidden="true"></i> Test hinzufügen
            </button>
          </fieldset>

          <fieldset>
            <legend>Versteckte Tests</legend>
            <p class="lead">Anti-Hardcoding -- nur in dieser Verwaltung sichtbar.</p>
            {#each tests_versteckt_text as _, idx (idx)}
              <div class="test-zeile">
                <input type="text" bind:value={tests_versteckt_text[idx].input} placeholder="[100]" class="mono" />
                <span class="zeichen">→</span>
                <input type="text" bind:value={tests_versteckt_text[idx].expected} placeholder="200" class="mono" />
                <button type="button" class="entf" onclick={() => test_entfernen(true, idx)} aria-label="Entfernen">
                  <i class="fa-solid fa-xmark" aria-hidden="true"></i>
                </button>
              </div>
            {/each}
            <button type="button" class="add" onclick={() => test_hinzufuegen(true)}>
              <i class="fa-solid fa-plus" aria-hidden="true"></i> Test hinzufügen
            </button>
          </fieldset>
        {/if}

        <fieldset>
          <legend>Hints (Tipps)</legend>
          {#each hints as _, idx (idx)}
            <div class="hint-zeile">
              <label class="hint-kosten">
                <span>Kosten</span>
                <input type="number" min="0" bind:value={hints[idx].kosten} />
              </label>
              <label class="hint-text weit">
                <span>Text</span>
                <textarea rows="2" bind:value={hints[idx].text}></textarea>
              </label>
              <button type="button" class="entf" onclick={() => hint_entfernen(idx)} aria-label="Entfernen">
                <i class="fa-solid fa-xmark" aria-hidden="true"></i>
              </button>
            </div>
          {/each}
          <button type="button" class="add" onclick={hint_hinzufuegen}>
            <i class="fa-solid fa-plus" aria-hidden="true"></i> Hint hinzufügen
          </button>
        </fieldset>

        {#if !ist_neu}
          <fieldset>
            <legend>Musterlösungen</legend>
            {#each musterloesungen as ml (ml.variante)}
              <details class="muster-eintrag">
                <summary>
                  <span class="m-titel">{ml.variante}</span>
                  <button type="button" class="entf" onclick={(e) => { e.preventDefault(); musterloesung_loeschen(ml.variante); }} aria-label="Löschen">
                    <i class="fa-solid fa-trash" aria-hidden="true"></i>
                  </button>
                </summary>
                <textarea
                  rows="8"
                  class="mono"
                  bind:value={ml.code}
                  onblur={() => musterloesung_aktualisieren(ml.variante, ml.code)}
                ></textarea>
                <small class="hint">Speichert beim Verlassen des Feldes.</small>
              </details>
            {/each}

            <div class="neu-loesung">
              <span class="neu-label">Neue Variante</span>
              <input type="text" bind:value={neue_variante} placeholder="z.B. naive, idiomatic, optimal" />
              <textarea rows="4" class="mono" bind:value={neuer_solution_code} placeholder="def funktion(...):&#10;    return ..."></textarea>
              <button type="button" class="add" onclick={musterloesung_speichern_neu} disabled={!neue_variante.trim() || !neuer_solution_code.trim()}>
                <i class="fa-solid fa-plus" aria-hidden="true"></i> Hinzufügen
              </button>
            </div>

            <div class="validieren-zeile">
              <button type="button" class="action sek" onclick={validieren} disabled={validiert_laeuft || musterloesungen.length === 0}>
                {#if validiert_laeuft}
                  <i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i> validiere ...
                {:else}
                  <i class="fa-solid fa-flask" aria-hidden="true"></i> Musterlösungen gegen Tests prüfen
                {/if}
              </button>
              {#if validierung}
                <ul class="validierung-liste">
                  {#each validierung.varianten as v}
                    <li class:bestanden={v.bestanden}>
                      <i class="fa-solid {v.bestanden ? 'fa-check' : 'fa-xmark'}" aria-hidden="true"></i>
                      <strong>{v.variante}</strong>
                      <span class="num">{v.sichtbar_pass}/{v.sichtbar_total}</span> sichtbar,
                      <span class="num">{v.versteckt_pass}/{v.versteckt_pass + v.versteckt_fail}</span> versteckt,
                      <span class="num">{v.laufzeit_ms.toFixed(0)}</span> ms
                      {#if v.fehler_text}
                        <pre class="fehler-text">{v.fehler_text}</pre>
                      {/if}
                    </li>
                  {/each}
                </ul>
              {/if}
            </div>
          </fieldset>
        {/if}
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
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.6);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    backdrop-filter: blur(2px);
    padding: var(--sp-3);
  }
  .dialog {
    background: var(--bg-card);
    border: 1px solid var(--border);
    width: 100%;
    max-width: 1000px;
    max-height: 92vh;
    display: flex;
    flex-direction: column;
    box-shadow: var(--shadow-lg);
  }
  .dlg-kopf {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: var(--sp-3) var(--sp-4);
    border-bottom: 1px solid var(--border);
    background: var(--bg-card-2);
    flex-shrink: 0;
  }
  .dlg-kopf h2 {
    margin: 0;
    font-size: var(--fs-md);
    font-weight: 600;
  }
  .schliessen {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--fg-dim);
    width: 32px;
    height: 32px;
    border-radius: var(--radius-sm);
    cursor: pointer;
  }
  .schliessen:hover {
    color: var(--red);
    border-color: var(--red);
  }

  .body {
    overflow-y: auto;
    padding: var(--sp-3) var(--sp-4);
    display: flex;
    flex-direction: column;
    gap: var(--sp-3);
    flex: 1;
  }
  .dlg-fuss {
    display: flex;
    justify-content: flex-end;
    gap: var(--sp-2);
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
  .lead {
    margin: 0 0 var(--sp-2);
    color: var(--fg-dim);
    font-size: var(--fs-xs);
    font-family: var(--quick);
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: var(--sp-2);
  }
  .grid label.weit {
    grid-column: span 2;
  }
  label {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  label span {
    font-size: var(--fs-xs);
    color: var(--fg-dim);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  label small {
    text-transform: none;
    letter-spacing: 0;
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
  input:focus, select:focus, textarea:focus {
    outline: 1px solid var(--accent);
    border-color: var(--accent);
  }
  input:disabled {
    opacity: 0.6;
  }
  textarea {
    font-family: var(--quick);
    resize: vertical;
  }
  textarea.mono, input.mono {
    font-family: var(--mono);
    font-size: var(--fs-xs);
  }

  .test-zeile {
    display: grid;
    grid-template-columns: 1fr 24px 1fr 32px;
    gap: var(--sp-2);
    align-items: center;
    margin-bottom: var(--sp-1);
  }
  .test-zeile .zeichen {
    color: var(--fg-mute);
    text-align: center;
  }

  .hint-zeile {
    display: grid;
    grid-template-columns: 100px 1fr 32px;
    gap: var(--sp-2);
    margin-bottom: var(--sp-2);
    align-items: start;
  }
  .hint-zeile .hint-kosten {
    flex-direction: column;
  }

  .opt-liste { display: flex; flex-direction: column; gap: var(--sp-1); }
  .opt-zeile {
    display: grid;
    grid-template-columns: 24px 1fr 32px;
    gap: var(--sp-2);
    align-items: center;
  }
  .opt-label {
    font-size: var(--fs-xs);
    color: var(--fg-dim);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: var(--sp-1);
  }

  .add, .entf, .primaer, .abbrechen, .schliessen, .action {
    cursor: pointer;
    border-radius: var(--radius-sm);
    font-family: inherit;
  }
  .add {
    background: transparent;
    border: 1px dashed var(--accent);
    color: var(--accent);
    padding: 4px 12px;
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: var(--sp-2);
    align-self: flex-start;
  }
  .add:hover:not(:disabled) {
    background: color-mix(in srgb, var(--accent) 14%, transparent);
  }
  .add:disabled { opacity: 0.5; cursor: not-allowed; }
  .entf {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--fg-dim);
    width: 32px;
    height: 32px;
  }
  .entf:hover {
    color: var(--red);
    border-color: var(--red);
  }
  .primaer {
    background: color-mix(in srgb, var(--accent) 14%, transparent);
    border: 1px solid var(--accent);
    color: var(--accent);
    padding: 8px 16px;
    font-size: var(--fs-sm);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .primaer:hover:not(:disabled) {
    background: color-mix(in srgb, var(--accent) 22%, transparent);
  }
  .primaer:disabled { opacity: 0.5; cursor: not-allowed; }
  .abbrechen {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--fg-dim);
    padding: 8px 16px;
    font-size: var(--fs-sm);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .abbrechen:hover:not(:disabled) {
    color: var(--fg);
    border-color: var(--fg);
  }
  .action.sek {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--fg-dim);
    padding: 6px 12px;
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .action.sek:hover:not(:disabled) {
    color: var(--accent);
    border-color: var(--accent);
  }

  .fehler-box {
    margin: var(--sp-3) var(--sp-4) 0;
    background: color-mix(in srgb, var(--red) 12%, transparent);
    border: 1px solid var(--red);
    color: var(--fg);
    padding: var(--sp-2) var(--sp-3);
    border-radius: var(--radius-sm);
    display: flex;
    gap: var(--sp-2);
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

  .muster-eintrag {
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: var(--sp-2);
    margin-bottom: var(--sp-2);
    border-radius: var(--radius-sm);
  }
  .muster-eintrag summary {
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: var(--accent);
    font-family: var(--mono);
    font-size: var(--fs-xs);
    text-transform: uppercase;
  }
  .m-titel { letter-spacing: 0.05em; }
  .muster-eintrag textarea { margin-top: var(--sp-2); }
  .muster-eintrag .hint {
    color: var(--fg-mute);
    font-family: var(--quick);
    font-size: var(--fs-xs);
    display: block;
    margin-top: 4px;
  }

  .neu-loesung {
    display: flex;
    flex-direction: column;
    gap: var(--sp-1);
    margin-top: var(--sp-3);
    padding: var(--sp-2);
    border: 1px dashed var(--border);
    border-radius: var(--radius-sm);
  }
  .neu-label {
    font-size: var(--fs-xs);
    color: var(--fg-dim);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  .validieren-zeile {
    margin-top: var(--sp-3);
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
  }
  .validierung-liste {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .validierung-liste li {
    background: var(--bg-card);
    border: 1px solid var(--border);
    padding: 4px var(--sp-2);
    font-size: var(--fs-xs);
    color: var(--fg-dim);
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    align-items: center;
  }
  .validierung-liste li.bestanden {
    border-color: var(--green);
  }
  .validierung-liste li i { color: var(--red); }
  .validierung-liste li.bestanden i { color: var(--green); }
  .validierung-liste strong { color: var(--fg); font-weight: 600; }
  .validierung-liste .num { color: var(--fg); font-family: var(--num); }
  .fehler-text {
    width: 100%;
    margin: 4px 0 0;
    padding: var(--sp-2);
    background: var(--bg);
    border: 1px solid var(--border);
    color: var(--red);
    font-family: var(--mono);
    font-size: var(--fs-xs);
    white-space: pre-wrap;
  }
</style>
