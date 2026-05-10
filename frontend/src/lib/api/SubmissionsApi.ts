import { HttpBase } from './HttpBase';
import type { PruefErgebnis, ProbelaufAntwort, SubmissionAntwort } from '../types/Submission';

export class SubmissionsApi extends HttpBase {
  constructor() {
    super('/api/submissions');
  }

  submit(aufgabeId: string, code: string): Promise<SubmissionAntwort> {
    return this.post<SubmissionAntwort>('', { aufgabe_id: aufgabeId, code });
  }

  /** Speichert eine Submission mit clientseitig erstelltem Pruef-Ergebnis (z.B. JS via WebWorker). */
  submitLokal(
    aufgabeId: string,
    code: string,
    pruefung: PruefErgebnis,
  ): Promise<SubmissionAntwort> {
    return this.post<SubmissionAntwort>('/lokal', {
      aufgabe_id: aufgabeId,
      code,
      pruefung,
    });
  }

  probelauf(aufgabeId: string, code: string, input: unknown[]): Promise<ProbelaufAntwort> {
    return this.post<ProbelaufAntwort>('/probelauf', { aufgabe_id: aufgabeId, code, input });
  }
}

export const submissionsApi = new SubmissionsApi();
