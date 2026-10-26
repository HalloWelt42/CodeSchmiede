import { HttpBase } from './HttpBase';
import type { Debuglauf } from '../types/Aufzeichnung';
import type { Messung, ProbelaufAntwort, SubmissionAntwort } from '../types/Submission';

export class SubmissionsApi extends HttpBase {
  constructor() {
    super('/api/submissions');
  }

  submit(aufgabeId: string, code: string): Promise<SubmissionAntwort> {
    return this.post<SubmissionAntwort>('', { aufgabe_id: aufgabeId, code });
  }

  /** Abgabe mit einer Messung des Browsers (CSS); werten tut der Server. */
  submitLokal(aufgabeId: string, code: string, messung: Messung): Promise<SubmissionAntwort> {
    return this.post<SubmissionAntwort>('/lokal', { aufgabe_id: aufgabeId, code, messung });
  }

  probelauf(aufgabeId: string, code: string, input: unknown[]): Promise<ProbelaufAntwort> {
    return this.post<ProbelaufAntwort>('/probelauf', { aufgabe_id: aufgabeId, code, input });
  }

  /** Wie der Probelauf, aber als Aufzeichnung je Zeile für den Debugger. */
  debuggen(aufgabeId: string, code: string, input: unknown[]): Promise<Debuglauf> {
    return this.post<Debuglauf>('/debuggen', { aufgabe_id: aufgabeId, code, input });
  }
}

export const submissionsApi = new SubmissionsApi();
