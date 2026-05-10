import { HttpBase } from './HttpBase';
import type { AufgabeDetail, AufgabeKurz, Musterloesung } from '../types/Aufgabe';

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
}

export const aufgabenApi = new AufgabenApi();
