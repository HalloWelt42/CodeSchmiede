/*
 * Mock-Daten für das Frontend, solange die Backend-Routen noch nicht
 * stehen. Spiegelt 1:1 den Inhalt der drei Aufgaben-Frontmatter wider.
 * Wird ersetzt durch echten API-Aufruf in einem spaeteren Schritt.
 */

import type { AufgabeKurz, PfadKurz } from '../types/Aufgabe';

export const mockAufgaben: AufgabeKurz[] = [
  {
    id: '001-fizzbuzz',
    titel: 'FizzBuzz',
    sprache: 'python',
    schwierigkeit: 'anfaenger',
    schwierigkeit_score: 12,
    schaetz_minuten: 10,
    tags: ['if-else', 'modulo', 'schleifen', 'klassiker'],
    pfade: ['python_grundlagen'],
  },
  {
    id: '002-palindrom',
    titel: 'Palindrom-Pruefung',
    sprache: 'python',
    schwierigkeit: 'anfaenger',
    schwierigkeit_score: 18,
    schaetz_minuten: 10,
    tags: ['strings', 'slicing', 'schleifen'],
    pfade: ['python_grundlagen'],
  },
  {
    id: '003-fibonacci',
    titel: 'Fibonacci-Zahl',
    sprache: 'python',
    schwierigkeit: 'mittel',
    schwierigkeit_score: 35,
    schaetz_minuten: 20,
    tags: ['rekursion', 'iteration', 'memoisierung', 'performance'],
    pfade: ['python_grundlagen'],
  },
];

export const mockPfad: PfadKurz = {
  id: 'python_grundlagen',
  titel: 'Python-Grundlagen',
  beschreibung:
    'Klassische Einsteiger-Aufgaben für Python. Drei berühmte Klassiker, ' +
    'die zentrale Konzepte testen: Verzweigungen mit if/elif, den ' +
    'Modulo-Operator, String-Slicing und Rekursion vs. Iteration. Wer ' +
    'diesen Pfad durchgespielt hat, hat ein solides Fundament für alles ' +
    'Weitere.',
  reihenfolge: ['001-fizzbuzz', '002-palindrom', '003-fibonacci'],
};
