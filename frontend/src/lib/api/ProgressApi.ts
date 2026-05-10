import { HttpBase } from './HttpBase';

export interface GesamtFortschritt {
  aufgaben_gesamt: number;
  aufgaben_geloest: number;
  aufgaben_in_arbeit: number;
  aufgaben_neu: number;
  submissions_gesamt: number;
  bestandene_submissions: number;
  punkte_gesamt: number;
  punkte_maximal: number;
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
  punkte_erreicht: number;
  geloest_am: string | null;
  ease: number;
  intervall_tage: number;
  faellig_am: string | null;
  letzte_wiederholung: string | null;
}

export interface WeiterVorschlag {
  naechste_id: string | null;
  quelle: 'pfad' | 'global' | 'keine';
  pfad_id: string | null;
}

export interface HeatmapTag {
  datum: string;
  submissions: number;
  bestanden: number;
}

export interface HeatmapAntwort {
  tage: HeatmapTag[];
}

export interface Achievement {
  id: string;
  titel: string;
  beschreibung: string;
  icon: string;
  erreicht: boolean;
  fortschritt: number;
  ziel: number;
}

export interface AchievementsAntwort {
  eintraege: Achievement[];
  erreicht_anzahl: number;
  gesamt_anzahl: number;
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
  weiter(aufgabeId: string): Promise<WeiterVorschlag> {
    return this.get<WeiterVorschlag>(`/weiter/${aufgabeId}`);
  }
  reset(aufgabeId: string): Promise<{ status: string; aufgabe_id: string }> {
    return this.request<{ status: string; aufgabe_id: string }>(`/${aufgabeId}`, { method: 'DELETE' });
  }
  resetAlles(): Promise<{ status: string }> {
    return this.post<{ status: string }>('/reset-alles', {});
  }
  heatmap(tage = 90): Promise<HeatmapAntwort> {
    return this.get<HeatmapAntwort>(`/heatmap?tage=${tage}`);
  }
  heatmapJahr(jahr: number): Promise<HeatmapAntwort> {
    return this.get<HeatmapAntwort>(`/heatmap?jahr=${jahr}`);
  }
  achievements(): Promise<AchievementsAntwort> {
    return this.get<AchievementsAntwort>('/achievements');
  }
}

export const progressApi = new ProgressApi();
