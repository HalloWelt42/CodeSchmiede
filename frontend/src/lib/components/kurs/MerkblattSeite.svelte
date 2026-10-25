<script lang="ts">
  /*
   * Merkblatt eines Kapitels auf einer Seite: Grundform aus den Beispielen mit ihrer Ausgabe, Merksätze, typische
   * Fallen und Begriffe. Alles kommt aus der Einführung (eine Wahrheit); zum Nachschlagen und zum Ausdrucken.
   */
  import { kursApi, type MerkblattSicht } from '../../api/KursApi';
  import { markdownRenderer } from '../../markdown/MarkdownRenderer';
  import { route } from '../../stores/RouteStore.svelte';
  import { kursStore } from '../../stores/KursStore.svelte';
  import CodeBlock from './CodeBlock.svelte';

  interface Props {
    id: string;
    /** am Telefon ohne Kopf mit Drucken */
    telefon?: boolean;
  }
  let { id, telefon = false }: Props = $props();

  let blatt = $state<MerkblattSicht | null>(null);
  let fehler = $state<string | null>(null);
  $effect(() => {
    void id;
    kursApi.merkblatt(id).then(
      (m) => (blatt = m),
      (e: unknown) => (fehler = e instanceof Error ? e.message : String(e)),
    );
    void kursStore.laden();
  });
</script>

<div class="seite" data-sprache={blatt?.sprache ?? 'python'}>
  <header class="seiten-kopf">
    <div class="titelzeile">
      <button class="ikon" onclick={() => route.setze('einfuehrung', id)} aria-label="Zur Einführung"><i class="fa-solid fa-arrow-left" aria-hidden="true"></i></button>
      <h1>Merkblatt</h1>
      {#if !telefon}<span class="lead">Das Kapitel auf einer Seite: zum Nachschlagen und zum Ausdrucken</span>
        <div class="aktionen"><button class="knopf" onclick={() => window.print()}><i class="fa-solid fa-print" aria-hidden="true"></i>Drucken</button></div>{/if}
    </div>
  </header>
  <div class="merk-seite">
    {#if fehler}
      <div class="erklaerung schlecht"><i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i><span>{fehler}</span></div>
    {:else if blatt}
      <article class="blatt">
        <header class="blatt-kopf">
          <div class="blatt-bild">{#if blatt.bild?.url}<img src={blatt.bild.url} alt="" />{:else}<i class="fa-solid fa-graduation-cap" aria-hidden="true"></i>{/if}</div>
          <div><small>{kursStore.sprachTitel(blatt.sprache)}-Kurs{blatt.kapitel ? `, Kapitel ${blatt.kapitel}` : ''}</small><h1>{blatt.titel}</h1></div>
          <span class="marke"><i class="fa-solid fa-hammer" aria-hidden="true"></i> Codeschmiede</span>
        </header>
        {#each blatt.beispiele as b, i (i)}
          <section class="feld-merk">
            <h3>{i === 0 ? 'Grundform' : `Beispiel ${i + 1}`}</h3>
            <CodeBlock code={b.code} sprache={blatt.sprache} />
            {#if b.ausgabe}<pre class="ausgabe">{b.ausgabe}</pre>{/if}
          </section>
        {/each}
        {#if blatt.merke.length}
          <section class="feld-merk">
            <h3>Merke</h3>
            <ul class="merk-liste">{#each blatt.merke as m (m)}<li>{@html markdownRenderer.rendere(m)}</li>{/each}</ul>
          </section>
        {/if}
        {#if blatt.fallen.length}
          <section class="feld-merk">
            <h3>Typische Fallen</h3>
            <div class="fallen">{#each blatt.fallen as f (f.titel)}<div class="falle"><b>{f.titel}:</b> {@html markdownRenderer.rendere(f.text)}</div>{/each}</div>
          </section>
        {/if}
        <section class="feld-merk">
          <h3>Danach kannst du</h3>
          <ul class="merk-liste">{#each blatt.lernziele as z (z)}<li>{z}</li>{/each}</ul>
        </section>
        {#if blatt.begriffe.length}
          <section class="feld-merk ganz">
            <h3>Begriffe</h3>
            <div class="begriffe">{#each blatt.begriffe as b (b)}<span>{b}</span>{/each}</div>
          </section>
        {/if}
      </article>
    {/if}
  </div>
</div>

<style>
  .blatt-bild { width: 76px; height: 76px; display: grid; place-items: center; font-size: 34px; color: #8a5a00; }
  .blatt-bild img { width: 100%; height: 100%; object-fit: contain; }
  .merk-liste { margin: 0; padding-left: 18px; display: flex; flex-direction: column; gap: 4px; }
  .merk-liste :global(p), .falle :global(p) { display: inline; margin: 0; }
  .fallen { display: flex; flex-direction: column; gap: 6px; }
  .begriffe { display: flex; flex-wrap: wrap; gap: 6px; }
  .begriffe span { padding: 2px 8px; border: 1px solid #e0dbcf; border-radius: 3px; background: #efece4; font-size: 14px; }
</style>
