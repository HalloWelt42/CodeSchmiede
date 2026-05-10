<script lang="ts">
  /*
   * Aufgabentyp `output_quiz`: Code-Schnipsel + Multiple-Choice.
   * Frontmatter enthält im `extra.quiz`-Feld:
   *   code: string
   *   optionen: string[]
   *   richtig_index: number
   *
   * Antwort an /api/submissions ist der gewählte Index als String.
   * Backend pruefe-Funktion (`output_quiz_pruefer`) macht den Vergleich.
   */
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import { progressApi } from '../api/ProgressApi';
  import { submissionsApi } from '../api/SubmissionsApi';
  import type { AufgabeDetail } from '../types/Aufgabe';

  interface QuizDef {
    code: string;
    optionen: string[];
    richtig_index: number;
  }

  interface Props {
    detail: AufgabeDetail;
  }

  let { detail }: Props = $props();

  let quiz = $derived(detail.extra?.quiz as QuizDef | undefined);

  let gewaehlt = $state<number | null>(null);
  let pruefen_laeuft = $state(false);
  let bestanden = $state<boolean | null>(null);
  let stderr = $state<string>('');
  let punkte = $state<number>(0);
  let fehler = $state<string | null>(null);

  async function waehleUndPruefe(index: number): Promise<void> {
    if (pruefen_laeuft) return;
    gewaehlt = index;
    pruefen_laeuft = true;
    fehler = null;
    try {
      const ergebnis = await submissionsApi.submit(detail.id, String(index));
      bestanden = ergebnis.bestanden;
      stderr = ergebnis.pruefung.stderr;
      punkte = ergebnis.progress.punkte_erreicht;
      await progressStore.ladeAlles();
    } catch (e) {
      fehler = (e as Error).message;
    } finally {
      pruefen_laeuft = false;
    }
  }

  async function geheZuNaechster(): Promise<void> {
    try {
      const v = await progressApi.weiter(detail.id);
      if (v.naechste_id) {
        route.setze('aufgabe', v.naechste_id);
      } else {
        route.setze('aufgaben');
      }
    } catch {
      route.setze('aufgaben');
    }
  }

  function nochmal(): void {
    gewaehlt = null;
    bestanden = null;
    stderr = '';
  }
</script>

