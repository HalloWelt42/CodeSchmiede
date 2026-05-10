/*
 * Typen für die zentrale Konfiguration. Wird über /api/admin/konfig
 * geladen und im KonfigStore gehalten.
 */

export interface SchwierigkeitsStufe {
  id: string;
  titel: string;
  farbe: string;
  score_max: number;
}

export interface SprachKonfig {
  id: string;
  titel: string;
  editor_lang: string;
  runner_type: string;
}

export interface AufgabentypKonfig {
  id: string;
  titel: string;
  view: string;
  beschreibung: string;
}

export interface Konfiguration {
  schwierigkeiten: SchwierigkeitsStufe[];
  sprachen: SprachKonfig[];
  aufgabentypen: AufgabentypKonfig[];
}

/**
 * Mappt Konfig-Farb-Schluessel auf CSS-Variablen, sodass Theme-Wechsel
 * automatisch funktioniert. Wenn die Farbe kein bekannter Schluessel ist,
 * wird sie als CSS-Wert direkt durchgereicht (z.B. Hex-Code).
 */
export function farbeZuCss(farbe: string): string {
  const map: Record<string, string> = {
    green: 'var(--green)',
    orange: 'var(--orange)',
    red: 'var(--red)',
    accent: 'var(--accent)',
    petrol: 'var(--accent)',
    blau: 'var(--info-blue)',
    info_blue: 'var(--info-blue)',
    grau: 'var(--fg-mute)',
    grey: 'var(--fg-mute)',
  };
  return map[farbe] ?? farbe;
}
