<script lang="ts">
  /*
   * LueckentextView -- Aufgaben mit Code-Templates und Platzhaltern.
   *
   * Template kommt im `detail.extra.lueckentext`-Block:
   *   template: "code mit ___1___ und ___2___ Platzhaltern"
   *   luecken: [{nummer: 1, hinweis?: "..."}, ...]
   *
   * Nutzer fuellt pro Platzhalter ein Feld, wir bauen JSON-Map und
   * schicken sie an /api/submissions; Backend setzt die Werte ein
   * und laesst die Tests laufen.
   */
  import { onMount } from 'svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import { fassung } from '../stores/FassungStore.svelte';
  import { submissionsApi } from '../api/SubmissionsApi';
  import { progressApi } from '../api/ProgressApi';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import type { SubmissionAntwort } from '../types/Submission';
  import BeschreibungsBereich from './BeschreibungsBereich.svelte';
  import DreiSpaltenLayout from './DreiSpaltenLayout.svelte';
  import OutputBereich from './OutputBereich.svelte';

  interface Luecke {
    nummer: number;
    hinweis?: string;
  }

  interface Props {
    detail: AufgabeDetail;
  }

  let { detail }: Props = $props();

  let lueckentext = $derived(
    (detail.extra?.['lueckentext'] as { template?: string; luecken?: Luecke[] }) ?? {},
  );
  let template = $derived(lueckentext.template ?? '');
  let luecken = $derived<Luecke[]>(lueckentext.luecken ?? []);

  let werte = $state<Record<string, string>>({});

  onMount(() => {
    const neu: Record<string, string> = {};
    for (const l of luecken) {
      neu[String(l.nummer)] = '';
    }
    werte = neu;
  });

  let vorschau_code = $derived(
    template.replace(/___(\d+)___/g, (_, n) => werte[n] ?? `___${n}___`),
  );

  let pruefen_laeuft = $state(false);
  let ergebnis = $state<SubmissionAntwort | null>(null);
  let fehler = $state<string | null>(null);

  // Zuletzt geprüfte Antworten. Sind Lücken ausgefüllt und noch nicht
  // geprüft oder läuft eine Prüfung, wartet eine neue Fassung mit dem
  // Neuladen.
  let gesicherte_werte = $state(JSON.stringify({}));
  $effect(() => {
    const ausgefuellt = Object.values(werte).some((w) => w.trim() !== '');
    const ungeprueft = ausgefuellt && JSON.stringify(werte) !== gesicherte_werte;
    if (pruefen_laeuft || ungeprueft) return fassung.halten();
  });

  async function pruefen(): Promise<void> {
    pruefen_laeuft = true;
    fehler = null;
    try {
      // Code = JSON-Map. Backend entpackt + ersetzt im Template.
      const json = JSON.stringify(werte);
      ergebnis = await submissionsApi.submit(detail.id, json);
      gesicherte_werte = json;
      await progressStore.ladeAlles();
    } catch (e) {
      fehler = (e as Error).message;
    } finally {
      pruefen_laeuft = false;
    }
  }

  function alleAusgefuellt(): boolean {
    return luecken.every((l) => (werte[String(l.nummer)] ?? '').trim() !== '');
  }

  function neuStarten(): void {
    werte = Object.fromEntries(luecken.map((l) => [String(l.nummer), '']));
    ergebnis = null;
  }

  async function geheZuNaechster(): Promise<void> {
    try {
      const v = await progressApi.weiter(detail.id);
      route.setze(v.naechste_id ? 'aufgabe' : 'aufgaben', v.naechste_id ?? undefined);
    } catch {
      route.setze('aufgaben');
    }
  }
</script>

<DreiSpaltenLayout
  mitteTitel="Lückentext, {luecken.length} Felder"
  rechtsTitel="Ergebnis"
  schritte={['Aufgabe', 'Ausfüllen', 'Ergebnis']}
  pruefen={{ aktion: pruefen, laeuft: pruefen_laeuft, moeglich: alleAusgefuellt() }}
>
  {#snippet links()}
    <div class="rollfeld ohne-rand">
      <BeschreibungsBereich
        aufgabeId={detail.id}
        markdown={detail.beschreibung_md}
        hints={detail.hints}
        tests_sichtbar={detail.tests_sichtbar}
        anzahl_versteckt={detail.anzahl_versteckte_tests}
        quelle={detail.quelle}
        schwierigkeit_score={detail.schwierigkeit_score}
      />
    </div>
  {/snippet}

  {#snippet mitte()}
    <div class="rollfeld">
      <div class="luecken">
        {#each luecken as l (l.nummer)}
          <label class="luecke-feld">
            <span class="luecke-nr">___{l.nummer}___</span>
            <input type="text" bind:value={werte[String(l.nummer)]} placeholder="..." />
            {#if l.hinweis}<small class="feld-hinweis">{l.hinweis}</small>{/if}
          </label>
        {/each}
      </div>
      <div class="gruppe abstand">Code mit deinen Einträgen</div>
      <pre class="code">{vorschau_code}</pre>
      <button class="knopf" onclick={neuStarten}>
        <i class="fa-solid fa-rotate-left" aria-hidden="true"></i>Felder leeren
      </button>
    </div>
  {/snippet}

  {#snippet rechts()}
    <div class="rollfeld">
      <OutputBereich
        {ergebnis}
        {fehler}
        laeuft={pruefen_laeuft}
        anzahl_versteckt={detail.anzahl_versteckte_tests}
        onWeiter={geheZuNaechster}
      />
    </div>
  {/snippet}
</DreiSpaltenLayout>

<style>
  .luecken {
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
  }
  .luecke-feld {
    display: grid;
    grid-template-columns: auto minmax(0, 1fr);
    gap: 4px var(--sp-2);
    align-items: center;
  }
  .luecke-nr {
    font-family: var(--mono);
    font-size: 12px;
    color: var(--accent);
  }
  .luecke-feld input {
    height: 30px;
    padding: 0 var(--sp-2);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    background: var(--bg-card);
    font-family: var(--mono);
    font-size: 13px;
  }
  .luecke-feld input:focus { outline: none; border-color: var(--accent); }
  .feld-hinweis {
    grid-column: 2;
    color: var(--fg-dim);
    font-size: var(--fs-xs);
  }
  .abstand { margin-top: var(--sp-3); }
  .code {
    margin: 0 0 var(--sp-3);
    padding: var(--sp-2) var(--sp-3);
    border: 1px solid var(--border);
    background: var(--bg-card);
    font-family: var(--mono);
    font-size: 12px;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
  }
</style>
