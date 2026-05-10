import { HttpBase } from './HttpBase';

export interface GesamtFortschritt {
  aufgaben_gesamt: number;
  aufgaben_geloest: number;
  aufgaben_in_arbeit: number;
  aufgaben_neu: number;
  submissions_gesamt: number;
  bestandene_submissions: number;
}

export interface Streak {
  aktuell: number;
  laengster: number;
  letzter_tag: string | null;
}

export interface Tagesziel {
  datum: string;
  faellige_wiederholungen: string[];
  vorgeschlagene_neue: string | null;
  letzte_aufgabe: string | null;
  streak_aktiv: boolean;
  aktueller_streak: number;
  laengster_streak: number;
}

export type ProgressStatus = 'neu' | 'in_arbeit' | 'geloest';

export interface ProgressEintrag {
  aufgabe_id: string;
  status: ProgressStatus;
  versuche: number;
  hints_genutzt: number;
  geloest_am: string | null;
  ease: number;
  intervall_tage: number;
  faellig_am: string | null;
  letzte_wiederholung: string | null;
}

export class ProgressApi extends HttpBase {
  constructor() {
    super('/api/progress');
  }

  gesamt(): Promise<GesamtFortschritt> {
    return this.get<GesamtFortschritt>('');
  }
  heute(): Promise<Tagesziel> {
    return this.get<Tagesziel>('/heute');
  }
  streak(): Promise<Streak> {
    return this.get<Streak>('/streak');
  }
  alleAufgaben(): Promise<Record<string, ProgressEintrag>> {
    return this.get<Record<string, ProgressEintrag>>('/aufgaben');
  }
}

export const progressApi = new ProgressApi();
