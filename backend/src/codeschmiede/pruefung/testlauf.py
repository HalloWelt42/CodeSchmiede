"""Testlauf -- ruft die Funktion einer Aufgabe in der Sandbox mit einer
Liste von Eingaben auf und liefert die dekodierten Rückgaben.

In die Sandbox gehen nur Nutzercode und Eingaben. Erwartete Werte
verlassen das Backend nie; verglichen wird in den Prüfern.

Das Skript besteht aus dem Nutzercode und einem angehängten Lauf je
Sprache. Der Lauf schreibt am Ende eine Zeile hinter eine Marke mit
Zufallsanteil je Lauf; alles davor ist Ausgabe des Nutzers.
"""

import json
import re
import secrets
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from ..sandbox.result import RunLimits, RunResult
from ..sandbox.runner import Runner
from .kodierung import dekodiere

FUNKTIONSNAME = re.compile(r"^[A-Za-z_$][A-Za-z0-9_$]*$")


@dataclass
class Aufruf:
    ok: bool
    wert: Any = None
    fehler: str | None = None


@dataclass
class TestlaufErgebnis:
    # None: der Lauf kam nicht bis zum Ergebnis (Syntaxfehler, Abbruch, Zeit)
    aufrufe: list[Aufruf] | None
    nutzer_stdout: str
    stderr: str
    laufzeit_ms: float
    timeout: bool
    gekuerzt: bool


def neue_marke() -> str:
    return f"===CODESCHMIEDE_{secrets.token_hex(8)}==="


def lies_block(erg: RunResult, marke: str) -> tuple[str, Any | None]:
    """Trennt Nutzerausgabe und Ergebniszeile. Liefert (stdout, block)."""
    davor, gefunden, danach = erg.stdout.rpartition(marke)
    if not gefunden:
        return erg.stdout, None
    zeile = danach.strip().splitlines()[0] if danach.strip() else ""
    try:
        return davor.removesuffix("\n"), json.loads(zeile)
    except json.JSONDecodeError:
        return davor.removesuffix("\n"), None


def hinweise(erg: RunResult) -> str:
    if erg.gekuerzt:
        return erg.stderr + "\nAbgebrochen: Die Ausgabe war zu lang."
    return erg.stderr


def _python(code: str, funktion: str, eingaben_json: str, marke: str) -> str:
    return (
        f"{code}\n\n"
        "# === Codeschmiede: Testlauf ===\n"
        "def __cs_testlauf():\n"
        "    import json as __j, math as __m, sys as __s, time as __t\n"
        "    def __k(w, tiefe=0):\n"
        "        if tiefe > 50:\n"
        "            return {'__r': 'zu tief verschachtelt'}\n"
        "        if w is None or isinstance(w, (bool, str, int)):\n"
        "            return w\n"
        "        if isinstance(w, float):\n"
        "            return w if __m.isfinite(w) else {'__f': repr(w)}\n"
        "        if isinstance(w, list):\n"
        "            return [__k(x, tiefe + 1) for x in w]\n"
        "        if isinstance(w, tuple):\n"
        "            return {'__t': [__k(x, tiefe + 1) for x in w]}\n"
        "        if isinstance(w, (set, frozenset)):\n"
        "            return {'__s': [__k(x, tiefe + 1) for x in w]}\n"
        "        if isinstance(w, dict):\n"
        "            return {'__d': [[__k(a, tiefe + 1), __k(b, tiefe + 1)] for a, b in w.items()]}\n"
        "        return {'__r': type(w).__name__ + ': ' + repr(w)[:200]}\n"
        f"    __eingaben = __j.loads({eingaben_json!r})\n"
        "    __aufrufe = []\n"
        "    __start = __t.perf_counter()\n"
        "    for __e in __eingaben:\n"
        "        try:\n"
        f"            __w = {funktion}(*__e)\n"
        "        except Exception as __x:\n"
        "            __aufrufe.append({'ok': False, 'fehler': (type(__x).__name__ + ': ' + str(__x))[:500]})\n"
        "            continue\n"
        "        try:\n"
        "            __aufrufe.append({'ok': True, 'wert': __k(__w)})\n"
        "        except Exception as __x:\n"
        "            __aufrufe.append({'ok': True, 'wert': {'__r': 'nicht lesbar: ' + type(__x).__name__}})\n"
        "    __ms = (__t.perf_counter() - __start) * 1000\n"
        "    __s.stdout.flush()\n"
        f"    __s.stdout.write('\\n' + {marke!r} + __j.dumps({{'aufrufe': __aufrufe, 'ms': __ms}}) + '\\n')\n"
        "    __s.stdout.flush()\n"
        "\n"
        "__cs_testlauf()\n"
    )


