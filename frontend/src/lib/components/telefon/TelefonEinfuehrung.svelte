<script lang="ts">
  /*
   * Einführung am Telefon: eine Spalte, Abschnitt für Abschnitt. Lesen, vorhersagen, Fragen beantworten, Beispiele
   * unverändert ausführen und den Ablauf abspielen; verändern und üben geht am Rechner (das Telefon ist Unterstützung).
   */
  import { kursApi, type Antwort, type EinfuehrungSicht, type Urteil } from '../../api/KursApi';
  import { route } from '../../stores/RouteStore.svelte';
  import { kursStore } from '../../stores/KursStore.svelte';
  import TeilAnzeige from '../kurs/TeilAnzeige.svelte';
  import KvWerkbank from '../kurs/KvWerkbank.svelte';
  import Werkbank from '../kurs/Werkbank.svelte';
  import FrageBlock from '../kurs/FrageBlock.svelte';

  interface Props {
    id: string;
  }
  let { id }: Props = $props();

  let e = $state<EinfuehrungSicht | null>(null);
  let fehler = $state<string | null>(null);
  let nummer = $state(1);
  let ende = $state(false);
  let beantwortet = $state<Record<string, boolean>>({});
  let richtig = $state<Record<string, boolean>>({});
  let feld: HTMLDivElement | undefined = $state();

  $effect(() => {
    void id;
    kursApi.einfuehrung(id).then(
      (x) => {
        e = x;
        const offen = x.abschnitte.find((a) => !a.fertig);
        ende = !offen;
        nummer = offen?.nummer ?? x.abschnitte.length;
      },
      (err: unknown) => (fehler = err instanceof Error ? err.message : String(err)),
    );
    void kursStore.laden();
  });

  let abschnitt = $derived(e?.abschnitte.find((a) => a.nummer === nummer) ?? null);
  let fragenRichtig = $derived((abschnitt?.teile ?? []).every((t) => t.art !== 'frage' || t.frage.richtig || richtig[t.frage.id]));
  const senden = (a: Antwort) => kursApi.antworten(id, a);
  function beiUrteil(element: string, u: Urteil) {
    beantwortet[element] = true;
    if (u.richtig) richtig[element] = true;
  }

  async function weiter() {
    if (!abschnitt) return;
    try {
      e = await kursApi.abschnittFertig(id, abschnitt.nummer);
      const naechster = e.abschnitte.find((a) => !a.fertig);
      if (naechster) nummer = naechster.nummer;
      else {
        ende = true;
        void kursStore.laden(true);
      }
      feld?.scrollTo({ top: 0 });
    } catch (err) {
      fehler = err instanceof Error ? err.message : String(err);
    }
  }
</script>

<div class="seite" data-sprache={e?.sprache ?? 'python'}>
  <header class="seiten-kopf">
    <div class="titelzeile">
      <button class="ikon" onclick={() => route.setze('kurs')} aria-label="Zur Kursübersicht"><i class="fa-solid fa-arrow-left" aria-hidden="true"></i></button>
      <span class="zelle-titel"><b>{e?.titel ?? 'Einführung'}</b>{#if e}<span>{e.kapitel ? `Kapitel ${e.kapitel}, ` : ''}{ende ? 'geschafft' : `Abschnitt ${nummer} von ${e.abschnitte.length}`}</span>{/if}</span>
      <button class="ikon" style="margin-left:auto" onclick={() => route.setze('merkblatt', id)} aria-label="Merkblatt"><i class="fa-solid fa-note-sticky" aria-hidden="true"></i></button>
    </div>
    {#if e}<div class="t-abschnitte">{#each e.abschnitte as a (a.nummer)}<span class:fertig={a.fertig} class:jetzt={!ende && a.nummer === nummer && !a.fertig}></span>{/each}</div>{/if}
  </header>

  <div class="rollfeld lesen" bind:this={feld}>
    {#if fehler}
      <div class="erklaerung schlecht"><i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i><span>{fehler}</span></div>
    {:else if e && ende}
      <div class="lesen-innen">
        <h2>{e.titel} geschafft</h2>
        <div class="block"><div class="block-kopf"><span>Das kannst du jetzt</span></div>
          <ul class="lernziele">{#each e.lernziele as z (z)}<li><i class="fa-solid fa-check" aria-hidden="true"></i><span>{z}</span></li>{/each}</ul></div>
        <p class="dim">Die Übungen warten am Rechner.</p>
        <div class="block"><div class="block-kopf"><span>Nochmal lesen</span></div>
          <div class="schritt-liste">
            {#each e.abschnitte as a (a.nummer)}
              <button class="schritt nachlesen" onclick={() => { nummer = a.nummer; ende = false; feld?.scrollTo({ top: 0 }); }}><span class="nr">{a.nummer}</span><span class="t">{a.titel}</span><i class="fa-solid fa-chevron-right" aria-hidden="true"></i></button>
            {/each}
          </div>
        </div>
      </div>
    {:else if e && abschnitt}
      <div class="lesen-innen">
        <h2>{abschnitt.titel}</h2>
        {#each abschnitt.teile as teil, i (`${abschnitt.nummer}-${i}`)}
          {#if teil.art === 'beispiel'}
            {@const b = teil}
            <Werkbank einfuehrung={id} beispiel={b} sprache={e.sprache} bearbeitbar={false}
              gesperrt={!!b.vorhersage && !b.vorhersage.beantwortet && !beantwortet[b.id]}>
              {#snippet vorAusfuehren()}
                {#if b.vorhersage}<FrageBlock element={b.id} sprache={e!.sprache} vorhersage={b.vorhersage} {senden} beiUrteil={(u) => beiUrteil(b.id, u)} />{/if}
              {/snippet}
            </Werkbank>
          {:else if teil.art === 'kv'}
            <KvWerkbank {teil} />
          {:else}
            <TeilAnzeige {teil} sprache={e.sprache} {senden} {beiUrteil} />
          {/if}
        {/each}
      </div>
    {/if}
  </div>
  {#if e && !ende}
    <div class="t-unten">
      <button class="knopf" disabled={nummer <= 1} onclick={() => { nummer -= 1; feld?.scrollTo({ top: 0 }); }}><i class="fa-solid fa-arrow-left" aria-hidden="true"></i>Zurück</button>
      <button class="knopf voll" disabled={!fragenRichtig} onclick={weiter}><i class="fa-solid fa-arrow-right" aria-hidden="true"></i>Weiter</button>
    </div>
  {/if}
</div>

<style>
  .nachlesen { width: 100%; min-height: 44px; border: 0; background: transparent; color: var(--fg); font: inherit; text-align: left; }
  .nachlesen:hover:not(:disabled) { background: var(--bg-card-2); color: var(--fg); }
</style>
