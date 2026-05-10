/*
 * WebWorkerRunner -- fuehrt JavaScript-Code in einer isolierten
 * Web-Worker-Sandbox im Browser aus.
 *
 * Ablauf:
 *   1. Wir spawnen pro Submission einen frischen Worker, damit globale
 *      State-Reste vom Nutzer-Code keine Folge-Tests stoeren.
 *   2. Der Worker bekommt Nutzer-Code + Funktionsname + Liste von Tests
 *      ueber `postMessage`. Er ruft die Funktion fuer jeden Test auf,
 *      vergleicht das Ergebnis und schickt eine Zusammenfassung zurueck.
 *   3. Timeout sorgt dafuer, dass Endlosschleifen den UI-Thread nicht
 *      blockieren -- nach `timeout_ms` wird der Worker terminiert und
 *      ein Timeout-Resultat geliefert.
 *
 * Sicherheit: Web Worker haben keinen DOM-Zugriff, kein localStorage,
 * keinen Cookie. fetch() ist im Worker zwar verfuegbar, aber
 * Same-Origin-Policy gilt -- kein direkter Schaden moeglich.
 */

export interface WebWorkerTestErgebnis {
  index: number;
  bestanden: boolean;
  eingabe: unknown[];
  erwartet: unknown;
  tatsaechlich: unknown;
  fehler: string | null;
}

export interface WebWorkerLaufErgebnis {
  bestanden: boolean;
  sichtbar: WebWorkerTestErgebnis[];
  versteckt_pass: number;
  versteckt_fail: number;
  laufzeit_ms: number;
  stdout: string;
  stderr: string;
  timeout: boolean;
}

interface WorkerInput {
  code: string;
  funktion: string;
  tests: { input: unknown[]; expected: unknown }[];
  sichtbar_anz: number;
}

interface WorkerOutput {
  bestanden: boolean;
  sichtbar: WebWorkerTestErgebnis[];
  versteckt_pass: number;
  versteckt_fail: number;
  laufzeit_ms: number;
  stdout: string;
  stderr: string;
}

const WORKER_QUELLCODE = `
self.onmessage = (ev) => {
  const { code, funktion, tests, sichtbar_anz } = ev.data;
  const stdout_teile = [];
  const stderr_teile = [];
  const original_log = console.log;
  console.log = (...args) => {
    stdout_teile.push(args.map((a) => String(a)).join(' '));
  };
  const original_err = console.error;
  console.error = (...args) => {
    stderr_teile.push(args.map((a) => String(a)).join(' '));
  };

  let starten;
  try {
    // Nutzer-Code wird als IIFE ausgewertet, fn wird per Name geholt
    const wrapper = new Function(code + '\\nreturn typeof ' + funktion + ' === "function" ? ' + funktion + ' : null;');
    starten = wrapper();
    if (!starten) {
      self.postMessage({
        bestanden: false,
        sichtbar: tests.slice(0, sichtbar_anz).map((t, i) => ({
          index: i, bestanden: false, eingabe: t.input, erwartet: t.expected,
          tatsaechlich: null, fehler: 'Funktion ' + funktion + ' nicht definiert',
        })),
        versteckt_pass: 0,
        versteckt_fail: tests.length - sichtbar_anz,
        laufzeit_ms: 0,
        stdout: stdout_teile.join('\\n'),
        stderr: stderr_teile.join('\\n'),
      });
      return;
    }
  } catch (e) {
    self.postMessage({
      bestanden: false,
      sichtbar: tests.slice(0, sichtbar_anz).map((t, i) => ({
        index: i, bestanden: false, eingabe: t.input, erwartet: t.expected,
        tatsaechlich: null, fehler: e.name + ': ' + e.message,
      })),
      versteckt_pass: 0,
      versteckt_fail: tests.length - sichtbar_anz,
      laufzeit_ms: 0,
      stdout: stdout_teile.join('\\n'),
      stderr: stderr_teile.join('\\n'),
    });
    return;
  }

  const start_zeit = performance.now();
  const sichtbar = [];
  let versteckt_pass = 0;
  let versteckt_fail = 0;
  let alle_ok = true;

  for (let i = 0; i < tests.length; i++) {
    const t = tests[i];
    let actual = null;
    let fehler = null;
    let ok = false;
    try {
      actual = starten(...t.input);
      ok = JSON.stringify(actual) === JSON.stringify(t.expected);
    } catch (e) {
      fehler = e.name + ': ' + e.message;
    }
    if (!ok) alle_ok = false;
    if (i < sichtbar_anz) {
      sichtbar.push({
        index: i, bestanden: ok, eingabe: t.input, erwartet: t.expected,
        tatsaechlich: actual, fehler,
      });
    } else {
      if (ok) versteckt_pass++;
      else versteckt_fail++;
    }
  }

  const laufzeit = performance.now() - start_zeit;
  console.log = original_log;
  console.error = original_err;
  self.postMessage({
    bestanden: alle_ok,
    sichtbar,
    versteckt_pass,
    versteckt_fail,
    laufzeit_ms: laufzeit,
    stdout: stdout_teile.join('\\n'),
    stderr: stderr_teile.join('\\n'),
  });
};
`;

