<script lang="ts">
  /*
   * Anmeldung und erste Einrichtung, ohne Navigation (Entwurf
   * mockups/rechner-anmeldung.html und telefon-anmeldung.html).
   * Anmelden mit Name und Passwort der Kellerwolke oder ein Gerät mit
   * einem Code aus der Kellerwolke koppeln; als Web-App am Telefon ist
   * Koppeln vorgewählt (jede Web-App hat ihren eigenen Speicher).
   */
  import { zugang, alsWebApp } from '../stores/ZugangStore.svelte';
  import { geraet } from '../stores/GeraetStore.svelte';
  import { theme } from '../stores/ThemeStore.svelte';

  let weg = $state<'passwort' | 'code'>(alsWebApp() ? 'code' : 'passwort');
  let kennung = $state('');
  let passwort = $state('');
  let code = $state('');
  let geraetename = $state(vorschlagGeraet());
  let adresse = $state('');
  let schluessel = $state('');
  let einrichtungscode = $state('');
  let laeuft = $state(false);
  let fehler = $state<string | null>(null);

  function vorschlagGeraet(): string {
    const ua = navigator.userAgent;
    const name = /iPhone/.test(ua) ? 'iPhone' : /iPad/.test(ua) ? 'iPad' : /Android/.test(ua) ? 'Android' : /Mac/.test(ua) ? 'Mac' : 'Rechner';
    return `${name}, ${alsWebApp() ? 'Web-App' : 'Browser'}`;
  }

  async function ausfuehren(aktion: () => Promise<void>): Promise<void> {
    laeuft = true;
    fehler = null;
    try {
      await aktion();
      passwort = '';
    } catch (e) {
      fehler = (e as Error).message;
    } finally {
      laeuft = false;
    }
  }

  function absenden(e: SubmitEvent): void {
    e.preventDefault();
    if (zugang.stand === 'einrichtung') {
      void ausfuehren(() => zugang.einrichten(adresse, schluessel, einrichtungscode));
    } else if (weg === 'passwort') {
      void ausfuehren(() => zugang.anmelden(kennung, passwort));
    } else {
      void ausfuehren(() => zugang.koppeln(code, geraetename));
    }
  }

  // Die Adresse, die der Server kennt, kommt erst mit seinen Angaben
  $effect(() => {
    if (!adresse && zugang.info?.kellerwolke) adresse = zugang.info.kellerwolke;
  });

  let moeglich = $derived(
    zugang.stand === 'einrichtung'
      ? adresse.trim() !== '' && schluessel.trim() !== ''
      : weg === 'passwort' ? kennung.trim() !== '' && passwort !== '' : code.trim() !== '' && geraetename.trim() !== '',
  );
</script>

