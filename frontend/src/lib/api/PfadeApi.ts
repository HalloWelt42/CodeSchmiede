import { HttpBase } from './HttpBase';
import type { Pfad } from '../types/Aufgabe';

export class PfadeApi extends HttpBase {
  constructor() {
    super('/api/pfade');
  }

  liste(): Promise<Pfad[]> {
    return this.get<Pfad[]>('');
  }

  detail(id: string): Promise<Pfad> {
    return this.get<Pfad>(`/${id}`);
  }
}

export const pfadeApi = new PfadeApi();