let blob_url: string | null = null;

function holeWorkerUrl(): string {
  if (!blob_url) {
    const blob = new Blob([WORKER_QUELLCODE], { type: 'application/javascript' });
    blob_url = URL.createObjectURL(blob);
  }
  return blob_url;
}

export class WebWorkerRunner {
  async run(
    code: string,
    funktion: string,
    tests_sichtbar: { input: unknown[]; expected: unknown }[],
    tests_versteckt: { input: unknown[]; expected: unknown }[],
    timeout_ms = 5000,
  ): Promise<WebWorkerLaufErgebnis> {
    const alle_tests = [...tests_sichtbar, ...tests_versteckt];
    const eingabe: WorkerInput = {
      code,
      funktion,
      tests: alle_tests,
      sichtbar_anz: tests_sichtbar.length,
    };

    const worker = new Worker(holeWorkerUrl());
    let timer: ReturnType<typeof setTimeout> | null = null;

    const ergebnis = await new Promise<WebWorkerLaufErgebnis>((resolve) => {
      worker.onmessage = (e: MessageEvent<WorkerOutput>) => {
        if (timer) clearTimeout(timer);
        worker.terminate();
        resolve({ ...e.data, timeout: false });
      };
      worker.onerror = (e) => {
        if (timer) clearTimeout(timer);
        worker.terminate();
        resolve({
          bestanden: false,
          sichtbar: tests_sichtbar.map((t, i) => ({
            index: i, bestanden: false, eingabe: t.input, erwartet: t.expected,
            tatsaechlich: null, fehler: e.message ?? 'Worker-Fehler',
          })),
          versteckt_pass: 0,
          versteckt_fail: tests_versteckt.length,
          laufzeit_ms: 0,
          stdout: '',
          stderr: e.message ?? 'Worker-Fehler',
          timeout: false,
        });
      };
      timer = setTimeout(() => {
        worker.terminate();
        resolve({
          bestanden: false,
          sichtbar: tests_sichtbar.map((t, i) => ({
            index: i, bestanden: false, eingabe: t.input, erwartet: t.expected,
            tatsaechlich: null, fehler: 'Timeout',
          })),
          versteckt_pass: 0,
          versteckt_fail: tests_versteckt.length,
          laufzeit_ms: timeout_ms,
          stdout: '',
          stderr: `Timeout nach ${timeout_ms}ms`,
          timeout: true,
        });
      }, timeout_ms);
      worker.postMessage(eingabe);
    });

    return ergebnis;
  }
}

export const webWorkerRunner = new WebWorkerRunner();
