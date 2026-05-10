/*
 * LayoutStore -- Sidebar-Toggle und Spaltenbreiten der Aufgaben-Detail-
 * Ansicht. Persistierung in localStorage. Spaltenbreiten werden als
 * Anteile (Summe = 1) gehalten, damit die Aufteilung bei
 * unterschiedlichen Fensterbreiten konsistent bleibt.
 */

const SIDEBAR_SCHLUESSEL = 'codeschmiede.sidebar_offen';
const SPALTEN_SCHLUESSEL = 'codeschmiede.detail_spalten';

const STANDARD_SPALTEN: [number, number, number] = [1 / 3, 1 / 3, 1 / 3];
const MIN_ANTEIL = 0.12;

class LayoutStore {
  sidebarOffen = $state(true);
  detailSpalten = $state<[number, number, number]>([...STANDARD_SPALTEN]);

  init(): void {
    const sb = localStorage.getItem(SIDEBAR_SCHLUESSEL);
    if (sb !== null) {
      this.sidebarOffen = sb === '1';
    }
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

  toggleSidebar(): void {
    this.sidebarOffen = !this.sidebarOffen;
    localStorage.setItem(SIDEBAR_SCHLUESSEL, this.sidebarOffen ? '1' : '0');
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