<div class="rahmen" data-rahmen={geraet.telefon ? 'app' : undefined}>
  <header class={geraet.telefon ? 't-kopf' : 'topbar'} data-rahmen={geraet.telefon ? 'kopf' : undefined}>
    <div class="marke"><i class="fa-solid fa-hammer" aria-hidden="true"></i>Codeschmiede</div>
    <button class="ikon rechts" onclick={() => theme.toggle()} aria-label="Theme wechseln">
      <i class="fa-solid {theme.modus === 'dark' ? 'fa-sun' : 'fa-moon'}" aria-hidden="true"></i>
    </button>
  </header>

  <main class="zugang" data-rahmen={geraet.telefon ? 'inhalt' : undefined}>
    {#if zugang.stand === 'laden'}
      <p class="dim">Lade ...</p>
    {:else if zugang.stand === 'fehler'}
      <section class="zugang-karte">
        <h1>Server nicht erreichbar</h1>
        <p class="unter">{zugang.fehler}</p>
        <button class="knopf voll" onclick={() => zugang.pruefen()}><i class="fa-solid fa-rotate" aria-hidden="true"></i>Erneut versuchen</button>
      </section>
    {:else if zugang.stand === 'einrichtung'}
      <form class="zugang-karte" onsubmit={absenden}>
        <h1>Erste Einrichtung</h1>
        <p class="unter">Die Codeschmiede braucht einen App-Schlüssel der Kellerwolke. Wer ihn besitzt, darf die App nutzen.</p>
        <label class="feld">Adresse der Kellerwolke<input class="eingabe mono" bind:value={adresse} placeholder="https://..." autocomplete="url" /></label>
        <label class="feld">App-Schlüssel<input class="eingabe mono" type="password" bind:value={schluessel} placeholder="kw_app_..." autocomplete="off" /></label>
        {#if zugang.info?.einrichtungscode}
          <label class="feld">Einrichtungscode<input class="eingabe mono" bind:value={einrichtungscode} placeholder="XXXX-XXXX-XXXX-XXXX" autocomplete="off" /></label>
        {/if}
        {#if fehler}<p class="hinweis-box fehler"><i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i>{fehler}</p>{/if}
        <p class="zugang-fuss">
          {#if zugang.info?.einrichtungscode}Den Code findest du am Rechner der App in <code>{zugang.info.einrichtungscode}</code>.{/if}
          Den App-Schlüssel stellst du in der Kellerwolke aus: Menü am Namen, Zugänge, Name der App eintragen, Schlüssel ausstellen.
        </p>
        <button class="knopf voll" type="submit" disabled={laeuft || !moeglich}>
          <i class="fa-solid {laeuft ? 'fa-spinner fa-spin' : 'fa-plug'}" aria-hidden="true"></i>Einrichten
        </button>
      </form>
    {:else}
      <form class="zugang-karte" onsubmit={absenden}>
        <h1>Anmelden</h1>
        <p class="unter">Mit deinem Konto der Kellerwolke unter <code>{zugang.info?.kellerwolke}</code></p>
        <div class="segment">
          <button type="button" class:aktiv={weg === 'passwort'} onclick={() => (weg = 'passwort')}><i class="fa-solid fa-key" aria-hidden="true"></i>Passwort</button>
          <button type="button" class:aktiv={weg === 'code'} onclick={() => (weg = 'code')}><i class="fa-solid fa-link" aria-hidden="true"></i>Gerät koppeln</button>
        </div>
        {#if weg === 'passwort'}
          <label class="feld">Name<input class="eingabe" bind:value={kennung} autocomplete="username" /></label>
          <label class="feld">Passwort<input class="eingabe" type="password" bind:value={passwort} autocomplete="current-password" /></label>
        {:else}
          <label class="feld">Code aus der Kellerwolke<input class="eingabe mono" bind:value={code} placeholder="ABCD-EFGH" autocomplete="one-time-code" /></label>
          <label class="feld">Name dieses Geräts<input class="eingabe" bind:value={geraetename} /></label>
        {/if}
        {#if fehler || zugang.fehler}
          <p class="hinweis-box fehler"><i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i>{fehler ?? zugang.fehler}</p>
        {/if}
        <button class="knopf voll" type="submit" disabled={laeuft || !moeglich}>
          <i class="fa-solid {laeuft ? 'fa-spinner fa-spin' : weg === 'passwort' ? 'fa-right-to-bracket' : 'fa-link'}" aria-hidden="true"></i>
          {weg === 'passwort' ? 'Anmelden' : 'Koppeln'}
        </button>
        <p class="zugang-fuss">Am Telefon als Web-App einmal koppeln: Code in der Kellerwolke am Rechner unter Menü am Namen, Geräte.</p>
      </form>
    {/if}
  </main>
</div>

<style>
  .rahmen {
    flex: 1;
    min-height: 0;
    display: flex;
    flex-direction: column;
  }
  .topbar {
    flex: none;
    height: var(--kopf-h);
    display: flex;
    align-items: center;
    gap: var(--sp-3);
    padding: 0 var(--sp-3);
    background: var(--bg-card);
    border-bottom: 1px solid var(--border);
  }
  /* am Telefon Höhe und sicherer Rand aus dem Rahmen des Appkerns (data-rahmen) */
  .t-kopf {
    display: flex;
    align-items: center;
    padding-inline: var(--rahmen-rand);
    background: var(--bg-card);
    border-bottom: 1px solid var(--border);
  }
  .marke {
    display: flex;
    align-items: center;
    gap: var(--sp-2);
    font-size: var(--fs-lg);
    font-weight: 600;
  }
  .marke i { color: var(--accent); }
  .rechts { margin-left: auto; }
</style>
