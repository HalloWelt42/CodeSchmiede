<script lang="ts">
  /*
   * Einführung am Rechner: links die Gliederung, in der Mitte der Lesetext Abschnitt für Abschnitt, rechts die
   * Werkbank mit dem Beispiel des Abschnitts. Weiter geht es, wenn alle Fragen des Abschnitts richtig beantwortet
   * sind; nach dem letzten Abschnitt folgt das Kapitelende mit "Kann ich jetzt" und den Übungen.
   */
  import { kursApi, type Antwort, type BeispielTeil, type EinfuehrungSicht, type KapitelSicht, type Urteil } from '../../api/KursApi';
  import { route } from '../../stores/RouteStore.svelte';
  import { kursStore } from '../../stores/KursStore.svelte';
  import TeilAnzeige from './TeilAnzeige.svelte';
  import Werkbank from './Werkbank.svelte';
  import KapitelEnde from './KapitelEnde.svelte';

  interface Props {
    id: string;
  }
  let { id }: Props = $props();

  let e = $state<EinfuehrungSicht | null>(null);
  let fehler = $state<string | null>(null);
  let nummer = $state(1);
  let ende = $state(false);
  let beispielId = $state<string | null>(null);
  let beantwortet = $state<Record<string, boolean>>({});
  let richtig = $state<Record<string, boolean>>({});

  async function laden() {
    try {
      e = await kursApi.einfuehrung(id);
      const offen = e.abschnitte.find((a) => !a.fertig);
      ende = !offen;
      nummer = offen?.nummer ?? e.abschnitte.length;
      void kursStore.laden();
    } catch (err) {
      fehler = err instanceof Error ? err.message : String(err);
    }
  }
  $effect(() => {
    void id;
    void laden();
  });

  let abschnitt = $derived(e?.abschnitte.find((a) => a.nummer === nummer) ?? null);
  let beispiele = $derived((abschnitt?.teile.filter((t) => t.art === 'beispiel') ?? []) as BeispielTeil[]);
  let beispiel = $derived(beispiele.find((b) => b.id === beispielId) ?? beispiele[0] ?? null);
  let kapitel = $derived<KapitelSicht | null>(kursStore.kapitel(id));

  function istBeantwortet(b: BeispielTeil): boolean {
    return !b.vorhersage || b.vorhersage.beantwortet || !!beantwortet[b.id];
  }
  let fragenRichtig = $derived(
    (abschnitt?.teile ?? []).every((t) => t.art !== 'frage' || t.frage.richtig || richtig[t.frage.id]),
  );

  const senden = (a: Antwort) => kursApi.antworten(id, a);
  function beiUrteil(element: string, u: Urteil) {
    beantwortet[element] = true;
    if (u.richtig) richtig[element] = true;
  }

  async function weiter() {
    if (!e || !abschnitt) return;
    try {
      e = await kursApi.abschnittFertig(id, abschnitt.nummer);
      const naechster = e.abschnitte.find((a) => a.nummer > nummer && !a.fertig) ?? e.abschnitte.find((a) => !a.fertig);
      if (naechster) {
        nummer = naechster.nummer;
        beispielId = null;
      } else {
        ende = true;
        void kursStore.laden(true);
      }
      document.querySelector('.lesen')?.scrollTo({ top: 0 });
    } catch (err) {
      fehler = err instanceof Error ? err.message : String(err);
    }
  }

  function gehe(n: number) {
    nummer = n;
    ende = false;
    beispielId = null;
    document.querySelector('.lesen')?.scrollTo({ top: 0 });
  }
</script>

