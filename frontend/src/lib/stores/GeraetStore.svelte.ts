/*
 * GeraetStore -- entscheidet an genau einer Stelle, ob die Telefonansicht
 * gilt. Die Rechneransicht nimmt keine Rücksicht auf Telefone und
 * umgekehrt; geteilt werden nur Daten und Inhalte.
 *
 * Das Ergebnis steht zusätzlich als data-geraet am <html>, damit globale
 * Stile (Schriftgrößen) ohne Prop-Weitergabe folgen können.
 */

const TELEFON_ABFRAGE = '(max-width: 640px)';

class GeraetStore {
  private abfrage = window.matchMedia(TELEFON_ABFRAGE);
  telefon = $state(this.abfrage.matches);

  init(): () => void {
    const setze = (): void => {
      this.telefon = this.abfrage.matches;
      document.documentElement.dataset.geraet = this.telefon ? 'telefon' : 'rechner';
    };
    setze();
    this.abfrage.addEventListener('change', setze);
    return () => this.abfrage.removeEventListener('change', setze);
  }
}

export const geraet = new GeraetStore();
