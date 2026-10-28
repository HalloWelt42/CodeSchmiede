<script lang="ts">
  /*
   * Muster-Jagd (Spiel): Aufgabe mit Spickzettel und Sternen | Muster mit
   * live markierten Treffern und Nieten | Wertung.
   *
   * Die Vorschau markiert im Browser mit derselben Regel wie der Prüfer
   * (lib/muster.ts), in einem Worker mit Zeitgrenze. Verbindlich prüft der
   * Server in der JavaScript-Sandbox, dazu gegen versteckte Zeilen.
   *
   * Frontmatter-Felder (im `extra`-Block `muster`):
   *   treffer, nieten:   sichtbare Zeilen
   *   flags:             etwa "i"
   *   sterne:            {zwei, drei}: höchstens so viele Zeichen
   *   spickzettel:       [[Zeichen, Bedeutung], ...]
   */
  import { onDestroy, onMount } from 'svelte';
  import { aufgabenApi } from '../api/AufgabenApi';
  import { progressApi } from '../api/ProgressApi';
  import { submissionsApi } from '../api/SubmissionsApi';
  import { unmarkiert, type Markierung } from '../muster';
  import { MusterVorschau, ZU_GIERIG } from '../sandbox/MusterVorschau';
  import { fassung } from '../stores/FassungStore.svelte';
  import { progressStore } from '../stores/ProgressStore.svelte';
  import { route } from '../stores/RouteStore.svelte';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import type { SubmissionAntwort } from '../types/Submission';
  import BeschreibungsBereich from './BeschreibungsBereich.svelte';
  import DreiSpaltenLayout from './DreiSpaltenLayout.svelte';
  import MusterloesungenBereich from './MusterloesungenBereich.svelte';
  import SpaltenReiter from './SpaltenReiter.svelte';
  import VerlaufBereich from './VerlaufBereich.svelte';
  import BelohnungsBand from './spiel/BelohnungsBand.svelte';

  interface MusterLevel {
    treffer: string[];
    nieten: string[];
    flags?: string;
    sterne: { zwei: number; drei: number };
    spickzettel?: [string, string][];
  }

  let { detail }: { detail: AufgabeDetail } = $props();

  let level = $derived(detail.extra?.['muster'] as MusterLevel);
  let flags = $derived(level.flags ?? '');
  let zeilen = $derived([...level.treffer, ...level.nieten]);

  let muster = $state('');
  let gesichertes_muster = $state('');
  let abgaben = $state(0);
  let pruefen_laeuft = $state(false);
  let ergebnis = $state<SubmissionAntwort | null>(null);
  let fehler = $state<string | null>(null);
  // svelte-ignore state_referenced_locally
  let musterloesungen_frei = $state(detail.musterloesungen_frei);
  let aktiver_tab = $state<'aufgabe' | 'loesungen'>('aufgabe');
  let bestwert = $state<number | null>(null);

  $effect(() => {
    if (pruefen_laeuft || muster !== gesichertes_muster) return fassung.halten();
  });

  // Live-Vorschau: leeres Muster markiert nichts; ein Auftrag läuft nach dem letzten Tastendruck
  const vorschau = new MusterVorschau();
  let markierung = $state<Markierung | null>(null);
  let zu_gierig = $state(false);
  let auftrag = 0;
  $effect(() => {
    const m = muster;
    const nr = ++auftrag;
    if (!m) {
      markierung = null;
      zu_gierig = false;
      return;
    }
    const uhr = setTimeout(async () => {
      const r = await vorschau.markiere(m, flags, zeilen);
      if (nr !== auftrag) return;
      zu_gierig = r === ZU_GIERIG;
      markierung = r === ZU_GIERIG ? null : r;
    }, 80);
    return () => clearTimeout(uhr);
  });
  onDestroy(() => vorschau.beenden());

  // ohne Vorschau (leer oder zu gierig) stehen die Zeilen unmarkiert da
  let anzeige = $derived(markierung ?? unmarkiert(zeilen));
  let soll = $derived(zeilen.map((_, i) => i < level.treffer.length));
  let stimmt = $derived(
    markierung && !markierung.fehler ? markierung.zeilen.map((z, i) => z.getroffen === soll[i]) : null,
  );
  let richtig = $derived(stimmt ? stimmt.filter(Boolean).length : 0);
  let anteil = $derived(Math.round((richtig / zeilen.length) * 100));
  let richtigTreffer = $derived(stimmt ? stimmt.slice(0, level.treffer.length).filter(Boolean).length : 0);

  let urteil = $derived.by(() => {
    if (!muster) return { titel: 'Noch kein Muster', unter: 'Tippe ein Muster, jede Zeile zeigt sofort, ob sie stimmt.' };
    if (zu_gierig) return { titel: 'Vorschau abgebrochen', unter: 'Das Muster braucht zu lange; vermutlich probiert es zu viele Wege durch.' };
    if (markierung?.fehler) return { titel: 'Muster unvollständig', unter: markierung.fehler };
    if (richtig < zeilen.length) return { titel: `${richtig} von ${zeilen.length} stimmen`, unter: 'Rot markierte Zeilen ansehen.' };
    const zuviel = muster.length - level.sterne.drei;
    return {
      titel: 'Alle sichtbaren Zeilen stimmen',
      unter: zuviel <= 0 ? 'Kurz genug für drei Sterne. Prüfen läuft auch gegen versteckte Zeilen.' : `Für drei Sterne ${zuviel} Zeichen kürzer.`,
    };
  });

  let sternKriterien = $derived([
    'alle Treffer, keine Niete, auch versteckte',
    `höchstens ${level.sterne.zwei} Zeichen`,
    `höchstens ${level.sterne.drei} Zeichen`,
  ]);
  let besteSterne = $derived(progressStore.proAufgabe[detail.id]?.sterne ?? null);

  onMount(async () => {
    try {
      const letzte = await aufgabenApi.letzteSubmission(detail.id);
      if (letzte.code && !letzte.bestanden) muster = letzte.code;
    } catch {
      // keine vorherige Abgabe
    }
    gesichertes_muster = muster;
    await ladeBestwert();
  });

  async function ladeBestwert(): Promise<void> {
    try {
      const verlauf = await aufgabenApi.submissionsVerlauf(detail.id, 20);
      const laengen = verlauf.filter((v) => v.bestanden).map((v) => v.code.trimEnd().length);
      bestwert = laengen.length ? Math.min(...laengen) : null;
    } catch {
      bestwert = null;
    }
  }

  async function pruefen(): Promise<void> {
    pruefen_laeuft = true;
    fehler = null;
    const eingereicht = muster;
    try {
      ergebnis = await submissionsApi.submit(detail.id, muster);
      gesichertes_muster = eingereicht;
      abgaben += 1;
      if (ergebnis.bestanden) musterloesungen_frei = true;
      await Promise.all([progressStore.ladeAlles(), ladeBestwert()]);
    } catch (e) {
      fehler = (e as Error).message;
    } finally {
      pruefen_laeuft = false;
    }
  }

  async function geheZuNaechster(): Promise<void> {
    try {
      const v = await progressApi.weiter(detail.id);
      route.setze(v.naechste_id ? 'aufgabe' : 'spiele', v.naechste_id ?? undefined);
    } catch {
      route.setze('spiele');
    }
  }