<div class="seite" data-sprache={e?.sprache ?? 'python'}>
  <header class="a-kopf">
    <button class="ikon" onclick={() => route.setze('kurs')} aria-label="Zur Kursübersicht"><i class="fa-solid fa-arrow-left" aria-hidden="true"></i></button>
    <span class="zelle-titel">
      <b>{e?.titel ?? 'Einführung'}</b>
      {#if e}<span>{kursStore.sprachTitel(e.sprache)}-Kurs{e.kapitel ? `, Kapitel ${e.kapitel}` : ''}: {ende ? 'Kapitelende' : `Einführung, Abschnitt ${nummer} von ${e.abschnitte.length}`}</span>{/if}
    </span>
    <div class="meta">
      {#if e}
        <div class="t-abschnitte" style="width:150px">
          {#each e.abschnitte as a (a.nummer)}<span class:fertig={a.fertig} class:jetzt={!ende && a.nummer === nummer && !a.fertig}></span>{/each}
        </div>
      {/if}
      <button class="knopf" onclick={() => route.setze('merkblatt', id)}><i class="fa-solid fa-note-sticky" aria-hidden="true"></i>Merkblatt</button>
    </div>
  </header>

  {#if fehler}
    <div class="rollfeld"><div class="erklaerung schlecht"><i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i><span>{fehler}</span></div></div>
  {:else if e}
    <div class="lehr-seite">
      <section class="spalte gliederung-spalte">
        <div class="spalten-kopf"><span>Einführung</span></div>
        <div class="rollfeld">
          <div class="gliederung">
            {#each e.abschnitte as a (a.nummer)}
              {@const erreichbar = a.fertig || e.abschnitte.filter((x) => x.nummer < a.nummer).every((x) => x.fertig)}
              <button class:fertig={a.fertig} class:jetzt={!ende && a.nummer === nummer} class:zu={!erreichbar} disabled={!erreichbar} onclick={() => gehe(a.nummer)}>
                <i class="fa-{a.fertig ? 'solid fa-circle-check' : !ende && a.nummer === nummer ? 'solid fa-circle-play' : 'regular fa-circle'}" aria-hidden="true"></i><span>{a.titel}</span>
              </button>
            {/each}
          </div>
          <div class="gruppe" style="margin-top:var(--sp-4)">Danach</div>
          <div class="gliederung">
            <button class:jetzt={ende} disabled={!e.abschnitte.every((a) => a.fertig)} onclick={() => (ende = true)}><i class="fa-solid fa-id-card" aria-hidden="true"></i><span>Kann ich jetzt</span></button>
            {#if kapitel?.kurztest}<button onclick={() => route.setze('kurztest', id)}><i class="fa-solid fa-forward" aria-hidden="true"></i><span>Kurztest</span></button>{/if}
          </div>
        </div>
      </section>

      <section class="spalte">
        <div class="rollfeld lesen">
          <div class="lesen-innen">
            {#if ende}
              <KapitelEnde einfuehrung={e} {kapitel} />
            {:else if abschnitt}
              <div><div class="dachzeile">Abschnitt {abschnitt.nummer} von {e.abschnitte.length}</div><h2>{abschnitt.titel}</h2></div>
              {#each abschnitt.teile as teil, i (`${abschnitt.nummer}-${i}`)}
                <TeilAnzeige {teil} sprache={e.sprache} {senden} {beiUrteil} beispielWaehlen={(b) => (beispielId = b)} gewaehltesBeispiel={beispiel?.id ?? null} />
              {/each}
              <div class="weiter-zeile">
                {#if nummer > 1}<button class="knopf" onclick={() => gehe(nummer - 1)}><i class="fa-solid fa-arrow-left" aria-hidden="true"></i>Abschnitt {nummer - 1}</button>{/if}
                <button class="knopf voll" disabled={!fragenRichtig} onclick={weiter}>
                  <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>{nummer < e.abschnitte.length ? `Weiter: ${e.abschnitte[nummer].titel}` : 'Kapitel abschließen'}
                </button>
              </div>
              {#if !fragenRichtig}<span class="dim" style="font-size:var(--fs-sm);text-align:right">Weiter geht es, wenn die Fragen dieses Abschnitts richtig beantwortet sind.</span>{/if}
            {/if}
          </div>
        </div>
      </section>

      <section class="spalte werkbank">
        <div class="spalten-kopf"><span>Werkbank</span>{#if beispiele.length > 1}<span class="dim" style="margin-left:auto;text-transform:none;letter-spacing:0">Beispiel {beispiele.indexOf(beispiel as BeispielTeil) + 1} von {beispiele.length}</span>{/if}</div>
        <div class="rollfeld">
          {#if beispiel && !ende}
            {#key beispiel.id}
              <Werkbank einfuehrung={id} {beispiel} sprache={e.sprache} gesperrt={!istBeantwortet(beispiel)} />
            {/key}
          {:else}
            <p class="dim" style="font-family:var(--quick)">{ende ? 'Die Übungen warten.' : 'In diesem Abschnitt gibt es nichts auszuführen.'}</p>
          {/if}
        </div>
      </section>
    </div>
  {/if}
</div>
