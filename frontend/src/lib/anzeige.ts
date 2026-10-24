/*
 * Kleine Anzeigehilfen, die Listen am Rechner und am Telefon teilen.
 */
import type { ProgressStatus } from './api/ProgressApi';

export function statusIcon(status: ProgressStatus): string {
  if (status === 'geloest') return 'fa-circle-check';
  if (status === 'in_arbeit') return 'fa-pen-to-square';
  return 'fa-circle';
}

/** CSS-Klasse für Randfarbe und Symbolfarbe einer Zeile */
export function statusKlasse(status: ProgressStatus): string {
  if (status === 'geloest') return 'geloest';
  if (status === 'in_arbeit') return 'arbeit';
  return '';
}
