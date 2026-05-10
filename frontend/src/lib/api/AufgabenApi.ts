import { HttpBase } from './HttpBase';
import type { AufgabeDetail, AufgabeKurz, Musterloesung } from '../types/Aufgabe';
import type { ProgressEintrag } from './ProgressApi';

export interface LetzteSubmission {
  code: string | null;
  bestanden: boolean | null;
  zeitstempel: string | null;
}

export class AufgabenApi extends HttpBase {
  constructor() {
    super('/api/aufgaben');
  }

  liste(): Promise<AufgabeKurz[]> {
    return this.get<AufgabeKurz[]>('');
  }

  detail(id: string): Promise<AufgabeDetail> {
    return this.get<AufgabeDetail>(`/${id}`);
  }

  musterloesungen(id: string): Promise<Musterloesung[]> {
    return this.get<Musterloesung[]>(`/${id}/musterloesungen`);
  }

  hintGeoeffnet(aufgabeId: string, hintIndex: number): Promise<ProgressEintrag> {
    return this.post<ProgressEintrag>(`/${aufgabeId}/hints/${hintIndex}`, {});
  }

  letzteSubmission(aufgabeId: string): Promise<LetzteSubmission> {
    return this.get<LetzteSubmission>(`/${aufgabeId}/letzte-submission`);
  }
}

export const aufgabenApi = new AufgabenApi();
