import { HttpBase } from './HttpBase';

export interface Gesundheit {
  status: string;
  version: string;
  aufgaben_anzahl: number;
  pfade_anzahl: number;
  befunde_anzahl: number;
  aufgaben_schreibbar: boolean;
}

export class SystemApi extends HttpBase {
  constructor() {
    super('/api');
  }

  // Ohne Browser-Zwischenspeicher: die Fassung des Servers muss frisch sein.
  gesundheit(): Promise<Gesundheit> {
    return this.request<Gesundheit>('/healthz', { method: 'GET', cache: 'no-store' });
  }
}

export const systemApi = new SystemApi();
