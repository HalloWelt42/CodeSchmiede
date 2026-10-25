/*
 * Spielmechanik: Stufe, Serie, Tagesauftrag, Meisterschaft und Erfolge.
 * Alles leitet der Server aus Abgaben und Fortschritt ab (docs/SPIELE.md);
 * die Belohnung einer Abgabe kommt mit der Abgabe.
 */
import { HttpBase } from './HttpBase';

export type Rang = 'bronze' | 'silber' | 'gold';
export type ErfolgsGruppe = 'meilensteine' | 'serie' | 'technik' | 'spiele';

export interface StufenStand {
  stufe: number;
  titel: string;
  punkte: number;
  /** Punkte, ab denen die Stufe gilt, und ab denen die nächste gilt */
  ab: number;
  bis: number;
  naechster_titel: string | null;
  naechster_titel_ab_stufe: number | null;
}

export interface SerienStand {
  aktuell: number;
  laengste: number;
  heute_geuebt: boolean;
  schilde: number;
  schilde_max: number;
  /** Tage bis zum nächsten Schutzschild; null, wenn alle da sind */
  naechster_schild_in: number | null;
}

export interface AuftragsZiel {
  id: string;
  text: string;
  erledigt: boolean;
}

export interface Tagesauftrag {
  datum: string;
  ziele: AuftragsZiel[];
  erledigt: boolean;
  bonus: number;
  gutgeschrieben: boolean;
}

export interface BereichStand {
  id: string;
  titel: string;
  punkte: number;
  moeglich: number;
  anteil: number;
  rang: Rang | null;
}

export interface ErfolgStand {
  id: string;
  gruppe: ErfolgsGruppe;
  titel: string;
  beschreibung: string;
  icon: string;
  rang: Rang | null;
  wert: number;
  ziel: number;
  erreicht: boolean;
}

export interface ErfolgsListe {
  eintraege: ErfolgStand[];
  erreicht: number;
  gesamt: number;
}

export interface Spielstand {
  punkte: number;
  stufe: StufenStand;
  serie: SerienStand;
  auftrag: Tagesauftrag;
  meisterschaft: BereichStand[];
}

export interface Bestwert {
  art: 'zeichen' | 'laufzeit' | 'sterne';
  neu: number;
  vorher: number;
}

export interface Belohnung {
  /** Zuwachs der Aufgabe; der beste Versuch zählt */
  punkte: number;
  punkte_versuch: number;
  punkte_moeglich: number;
  hinweise: number;
  aufgegeben: boolean;
  wiederholung: boolean;
  erster_versuch: boolean;
  sterne: number | null;
  stufe_vorher: number;
  stufe: StufenStand;
  neue_erfolge: ErfolgStand[];
  bestwerte: Bestwert[];
  auftrag_bonus: number;
  auftrag: Tagesauftrag;
}

export class SpielApi extends HttpBase {
  constructor() {
    super('/api/spiel');
  }

  stand(): Promise<Spielstand> {
    return this.get<Spielstand>('/stand');
  }
  erfolge(): Promise<ErfolgsListe> {
    return this.get<ErfolgsListe>('/erfolge');
  }
}

export const spielApi = new SpielApi();
