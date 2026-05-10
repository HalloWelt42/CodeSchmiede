import { HttpBase } from './HttpBase';
import type { SubmissionAntwort } from '../types/Submission';

export class SubmissionsApi extends HttpBase {
  constructor() {
    super('/api/submissions');
  }

  submit(aufgabeId: string, code: string): Promise<SubmissionAntwort> {
    return this.post<SubmissionAntwort>('', { aufgabe_id: aufgabeId, code });
  }
}

export const submissionsApi = new SubmissionsApi();