def _javascript(code: str, funktion: str, eingaben_json: str, marke: str) -> str:
    return (
        f"{code}\n"
        ";// === Codeschmiede: Testlauf ===\n"
        "(async () => {\n"
        "  const __k = (w, t = 0) => {\n"
        "    if (t > 50) return { __r: 'zu tief verschachtelt' };\n"
        "    if (w === null) return null;\n"
        "    if (w === undefined) return { __u: 1 };\n"
        "    const art = typeof w;\n"
        "    if (art === 'boolean' || art === 'string') return w;\n"
        "    if (art === 'number') return Number.isFinite(w) ? w : { __f: String(w) };\n"
        "    if (Array.isArray(w)) return w.map((x) => __k(x, t + 1));\n"
        "    if (w instanceof Set) return { __s: [...w].map((x) => __k(x, t + 1)) };\n"
        "    if (w instanceof Map) return { __d: [...w].map(([a, b]) => [__k(a, t + 1), __k(b, t + 1)]) };\n"
        "    if (art === 'object') {\n"
        "      const proto = Object.getPrototypeOf(w);\n"
        "      if (proto === Object.prototype || proto === null) {\n"
        "        return { __d: Object.entries(w).map(([a, b]) => [a, __k(b, t + 1)]) };\n"
        "      }\n"
        "    }\n"
        "    const name = (w && w.constructor && w.constructor.name) || art;\n"
        "    return { __r: name + ': ' + String(w).slice(0, 200) };\n"
        "  };\n"
        f"  const __eingaben = JSON.parse({json.dumps(eingaben_json)});\n"
        f"  const __f = typeof {funktion} === 'function' ? {funktion} : null;\n"
        "  const __aufrufe = [];\n"
        "  const __start = performance.now();\n"
        "  for (const __e of __eingaben) {\n"
        "    if (!__f) {\n"
        f"      __aufrufe.push({{ ok: false, fehler: 'ReferenceError: {funktion} ist nicht definiert' }});\n"
        "      continue;\n"
        "    }\n"
        "    try {\n"
        "      const __w = await __f(...__e);\n"
        "      __aufrufe.push({ ok: true, wert: __k(__w) });\n"
        "    } catch (__x) {\n"
        "      const name = __x && __x.name ? __x.name : 'Error';\n"
        "      const text = __x && __x.message !== undefined ? __x.message : String(__x);\n"
        "      __aufrufe.push({ ok: false, fehler: (name + ': ' + text).slice(0, 500) });\n"
        "    }\n"
        "  }\n"
        "  const __ms = performance.now() - __start;\n"
        f"  process.stdout.write('\\n' + {json.dumps(marke)} + JSON.stringify({{ aufrufe: __aufrufe, ms: __ms }}) + '\\n');\n"
        "})();\n"
    )


LAEUFE: dict[str, Callable[[str, str, str, str], str]] = {
    "python": _python,
    "javascript": _javascript,
}


def fuehre_aus(
    runner: Runner,
    sprache: str,
    code: str,
    funktion: str,
    eingaben: list[list[Any]],
    limits: RunLimits,
) -> TestlaufErgebnis:
    lauf = LAEUFE.get(sprache)
    if lauf is None:
        raise ValueError(f"Für die Sprache '{sprache}' gibt es keinen Testlauf")
    if not FUNKTIONSNAME.match(funktion):
        raise ValueError(f"Ungültiger Funktionsname '{funktion}'")

    marke = neue_marke()
    erg = runner.run_code(lauf(code, funktion, json.dumps(eingaben), marke), sprache, limits)
    stdout, block = lies_block(erg, marke)

    aufrufe: list[Aufruf] | None = None
    laufzeit_ms = erg.laufzeit_ms
    if isinstance(block, dict) and isinstance(block.get("aufrufe"), list):
        roh = block["aufrufe"]
        if len(roh) == len(eingaben):
            aufrufe = [
                Aufruf(ok=True, wert=dekodiere(a.get("wert")))
                if a.get("ok")
                else Aufruf(ok=False, fehler=str(a.get("fehler")))
                for a in roh
            ]
            laufzeit_ms = float(block.get("ms", laufzeit_ms))

    return TestlaufErgebnis(
        aufrufe=aufrufe,
        nutzer_stdout=stdout,
        stderr=hinweise(erg),
        laufzeit_ms=laufzeit_ms,
        timeout=erg.timeout,
        gekuerzt=erg.gekuerzt,
    )
