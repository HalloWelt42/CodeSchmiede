import { HttpBase } from './HttpBase';
import type { AufgabeDetail, AufgabeKurz, Musterloesung } from '../types/Aufgabe';
import type { ProgressEintrag } from './ProgressApi';

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
}

export const aufgabenApi = new AufgabenApi();
