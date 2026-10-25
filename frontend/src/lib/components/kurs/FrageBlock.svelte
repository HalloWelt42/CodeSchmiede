<script lang="ts">
  /*
   * Eine Verständnisfrage (Auswahl, Lücke, Zeilen ordnen, Fehlerstelle) oder eine Vorhersage (Auswahl, Eintippen).
   * Geprüft wird auf dem Server; erst sein Urteil bringt die Erklärung. Falsche Antworten kosten nichts, man darf
   * es so oft versuchen, wie man will.
   */
  import type { Antwort, FrageSicht, Urteil, VorhersageSicht } from '../../api/KursApi';
  import CodeBlock from './CodeBlock.svelte';

  interface Props {
    element: string;
    sprache: string;
    frage?: FrageSicht;
    vorhersage?: VorhersageSicht;
    senden: (a: Antwort) => Promise<Urteil>;
    beiUrteil?: (u: Urteil) => void;
  }
  let { element, sprache, frage, vorhersage, senden, beiUrteil }: Props = $props();

  type Art = 'auswahl' | 'luecke' | 'ordnen' | 'fehlerstelle' | 'eintippen';
  let art = $derived<Art>(frage ? frage.frageart : vorhersage?.art === 'eintippen' ? 'eintippen' : 'auswahl');
  let optionen = $derived(frage?.optionen ?? vorhersage?.optionen ?? []);
  let mehrere = $derived(frage?.mehrere ?? false);
  // Vorhersagen zeigen Ausgaben in fester Breite, außer sie stellen eine eigene Frage (etwa nach der Zeilenzahl)
  let alsCode = $derived(vorhersage ? !vorhersage.frage : (frage?.als_code ?? false));
  let vorhersageText = $derived(vorhersage?.frage ?? (sprache === 'sql' ? 'Was liefert die Abfrage?' : 'Was gibt das Beispiel aus?'));

  let urteil = $state<Urteil | null>(null);
  let gewaehlt = $state<number[]>([]);
  let luecken = $state<string[]>([]);
  let reihe = $state<number[]>([]);
  let zeile = $state<number | null>(null);
  let eingetippt = $state('');
  let sendet = $state(false);
  let fehler = $state<string | null>(null);

  $effect(() => {
    if (frage?.frageart === 'luecke' && luecken.length !== (frage.luecken ?? 0)) luecken = Array(frage.luecken ?? 0).fill('');
    if (frage?.frageart === 'ordnen' && reihe.length !== (frage.zeilen?.length ?? 0)) reihe = (frage.zeilen ?? []).map((_, i) => i);
  });

  async function pruefe(antwort: Omit<Antwort, 'element'>) {
    sendet = true;
    fehler = null;
    try {
      urteil = await senden({ element, ...antwort });
      beiUrteil?.(urteil);
    } catch (e) {
      fehler = e instanceof Error ? e.message : String(e);
    } finally {
      sendet = false;
    }
  }

  function waehle(i: number) {
    if (mehrere) {
      gewaehlt = gewaehlt.includes(i) ? gewaehlt.filter((x) => x !== i) : [...gewaehlt, i];
      urteil = null;
      return;
    }
    gewaehlt = [i];
    void pruefe({ wahl: [i] });
  }

  function schiebe(stelle: number, richtung: -1 | 1) {
    const ziel = stelle + richtung;
    if (ziel < 0 || ziel >= reihe.length) return;
    const neu = [...reihe];
    [neu[stelle], neu[ziel]] = [neu[ziel], neu[stelle]];
    reihe = neu;
    urteil = null;
  }

  function zeileWaehlen(nr: number) {
    zeile = nr;
    void pruefe({ zeile: nr });
  }

  let klassenFehler = $derived<Record<number, string>>(zeile === null || !urteil ? {} : { [zeile]: urteil.richtig ? 'richtig' : 'gewaehlt' });
  let erledigt = $derived(urteil?.richtig ?? frage?.richtig ?? vorhersage?.beantwortet ?? false);
</script>

