<script lang="ts">
  /*
   * Kurztest zum Überspringen eines Kapitels: eigene Fragen nacheinander, dazu eine Übung, die alles aus dem
   * Kapitel braucht. Bestanden, wenn alles stimmt; das Kapitel gilt dann als erledigt.
   */
  import { kursApi, type Antwort, type KurztestSicht, type Urteil } from '../../api/KursApi';
  import { route } from '../../stores/RouteStore.svelte';
  import { kursStore } from '../../stores/KursStore.svelte';
  import FrageBlock from './FrageBlock.svelte';

  interface Props {
    id: string;
  }
  let { id }: Props = $props();

  let test = $state<KurztestSicht | null>(null);
  let fehler = $state<string | null>(null);
  let teil = $state(0);
  let richtig = $state<Record<string, boolean>>({});
  let sprache = $derived(kursStore.kapitel(id) ? (kursStore.kurse.find((k) => kursStore.alleKapitel(k).some((x) => x.einfuehrung === id))?.sprache ?? 'python') : 'python');

  async function laden() {
    try {
      test = await kursApi.kurztest(id);
      if (test.bestanden) void kursStore.laden(true);
      else void kursStore.laden();
      const offen = test.fragen.findIndex((f) => !f.richtig);
      teil = offen >= 0 ? offen : test.fragen.length;
    } catch (e) {
      fehler = e instanceof Error ? e.message : String(e);
    }
  }
  $effect(() => {
    void id;
    void laden();
  });

  let anzahl = $derived(test ? test.fragen.length + 1 : 0);
  const istRichtig = (fid: string) => !!(richtig[fid] || test?.fragen.find((f) => f.id === fid)?.richtig);
  const senden = (a: Antwort) => kursApi.kurztestAntworten(id, a);
  function beiUrteil(fid: string, u: Urteil) {
    if (!u.richtig) return;
    richtig[fid] = true;
    setTimeout(() => {
      if (test && teil < test.fragen.length) teil += 1;
    }, 1400);
  }
  let frage = $derived(test && teil < test.fragen.length ? test.fragen[teil] : null);
  const ART: Record<string, string> = { auswahl: 'Auswahl', luecke: 'Lücke im Code', ordnen: 'Zeilen ordnen', fehlerstelle: 'Fehlerstelle zeigen' };
</script>

<div class="seite" data-sprache={sprache}>
  <header class="a-kopf">
    <button class="ikon" onclick={() => route.setze('kurs')} aria-label="Zur Kursübersicht"><i class="fa-solid fa-arrow-left" aria-hidden="true"></i></button>
    <span class="zelle-titel"><b>Kurztest: {test?.titel ?? ''}</b><span>Wer alles richtig hat, überspringt das Kapitel</span></span>
    {#if test}
      <div class="meta"><div class="test-fortschritt" style="width:200px">
        {#each test.fragen as f, i (f.id)}<span class:ok={istRichtig(f.id)} class:jetzt={i === teil}></span>{/each}
        <span class:ok={test.uebung.geloest} class:jetzt={teil === test.fragen.length}></span>
      </div></div>
    {/if}
  </header>

  {#if fehler}
    <div class="rollfeld"><div class="erklaerung schlecht"><i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i><span>{fehler}</span></div></div>
  {:else if test}
    <div class="test-seite">
      <section class="spalte">
        <div class="rollfeld lesen"><div class="lesen-innen">
          <div class="dachzeile">Teil {teil + 1} von {anzahl}: {frage ? ART[frage.frageart] : 'Kleine Übung'}</div>
          {#if frage}
            {#key frage.id}
              <FrageBlock element={frage.id} {sprache} {frage} {senden} beiUrteil={(u) => beiUrteil(frage.id, u)} />
            {/key}
          {:else}
            <h2>{test.uebung.titel}</h2>
            <p>Zum Schluss eine kleine Übung, die alles aus dem Kapitel braucht. Sie öffnet sich wie jede Aufgabe; ist sie gelöst, kommst du hierher zurück.</p>
            <div class="weiter-zeile">
              <button class="knopf voll" onclick={() => route.setze('aufgabe', test!.uebung.id)}><i class="fa-solid fa-code" aria-hidden="true"></i>{test.uebung.geloest ? 'Übung ansehen' : 'Übung lösen'}</button>
            </div>
          {/if}
        </div></div>
      </section>
      <section class="spalte">
        <div class="spalten-kopf"><span>{anzahl} Teile</span></div>
        <div class="rollfeld">
          <div class="test-teile">
            {#each test.fragen as f, i (f.id)}
              <button class="test-teil" class:ok={istRichtig(f.id)} class:jetzt={i === teil} onclick={() => (teil = i)}>
                <i class="fa-solid {istRichtig(f.id) ? 'fa-circle-check' : 'fa-circle-question'}" aria-hidden="true"></i><span>{ART[f.frageart]}</span><small>{istRichtig(f.id) ? 'richtig' : i === teil ? 'jetzt' : ''}</small>
              </button>
            {/each}
            <button class="test-teil" class:ok={test.uebung.geloest} class:jetzt={teil === test.fragen.length} onclick={() => (teil = test!.fragen.length)}>
              <i class="fa-solid {test.uebung.geloest ? 'fa-circle-check' : 'fa-code'}" aria-hidden="true"></i><span>Kleine Übung</span><small>{test.uebung.geloest ? 'gelöst' : ''}</small>
            </button>
          </div>
          <p class="dim" style="font-size:var(--fs-sm);font-family:var(--quick);margin-top:var(--sp-3)">Eigene Fragen, nicht die aus der Einführung. Bestanden nur, wenn alles stimmt; die Einführung bleibt danach trotzdem lesbar.</p>
          {#if test.bestanden}
            <div class="belohnung" style="margin:0">
              <div class="belohnung-kopf"><span class="plus"><i class="fa-solid fa-forward" aria-hidden="true"></i></span><span>Bestanden: das Kapitel gilt als erledigt</span></div>
              <button class="knopf primaer" onclick={() => route.setze('kurs')}><i class="fa-solid fa-arrow-right" aria-hidden="true"></i>Zur Kursübersicht</button>
            </div>
          {:else if test.fragen.every((f) => istRichtig(f.id)) && !test.uebung.geloest}
            <div class="erklaerung gut"><i class="fa-solid fa-circle-check" aria-hidden="true"></i><span>Alle Fragen richtig. Fehlt nur noch die Übung.</span></div>
          {/if}
        </div>
      </section>
    </div>
  {/if}
</div>

<style>
  .test-teil { width: 100%; text-align: left; color: var(--fg); font: inherit; font-size: var(--fs-sm); cursor: pointer; }
  .test-teil:hover:not(:disabled) { color: var(--fg); background: var(--bg-card); }
</style>
