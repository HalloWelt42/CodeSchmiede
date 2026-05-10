/*
 * Theme-Manager. Drei Modi: 'auto' (folgt System), 'dark', 'light'.
 * Persistierung in localStorage, Anwendung ueber data-theme am <html>.
 */

type Modus = 'auto' | 'dark' | 'light';

const SCHLUESSEL = 'codeschmiede.theme';

class ThemeStore {
  modus = $state<Modus>('dark');

  init(): void {
    const gespeichert = localStorage.getItem(SCHLUESSEL) as Modus | null;
    if (gespeichert === 'dark' || gespeichert === 'light' || gespeichert === 'auto') {
      this.modus = gespeichert;
    }
    this.anwenden();

    window
      .matchMedia('(prefers-color-scheme: light)')
      .addEventListener('change', () => {
        if (this.modus === 'auto') this.anwenden();
      });
  }

  setze(modus: Modus): void {
    this.modus = modus;
    localStorage.setItem(SCHLUESSEL, modus);
    this.anwenden();
  }

  toggle(): void {
    this.setze(this.modus === 'dark' ? 'light' : 'dark');
  }

  private anwenden(): void {
    const effektiv =
      this.modus === 'auto'
        ? window.matchMedia('(prefers-color-scheme: light)').matches
          ? 'light'
          : 'dark'
        : this.modus;
    document.documentElement.dataset.theme = effektiv;
  }
}

export const theme = new ThemeStore();