<div class="frage-block" class:vorhersage={!!vorhersage}>
  <div class="frage-kopf">
    <i class="fa-solid {vorhersage ? 'fa-wand-magic-sparkles' : 'fa-circle-question'}" aria-hidden="true"></i>
    {vorhersage ? 'Vorhersage' : 'Kurze Frage'}
    {#if erledigt && !urteil}<span class="erledigt"><i class="fa-solid fa-check" aria-hidden="true"></i>schon beantwortet</span>{/if}
  </div>
  <div class="frage-text">{vorhersage ? (art === 'eintippen' && !vorhersage.frage ? `${vorhersageText} Tippe die Ausgabe.` : vorhersageText) : frage?.text}</div>

  {#if frage?.code && art === 'auswahl'}<CodeBlock code={frage.code} {sprache} />{/if}

  {#if art === 'auswahl'}
    <div class="wahl-liste">
      {#each optionen as o, i (i)}
        <button
          class="wahlknopf"
          class:richtig={gewaehlt.includes(i) && urteil?.richtig}
          class:falsch={gewaehlt.includes(i) && urteil && !urteil.richtig}
          class:markiert={mehrere && gewaehlt.includes(i) && !urteil}
          disabled={sendet}
          onclick={() => waehle(i)}
        ><kbd>{'ABCDEF'[i]}</kbd>{#if alsCode}<pre>{o}</pre>{:else}<span>{o}</span>{/if}</button>
      {/each}
    </div>
    {#if mehrere}<div class="weiter-zeile"><span class="dim">Mehrere Antworten richtig</span><button class="knopf voll" disabled={!gewaehlt.length || sendet} onclick={() => pruefe({ wahl: gewaehlt })}><i class="fa-solid fa-check" aria-hidden="true"></i>Prüfen</button></div>{/if}
  {:else if art === 'luecke' && frage?.code}
    <CodeBlock code={frage.code} {sprache} bind:luecken />
    <div class="weiter-zeile"><button class="knopf voll" disabled={sendet || luecken.some((l) => !l.trim())} onclick={() => pruefe({ luecken })}><i class="fa-solid fa-check" aria-hidden="true"></i>Prüfen</button></div>
  {:else if art === 'ordnen' && frage?.zeilen}
    <div class="ordnen" class:geprueft={!!urteil}>
      {#each reihe as idx, stelle (idx)}
        <div class="ordnen-zeile" class:ok={urteil?.richtig} class:nein={urteil && !urteil.richtig}>
          <i class="fa-solid fa-grip-vertical" aria-hidden="true"></i>
          <span>{frage.zeilen[idx]}</span>
          <span class="pfeile">
            <button onclick={() => schiebe(stelle, -1)} disabled={stelle === 0} aria-label="nach oben"><i class="fa-solid fa-arrow-up" aria-hidden="true"></i></button>
            <button onclick={() => schiebe(stelle, 1)} disabled={stelle === reihe.length - 1} aria-label="nach unten"><i class="fa-solid fa-arrow-down" aria-hidden="true"></i></button>
          </span>
        </div>
      {/each}
    </div>
    <div class="weiter-zeile"><button class="knopf voll" disabled={sendet} onclick={() => pruefe({ reihenfolge: reihe })}><i class="fa-solid fa-check" aria-hidden="true"></i>Prüfen</button></div>
  {:else if art === 'fehlerstelle' && frage?.code}
    <CodeBlock code={frage.code} {sprache} beiZeile={zeileWaehlen} klassen={klassenFehler} />
    <span class="dim" style="font-size:var(--fs-sm)">Klicke die Zeile mit dem Fehler an.</span>
  {:else if art === 'eintippen'}
    <textarea class="eingetippt" rows="3" spellcheck="false" bind:value={eingetippt} placeholder={vorhersage?.frage ? 'Deine Antwort' : 'Ausgabe Zeile für Zeile'}></textarea>
    <div class="weiter-zeile"><button class="knopf voll" disabled={sendet || !eingetippt.trim()} onclick={() => pruefe({ eingetippt })}><i class="fa-solid fa-check" aria-hidden="true"></i>Prüfen</button></div>
  {/if}

  {#if urteil}
    <div class="erklaerung" class:gut={urteil.richtig} class:schlecht={!urteil.richtig}>
      <i class="fa-solid {urteil.richtig ? 'fa-circle-check' : 'fa-lightbulb'}" aria-hidden="true"></i><span>{urteil.erklaerung}</span>
    </div>
  {/if}
  {#if fehler}<div class="erklaerung schlecht"><i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i><span>{fehler}</span></div>{/if}
</div>

<style>
  .erledigt { margin-left: auto; color: var(--green); text-transform: none; letter-spacing: 0; display: inline-flex; gap: 6px; align-items: center; }
  .markiert { border-color: var(--accent); background: color-mix(in srgb, var(--accent) 10%, var(--bg-card)); }
  .eingetippt { width: 100%; padding: var(--sp-2) var(--sp-3); border: 1px solid var(--border); border-radius: var(--radius-sm); background: var(--ed-grund); color: var(--ed-text); font-family: var(--mono); font-size: 14px; resize: vertical; }
  .eingetippt:focus { outline: none; border-color: var(--accent); }
</style>
