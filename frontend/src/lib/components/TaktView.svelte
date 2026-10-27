<script lang="ts">
  /*
   * Schaltungen mit Takt in der gemeinsamen Ansicht der Steuerungsspiele: der Schaltplan mit Flipflops als Editor,
   * rechts der Stand im gezeigten Takt (Zahl, Lämpchen oder 7-Segment-Anzeige, je mit Soll) und darunter der
   * Zeitverlauf aller Takte. Jede Änderung rechnet sofort neu (auf dem Server, ohne Sandbox); abspielen läuft Takt für
   * Takt, ein Klick in den Zeitverlauf springt zu einem Takt.
   */
  import { spielApi } from '../api/SpielApi';
  import { SPEICHER, istSiebenSegment } from '../steuerung/schaltplan';
  import type { AufgabeDetail } from '../types/Aufgabe';
  import type { CodeZugriff } from '../types/Steuerung';
  import type { TaktAblauf, TaktAnsicht, TaktKennzahlen, TaktWiedergabe } from '../types/Takt';
  import SchaltplanEditor from './steuerung/SchaltplanEditor.svelte';
  import SiebenSegment from './steuerung/SiebenSegment.svelte';
  import SteuerungsView from './steuerung/SteuerungsView.svelte';
  import Zeitverlauf from './steuerung/Zeitverlauf.svelte';

  let { detail }: { detail: AufgabeDetail } = $props();

  const BAUSTEINE: Record<string, string> = {
    FF: 'Flipflop: übernimmt beim Takt seinen Eingang D und zeigt ihn bis zum nächsten',
    UND: '1, wenn beide Eingänge 1 sind',
    ODER: '1, wenn mindestens einer 1 ist',
    XOR: '1, wenn genau einer 1 ist; mit 1 dreht es um',
    NAND: '0 nur, wenn beide 1 sind',
    NOR: '1 nur, wenn beide 0 sind',
    NICHT: 'dreht um: aus 1 wird 0',
  };

  /** Was im gezeigten Takt gilt: Werte (ohne Lauf null), Soll und Eingaben dieses Takts */
  function stand(ansicht: TaktAnsicht, w: TaktWiedergabe | null, nr: number) {
    const takt = Math.max(0, nr);
    const ablauf: Pick<TaktAblauf, 'eingaben' | 'soll'> = w ?? ansicht.ablaeufe[0];
    const zeichen = (folge: string | undefined) => folge?.[takt];
    return {
      takt,
      werte: w?.bilder[takt]?.[1] ?? null,
      soll: Object.fromEntries(ansicht.ausgaenge.map((a) => [a, zeichen(ablauf.soll[a]) ?? 'x'])),
      eingaben: Object.fromEntries(ansicht.eingaenge.map((e) => [e, zeichen(ablauf.eingaben[e]) ?? '0'])),
    };
  }

  function zahl(namen: string[], wert: (name: string) => number | null): number | null {
    let z = 0;
    for (const n of namen) {
      const w = wert(n);
      if (w == null) return null;
      z = z * 2 + w;
    }
    return z;
  }

  function bausteineIm(code: string): [number, number] {
    const zeilen = code.split('\n').map((z) => z.split('#')[0]).filter((z) => /=\s*[A-Z]+\s*\(/.test(z));
    const ff = zeilen.filter((z) => new RegExp(`=\\s*${SPEICHER}\\s*\\(`).test(z)).length;
    return [ff, zeilen.length - ff];
  }
</script>

{#snippet sterne(anzahl: number)}
  <span class="sterne" title="{anzahl} von 3 Sternen">
    {#each [1, 2, 3] as s (s)}<i class="fa-solid fa-star" class:aus={s > anzahl} aria-hidden="true"></i>{/each}
  </span>
{/snippet}

{#snippet hilfe(ansicht: TaktAnsicht)}
  <div class="gruppe">Bausteine</div>
  <div class="spickzettel">
    {#each ansicht.bausteine as b (b)}<code>{b}</code><span>{BAUSTEINE[b] ?? ''}</span>{/each}
    <code>0, 1</code><span>feste Werte, links unten im Plan</span>
  </div>
  <div class="gruppe">Plan als Text</div>
  <div class="spickzettel">
    <code>f0 = FF(n0)</code><span>ein Flipflop, sein Eingang D hängt an n0</span>
    <code>n0 = NICHT(f0)</code><span>Rückkopplung: erlaubt, wenn ein Flipflop dazwischen sitzt</span>
    <code>{ansicht.ausgaenge[0]} = f0</code><span>ein Ausgang zeigt, was f0 gemerkt hat</span>
  </div>
  <div class="gruppe">Abläufe</div>
  <div class="spickzettel">
    {#each ansicht.ablaeufe as a (a.name)}<code>{a.takte} Takte</code><span>{a.name}</span>{/each}
  </div>
  <div class="gruppe">Sterne</div>
  <div class="spickzettel">
    {@render sterne(1)}<span>alle Takte stimmen, auch in den versteckten Abläufen</span>
    {@render sterne(2)}<span>höchstens {ansicht.sterne.bausteine} {ansicht.sterne.bausteine === 1 ? 'Baustein' : 'Bausteine'} außer den Flipflops</span>
    {@render sterne(3)}<span>dazu höchstens {ansicht.sterne.tiefe} {ansicht.sterne.tiefe === 1 ? 'Baustein' : 'Bausteine'} auf dem längsten Weg</span>
  </div>
{/snippet}

{#snippet editor(ansicht: TaktAnsicht, zugriff: CodeZugriff, wiedergabe: TaktWiedergabe | null, nr: number)}
  <SchaltplanEditor {ansicht} {zugriff} werte={stand(ansicht, wiedergabe, nr).werte} zeile={-1} waehle={() => {}} takt />
{/snippet}

{#snippet szene(ansicht: TaktAnsicht, wiedergabe: TaktWiedergabe | null, nr: number, springe: (takt: number) => void)}
  {@const s = stand(ansicht, wiedergabe, nr)}
  {@const dauer = wiedergabe?.dauer ?? ansicht.ablaeufe[0].takte}
  {@const ist = (a: string) => s.werte?.[a] ?? null}
  {@const soll = (a: string) => (s.soll[a] === 'x' ? null : Number(s.soll[a]))}
  <div class="takt-leiste">
    <button class="knopf-klein" onclick={() => springe((s.takt + 1) % dauer)} disabled={!wiedergabe}>
      <i class="fa-solid fa-forward-step" aria-hidden="true"></i>Nächster Takt
    </button>
    {#if ansicht.eingaenge.length}
      <span class="eingaben">{#each ansicht.eingaenge as e (e)}<span class:an={s.eingaben[e] === '1'}>{e} = {s.eingaben[e]}</span>{/each}</span>
    {/if}
  </div>
  <div class="stand-rahmen">
    {#if istSiebenSegment(ansicht.ausgaenge)}
      <div class="paar"><SiebenSegment an={(seg) => ist(seg) === 1} /><small>ist</small></div>
      <div class="paar"><SiebenSegment an={(seg) => soll(seg) === 1} /><small>soll</small></div>
    {:else if ansicht.zahl.length}
      {@const z = zahl(ansicht.zahl, ist)}
      {@const zs = zahl(ansicht.zahl, soll)}
      <span class="gross num" class:falsch={z != null && zs != null && z !== zs}>{z ?? '?'}</span>
      <span class="bits num">{ansicht.zahl.join(' ')}<br />{ansicht.zahl.map((a) => ist(a) ?? '?').join(' ')}</span>
      <span class="soll-wert">soll<b class="num">{zs ?? '-'}</b></span>
    {:else}
      {#each ansicht.ausgaenge as a (a)}
        <div class="lampe-paar">
          <span class="lampe" class:an={ist(a) === 1} class:falsch={ist(a) != null && soll(a) != null && ist(a) !== soll(a)}></span>
          <b>{a}</b><small>soll {s.soll[a] === 'x' ? '-' : s.soll[a]}</small>
        </div>
      {/each}
    {/if}
  </div>
{/snippet}

{#snippet plan(ansicht: TaktAnsicht, wiedergabe: TaktWiedergabe | null, _: number, zeit: number, springe: (takt: number) => void)}
  {@const ablauf = wiedergabe ?? { ...ansicht.ablaeufe[0], dauer: ansicht.ablaeufe[0].takte }}
  <Zeitverlauf
    eingaenge={ansicht.eingaenge}
    ausgaenge={ansicht.ausgaenge}
    takte={ablauf.dauer}
    eingaben={ablauf.eingaben}
    soll={ablauf.soll}
    ist={wiedergabe ? wiedergabe.bilder.map((b) => b[1]) : null}
    jetzt={zeit}
    waehle={springe}
  />
{/snippet}

{#snippet kennzahlen(ansicht: TaktAnsicht, wiedergabe: TaktWiedergabe)}
  {@const k = wiedergabe.kennzahlen}
  <div class="sim-werte" style:grid-template-columns="repeat(2, minmax(0, 1fr))">
    <div><span class="num" class:gut={k.richtig === k.takte} class:schlecht={k.richtig < k.takte}>{k.richtig} / {k.takte}</span><small>Takte richtig</small></div>
    <div><span class="num">{k.flipflops}</span><small>Flipflops</small></div>
    <div><span class="num" class:gut={k.bausteine <= ansicht.sterne.bausteine}>{k.bausteine}</span><small>Bausteine</small></div>
    <div><span class="num" class:gut={k.tiefe <= ansicht.sterne.tiefe}>{k.tiefe}</span><small>Tiefe</small></div>
  </div>
{/snippet}

<SteuerungsView
  {detail}
  welt="Takt"
  symbol="fa-clock"
  planTitel="Zeitverlauf"
  planHinweis="Klick springt zum Takt"
  takt={0.6}
  live
  ladeAnsicht={(id) => spielApi.taktPlan(id)}
  probieren={(id, code) => spielApi.taktLauf(id, code)}
  mitteTitel={(code) => {
    const [ff, gatter] = bausteineIm(code);
    return `Schaltplan, ${ff} ${ff === 1 ? 'Flipflop' : 'Flipflops'}, ${gatter} ${gatter === 1 ? 'Baustein' : 'Bausteine'}`;
  }}
  zeitText={(zeit, dauer) => `Takt ${zeit} von ${dauer}`}
  stelleText={(stelle) => `Takt ${stelle}`}
  mitUnfall={(_: TaktKennzahlen) => false}
  {hilfe}
  {editor}
  {szene}
  {plan}
  {kennzahlen}
/>

<style>
  .takt-leiste {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: var(--sp-2);
    flex-shrink: 0;
  }
  .eingaben {
    display: flex;
    gap: var(--sp-2);
    font: 600 var(--fs-sm) var(--mono);
    color: var(--fg-dim);
  }
  .eingaben .an { color: var(--accent); }
  .stand-rahmen {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: var(--sp-3);
    flex-shrink: 0;
    padding: var(--sp-2) var(--sp-3);
    border: 1px solid var(--border);
    background: var(--bg);
  }
  .paar {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2px;
    font-size: var(--fs-xs);
    color: var(--fg-dim);
  }
  .gross {
    font-size: 34px;
    font-weight: 700;
    color: var(--accent);
    min-width: 1.4ch;
    text-align: center;
  }
  .gross.falsch { color: var(--red); }
  .bits {
    font-size: var(--fs-sm);
    color: var(--fg-dim);
  }
  .soll-wert {
    margin-left: auto;
    text-align: right;
    font-size: var(--fs-sm);
    color: var(--fg-dim);
  }
  .soll-wert b {
    display: block;
    font-size: 20px;
    color: var(--gold);
  }
  .lampe-paar {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2px;
    font-size: var(--fs-sm);
  }
  .lampe-paar small { color: var(--fg-dim); }
  .lampe {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: #2b3038;
    border: 1px solid var(--border-strong);
  }
  .lampe.an {
    background: #fbbf24;
    box-shadow: 0 0 8px #fbbf24;
  }
  .lampe.falsch { outline: 2px solid var(--red); outline-offset: 2px; }
</style>