<div class="quiz">
  {#if !quiz}
    <p class="warn">
      <i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i>
      Diese Aufgabe ist als <code>output_quiz</code> markiert, aber das
      <code>quiz</code>-Feld fehlt im Frontmatter.
    </p>
  {:else}
    <section class="frage">
      <h2>Was gibt dieser Code aus?</h2>
      <pre class="code"><code>{quiz.code}</code></pre>
    </section>

    <section class="optionen">
      <h3>Wähle die richtige Ausgabe:</h3>
      <div class="optionen-liste">
        {#each quiz.optionen as opt, i (i)}
          {@const istRichtig = bestanden !== null && i === quiz.richtig_index}
          {@const istFalschGewaehlt = bestanden === false && gewaehlt === i}
          <button
            class="option"
            class:gewaehlt={gewaehlt === i}
            class:richtig={istRichtig}
            class:falsch={istFalschGewaehlt}
            disabled={pruefen_laeuft || bestanden !== null}
            onclick={() => waehleUndPruefe(i)}
          >
            <span class="opt-nummer">{String.fromCharCode(65 + i)}</span>
            <pre class="opt-text"><code>{opt}</code></pre>
            {#if istRichtig}
              <i class="fa-solid fa-check status-icon" aria-hidden="true"></i>
            {:else if istFalschGewaehlt}
              <i class="fa-solid fa-xmark status-icon" aria-hidden="true"></i>
            {/if}
          </button>
        {/each}
      </div>
    </section>

    {#if fehler}
      <p class="warn">{fehler}</p>
    {/if}

    {#if bestanden !== null}
      <section class="ergebnis" class:ok={bestanden} class:fail={!bestanden}>
        {#if bestanden}
          <div class="ergebnis-zeile">
            <i class="fa-solid fa-check" aria-hidden="true"></i>
            <span class="ergebnis-text">Richtig!</span>
            <span class="punkte num">+{punkte} von {detail.schwierigkeit_score} Punkten</span>
          </div>
          <button class="weiter" onclick={geheZuNaechster}>
            Weiter
            <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
          </button>
        {:else}
          <div class="ergebnis-zeile">
            <i class="fa-solid fa-xmark" aria-hidden="true"></i>
            <span class="ergebnis-text">Leider falsch</span>
            <span class="hint">{stderr}</span>
          </div>
          <button class="nochmal" onclick={nochmal}>
            <i class="fa-solid fa-rotate-left" aria-hidden="true"></i>
            Nochmal versuchen
          </button>
        {/if}
      </section>
    {/if}
  {/if}
</div>

<style>
  .quiz {
    padding: var(--sp-5);
    overflow-y: auto;
    max-width: 880px;
    margin: 0 auto;
    width: 100%;
  }
  .warn {
    color: var(--orange);
    background: color-mix(in srgb, var(--orange) 10%, transparent);
    padding: var(--sp-3);
    border: 1px solid var(--orange);
    border-radius: var(--radius-sm);
  }

  .frage {
    margin-bottom: var(--sp-5);
  }
  h2 {
    font-family: var(--sans);
    font-size: var(--fs-md);
    color: var(--fg-dim);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin: 0 0 var(--sp-3);
  }
  h3 {
    font-family: var(--sans);
    font-size: var(--fs-sm);
    color: var(--fg-dim);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin: 0 0 var(--sp-3);
  }
  .code {
    margin: 0;
    padding: var(--sp-4);
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    overflow-x: auto;
  }
  .code code {
    font-family: var(--mono);
    font-size: var(--fs-md);
    line-height: 1.6;
    color: var(--fg);
    background: transparent;
    border: none;
    padding: 0;
  }

  .optionen-liste {
    display: flex;
    flex-direction: column;
    gap: var(--sp-2);
  }
  .option {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    padding: var(--sp-3);
    background: var(--bg-card-2);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    color: var(--fg);
    cursor: pointer;
    text-align: left;
    transition: border-color 0.15s, background 0.15s;
  }
  .option:hover:not(:disabled) {
    border-color: var(--accent);
  }
  .option:disabled {
    cursor: not-allowed;
  }
  .option.gewaehlt {
    border-color: var(--accent);
  }
  .option.richtig {
    border-color: var(--green);
    background: color-mix(in srgb, var(--green) 10%, transparent);
  }
  .option.falsch {
    border-color: var(--red);
    background: color-mix(in srgb, var(--red) 10%, transparent);
  }
  .opt-nummer {
    width: 32px;
    height: 32px;
    flex-shrink: 0;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: var(--bg);
    border: 1px solid var(--border);
    color: var(--accent);
    font-family: var(--num);
    font-size: var(--fs-md);
    border-radius: var(--radius-sm);
  }
  .opt-text {
    margin: 0;
    flex: 1;
    overflow-x: auto;
  }
  .opt-text code {
    font-family: var(--mono);
    font-size: var(--fs-sm);
    background: transparent;
    border: none;
    padding: 0;
    color: var(--fg);
    white-space: pre;
  }
  .status-icon {
    font-size: var(--fs-lg);
    flex-shrink: 0;
  }
  .option.richtig .status-icon { color: var(--green); }
  .option.falsch .status-icon { color: var(--red); }

  .ergebnis {
    margin-top: var(--sp-4);
    padding: var(--sp-3) var(--sp-4);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: var(--sp-3);
    flex-wrap: wrap;
  }
  .ergebnis.ok {
    background: color-mix(in srgb, var(--green) 10%, transparent);
    border-color: var(--green);
  }
  .ergebnis.fail {
    background: color-mix(in srgb, var(--red) 10%, transparent);
    border-color: var(--red);
  }
  .ergebnis-zeile {
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    flex-wrap: wrap;
  }
  .ergebnis-text {
    font-size: var(--fs-md);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .ergebnis.ok .ergebnis-text,
  .ergebnis.ok i { color: var(--green); }
  .ergebnis.fail .ergebnis-text,
  .ergebnis.fail i { color: var(--red); }
  .punkte {
    color: var(--green);
    font-size: var(--fs-md);
  }
  .hint {
    color: var(--fg-dim);
    font-family: var(--quick);
    font-size: var(--fs-sm);
  }
  .weiter {
    background: var(--green);
    border: 1px solid var(--green);
    color: var(--bg);
    padding: 8px 14px;
    font-size: var(--fs-sm);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: var(--radius-sm);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: var(--sp-2);
  }
  .weiter:hover { filter: brightness(1.1); }
  .nochmal {
    background: transparent;
    border: 1px solid var(--orange);
    color: var(--orange);
    padding: 8px 14px;
    font-size: var(--fs-sm);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: var(--radius-sm);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: var(--sp-2);
  }
  .nochmal:hover {
    background: color-mix(in srgb, var(--orange) 14%, transparent);
  }
</style>