</script>

{#snippet sterne(anzahl: number, gross = false)}
  <span class="sterne" class:gross title="{anzahl} von 3 Sternen">
    {#each [1, 2, 3] as s (s)}<i class="fa-solid fa-star" class:aus={s > anzahl} aria-hidden="true"></i>{/each}
  </span>
{/snippet}

{#snippet zeile(i: number)}
  {@const z = anzeige.zeilen[i]}
  {@const ok = stimmt?.[i]}
  <div class="ziel-zeile" class:gut={ok === true} class:schlecht={ok === false}>
    <i class="fa-solid {ok === undefined ? 'fa-circle' : ok ? 'fa-check' : 'fa-xmark'}" aria-hidden="true"></i>
    <span>{#each z.abschnitte as a, j (j)}{#if a.treffer}<mark>{a.text}</mark>{:else}{a.text}{/if}{/each}</span>
  </div>
{/snippet}

<DreiSpaltenLayout
  mitteTitel="Muster"
  rechtsTitel="Wertung"
  schritte={['Aufgabe', 'Muster', 'Wertung']}
  pruefen={{ aktion: pruefen, laeuft: pruefen_laeuft, moeglich: muster !== '' }}
>
  {#snippet links()}
    {#if detail.musterloesungen_anzahl > 0}
      <SpaltenReiter
        reiter={[
          { id: 'aufgabe', titel: 'Aufgabe', icon: 'fa-file-lines' },
          { id: 'loesungen', titel: `Musterlösung`, icon: 'fa-lightbulb' },
        ]}
        bind:aktiv={aktiver_tab}
      />
    {/if}
    <div class="rollfeld ohne-rand">
      {#if aktiver_tab === 'aufgabe'}
        <BeschreibungsBereich
          aufgabeId={detail.id}
          markdown={detail.beschreibung_md}
          hints={detail.hints}
          tests_sichtbar={[]}
          anzahl_versteckt={0}
          quelle={detail.quelle}
          schwierigkeit_score={detail.schwierigkeit_score}
        />
        <div class="zusatz">
          {#if level.spickzettel?.length}
            <div class="gruppe">Spickzettel</div>
            <div class="spickzettel">
              {#each level.spickzettel as [zeichen, bedeutung] (zeichen)}<code>{zeichen}</code><span>{bedeutung}</span>{/each}
            </div>
          {/if}
          {#if flags}
            <p class="dim flags">Geprüft mit Flag <code>{flags}</code></p>
          {/if}
          <div class="gruppe">Sterne</div>
          <div class="spickzettel">
            {#each sternKriterien as text, i (i)}{@render sterne(i + 1)}<span>{text}</span>{/each}
          </div>
        </div>
      {:else}
        <MusterloesungenBereich aufgabeId={detail.id} bind:freigegeben={musterloesungen_frei} />
      {/if}
    </div>
  {/snippet}

  {#snippet mitteZusatz()}
    <span class="num laenge">{muster.length} Zeichen</span>
  {/snippet}

  {#snippet mitte()}
    <div class="rollfeld muster-mitte">
      <label class="muster-eingabe">
        <span>/</span>
        <input bind:value={muster} spellcheck="false" autocomplete="off" autocapitalize="off" aria-label="Muster" placeholder="Muster" />
        <span>/{flags}</span>
      </label>
      <div class="zwei-listen">
        <div>
          <div class="gruppe"><i class="fa-solid fa-bullseye treffer-i" aria-hidden="true"></i>Treffer, müssen passen {#if stimmt}<span class="num">{richtigTreffer} / {level.treffer.length}</span>{/if}</div>
          <div class="zeilen-liste">
            {#each level.treffer as _, i (i)}{@render zeile(i)}{/each}
          </div>
        </div>
        <div>
          <div class="gruppe"><i class="fa-solid fa-ban nieten-i" aria-hidden="true"></i>Nieten, dürfen nicht passen {#if stimmt}<span class="num">{richtig - richtigTreffer} / {level.nieten.length}</span>{/if}</div>
          <div class="zeilen-liste">
            {#each level.nieten as _, i (i)}{@render zeile(level.treffer.length + i)}{/each}
          </div>
        </div>
      </div>
    </div>
  {/snippet}

  {#snippet rechts()}
    <div class="rollfeld">
      {#if ergebnis?.belohnung}<BelohnungsBand belohnung={ergebnis.belohnung} />{/if}
      <div class="wertung-leiste">
        <div class="ring" style:--wert={anteil}><span>{anteil}</span></div>
        <div class="wertung-text"><b>{urteil.titel}</b><span>{urteil.unter}</span></div>
      </div>

      {#if pruefen_laeuft}
        <p class="dim"><i class="fa-solid fa-spinner fa-spin" aria-hidden="true"></i> Muster läuft in der Sandbox ...</p>
      {:else if fehler}
        <p class="hinweis-box fehler">{fehler}</p>
      {:else if ergebnis}
        {@const p = ergebnis.pruefung}
        <div class="ergebnis-kopf" class:nein={!ergebnis.bestanden}>
          <i class="fa-solid {ergebnis.bestanden ? 'fa-circle-check' : 'fa-circle-xmark'}" aria-hidden="true"></i>
          {ergebnis.bestanden ? 'Bestanden' : 'Noch nicht bestanden'}
          {#if p.wertung}{@render sterne(p.wertung.sterne)}{/if}
        </div>
        {#if p.versteckt_pass + p.versteckt_fail > 0}
          <p class="dim versteckt">
            Versteckte Zeilen: {p.versteckt_pass} von {p.versteckt_pass + p.versteckt_fail} richtig
          </p>
        {/if}
        {#if p.stderr}<pre class="fehlerausgabe">{p.stderr}</pre>{/if}
        {#if ergebnis.bestanden}
          <button class="knopf primaer" onclick={geheZuNaechster}>
            <i class="fa-solid fa-forward" aria-hidden="true"></i>Nächstes Level
          </button>
        {/if}
      {/if}

      {#if bestwert !== null}
        <div class="gruppe abstand">Dein Bestwert</div>
        <p class="bestwert"><span class="num">{bestwert}</span> Zeichen{#if besteSterne}, {@render sterne(besteSterne)}{/if}</p>
      {/if}
      <VerlaufBereich aufgabeId={detail.id} stand={abgaben} onUebernehmen={(c) => (muster = c.trimEnd())} />
    </div>
  {/snippet}
</DreiSpaltenLayout>

<style>
  .zusatz { padding: 0 var(--sp-4) var(--sp-4); }
  .flags { font-size: var(--fs-sm); margin: var(--sp-2) 0 0; }
  .muster-mitte {
    display: flex;
    flex-direction: column;
    gap: var(--sp-3);
  }
  .zwei-listen {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: var(--sp-3);
  }
  :global([data-geraet='telefon']) .zwei-listen { grid-template-columns: minmax(0, 1fr); }
  .treffer-i { color: var(--green); }
  .nieten-i { color: var(--red); }
  .laenge {
    color: var(--fg);
    text-transform: none;
    letter-spacing: 0;
  }
  .wertung-leiste {
    margin-bottom: var(--sp-3);
  }
  .ergebnis-kopf .sterne { margin-left: auto; }
  .versteckt { font-size: var(--fs-sm); margin: var(--sp-2) 0; }
  .abstand { margin-top: var(--sp-4); }
  .bestwert { margin: 0 0 var(--sp-3); font-size: var(--fs-sm); }
  .fehlerausgabe {
    margin: 0 0 var(--sp-3);
    padding: var(--sp-2);
    background: var(--bg);
    border: 1px solid var(--border);
    color: var(--red);
    font-family: var(--mono);
    font-size: 12px;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
  }
</style>
