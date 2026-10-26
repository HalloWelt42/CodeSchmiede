/*
 * LayoutStore: breite oder schmale Navigation (nur Symbole) und
 * Spaltenbreiten der Aufgabenansicht. Persistierung in localStorage. Spaltenbreiten werden als
 * Anteile (Summe = 1) gehalten, damit die Aufteilung bei
 * unterschiedlichen Fensterbreiten konsistent bleibt.
 */

const NAV_SCHLUESSEL = 'codeschmiede.sidebar_offen';
/** Ohne gespeicherte Wahl startet die Navigation erst ab dieser Fensterbreite breit, damit der Inhalt Platz hat. */
const NAV_BREIT_AB_PX = 1200;
const SPALTEN_SCHLUESSEL = 'codeschmiede.detail_spalten';

const STANDARD_SPALTEN: [number, number, number] = [1 / 3, 1 / 3, 1 / 3];
const MIN_ANTEIL = 0.12;

class LayoutStore {
  navBreit = $state(true);
  detailSpalten = $state<[number, number, number]>([...STANDARD_SPALTEN]);

  init(): void {
    const nb = localStorage.getItem(NAV_SCHLUESSEL);
    this.navBreit = nb !== null ? nb === '1' : window.innerWidth >= NAV_BREIT_AB_PX;
    const sp = localStorage.getItem(SPALTEN_SCHLUESSEL);
    if (sp) {
      try {
        const werte = JSON.parse(sp);
        if (Array.isArray(werte) && werte.length === 3 && werte.every((w) => typeof w === 'number')) {
          this.detailSpalten = this.normalisiere(werte as [number, number, number]);
        }
      } catch {
        // Eintrag verwerfen, Standard bleibt.
      }
    }
  }

  umschaltenNav(): void {
    this.navBreit = !this.navBreit;
    localStorage.setItem(NAV_SCHLUESSEL, this.navBreit ? '1' : '0');
  }

  setzeSpalten(werte: [number, number, number]): void {
    this.detailSpalten = this.normalisiere(werte);
    localStorage.setItem(SPALTEN_SCHLUESSEL, JSON.stringify(this.detailSpalten));
  }

  resetSpalten(): void {
    this.detailSpalten = [...STANDARD_SPALTEN];
    localStorage.removeItem(SPALTEN_SCHLUESSEL);
  }

  private normalisiere(werte: [number, number, number]): [number, number, number] {
    const begrenzt = werte.map((w) => Math.max(MIN_ANTEIL, w)) as [number, number, number];
    const summe = begrenzt[0] + begrenzt[1] + begrenzt[2];
    return [begrenzt[0] / summe, begrenzt[1] / summe, begrenzt[2] / summe];
  }
}

export const layout = new LayoutStore();
