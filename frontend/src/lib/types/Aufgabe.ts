export type Schwierigkeit = 'anfaenger' | 'mittel' | 'fortgeschritten' | 'experte';

export interface AufgabeKurz {
  id: string;
  titel: string;
  sprache: string;
  schwierigkeit: Schwierigkeit;
  schwierigkeit_score: number;
  schaetz_minuten: number;
  tags: string[];
  pfade: string[];
}

export interface PfadKurz {
  id: string;
  titel: string;
  beschreibung: string;
  reihenfolge: string[];
}
