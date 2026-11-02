<?php
// Aufzeichnung eines PHP-Laufs für den Debugger (Nachschlag WIKI-48), Gegenstück zu lauf.py (Python) und
// aufzeichner.js. Das Beispiel läuft in einem eigenen PHP-Prozess mit Xdebug; dieser Rahmen verbindet sich mit ihm
// über DBGp wie ein Debugger, geht Schritt für Schritt (step_into) und liest bei jedem Halt den Aufrufstapel und die
// lokalen Namen jedes Rahmens. Nur Rahmen des Beispiels zählen; eingebaute Funktionen (array_map) bleiben unsichtbar.
// Haltepunkte vom Typ "return" auf jeder Funktion des Beispiels zeigen, wann sie zurückkehrt; so trennt sich der
// nächste Aufruf von einer Schleife, und ab Xdebug 3 steht dort der Rückgabewert ($__RETURN_VALUE). Wie in Python ist
// jeder Schritt eine ausgeführte Zeile mit dem Speicher danach.
//
// Läuft unter derselben PHP-Fassung wie das Beispiel, also auch unter 5.6: kein ??, keine Typangaben, kein fn.
// Die Platzhalter setzt lauf.py ein (Base64 von JSON, damit kein Zeichen den Rahmen bricht).

error_reporting(E_ALL & ~E_DEPRECATED);
$BEISPIEL = '/tmp/beispiel.php';
$GRENZEN = json_decode(base64_decode('__GRENZEN__'), true);
$MAX_SCHRITTE = $GRENZEN[0];
$MAX_TIEFE = $GRENZEN[1];
$MAX_ELEMENTE = $GRENZEN[2];
$MAX_ZEICHEN = $GRENZEN[3];
$MAX_BYTES = $GRENZEN[4];
$CODE = base64_decode('__CODE__');
$EINGABE = json_decode(base64_decode('__EINGABE__'), true);
$MARKE = base64_decode('__MARKE__');
$FRIST = microtime(true) + __SEKUNDEN__;

// ---------- DBGp: Pakete "Länge NUL XML NUL" lesen, Befehle "befehl -i nr NUL" senden ----------

function dbgp_lesen($v) {
    $laenge = '';
    while (($z = fgetc($v)) !== false && $z !== "\0") $laenge .= $z;
    if ($z === false) return null;
    $daten = '';
    $rest = (int) $laenge + 1;
    while ($rest > 0 && !feof($v)) {
        $teil = fread($v, $rest);
        if ($teil === false || $teil === '') break;
        $daten .= $teil;
        $rest -= strlen($teil);
    }
    // Namensräume und Vorsilben (xdebug:message) weg, sonst sieht SimpleXML die Kinder nicht
    $daten = preg_replace('/ xmlns(:\w+)?="[^"]*"/', '', rtrim($daten, "\0"));
    $daten = preg_replace('/<(\/?)\w+:/', '<$1', $daten);
    $daten = preg_replace('/ \w+:(\w+)=/', ' $1=', $daten);
    $xml = @simplexml_load_string($daten);
    return $xml === false ? null : $xml;
}

function dbgp($v, $befehl) {
    static $nr = 0;
    $nr++;
    fwrite($v, $befehl . ' -i ' . $nr . "\0");
    do {
        $antwort = dbgp_lesen($v);
    } while ($antwort !== null && $antwort->getName() !== 'response');
    return $antwort;
}

// ---------- Werte: wie die Python-Werte (Art, Darstellung, Elemente, Paare, Attribute) ----------

function utf8($s) {
    if (preg_match('//u', $s)) return $s;
    return function_exists('mb_convert_encoding') ? mb_convert_encoding($s, 'UTF-8', 'UTF-8') : preg_replace('/[\x80-\xff]/', '?', $s);
}

function kurz($s) {
    global $MAX_ZEICHEN;
    $s = utf8($s);
    if (function_exists('mb_strlen')) return mb_strlen($s, 'UTF-8') <= $MAX_ZEICHEN ? $s : mb_substr($s, 0, $MAX_ZEICHEN - 3, 'UTF-8') . '...';
    return strlen($s) <= $MAX_ZEICHEN ? $s : substr($s, 0, $MAX_ZEICHEN - 3) . '...';
}

function inhalt($p) {
    $s = (string) $p;
    return ((string) $p['encoding']) === 'base64' ? base64_decode($s) : $s;
}

function schluessel($p) {
    // Kinder eines Arrays heißen wie ihr Schlüssel; Xdebug 2 schreibt "0", Xdebug 3 auch, Texte ohne Anführung
    $name = (string) $p['name'];
    return ctype_digit(ltrim($name, '-')) && $name !== '' ? array('art' => 'zahl', 'darstellung' => $name)
        : array('art' => 'text', 'darstellung' => kurz("'" . $name . "'"));
}

function wert($p) {
    $typ = (string) $p['type'];
    $roh = inhalt($p);
    switch ($typ) {
        case 'int':
        case 'float':
            return array('art' => 'zahl', 'darstellung' => kurz($roh));
        case 'bool':
            return array('art' => 'wahrheit', 'darstellung' => $roh === '1' ? 'true' : 'false');
        case 'null':
        case 'uninitialized':
            return array('art' => 'nichts', 'darstellung' => 'null');
        case 'string':
            return array('art' => 'text', 'darstellung' => kurz("'" . $roh . "'"));
        case 'array':
            return liste($p);
        case 'object':
            return objekt($p);
    }
    return array('art' => 'sonst', 'darstellung' => kurz($typ));
}

function liste($p) {
    $kinder = array();
    foreach ($p->property as $k) $kinder[] = $k;
    $anzahl = (int) $p['numchildren'];
    $gekuerzt = count($kinder) < $anzahl;
    $fortlaufend = true;
    foreach ($kinder as $i => $k) if ((string) $k['name'] !== (string) $i) $fortlaufend = false;
    $teile = array();
    if ($fortlaufend) {
        $elemente = array();
        foreach ($kinder as $k) {
            $w = wert($k);
            $elemente[] = $w;
            $teile[] = $w['darstellung'];
        }
        $w = array('art' => 'liste', 'darstellung' => kurz('[' . implode(', ', $teile) . ($gekuerzt ? ', ...' : '') . ']'), 'elemente' => $elemente);
    } else {
        $paare = array();
        foreach ($kinder as $k) {
            $s = schluessel($k);
            $w = wert($k);
            $paare[] = array($s, $w);
            $teile[] = $s['darstellung'] . ' => ' . $w['darstellung'];
        }
        $w = array('art' => 'woerterbuch', 'darstellung' => kurz('[' . implode(', ', $teile) . ($gekuerzt ? ', ...' : '') . ']'), 'paare' => $paare);
    }
    if ($gekuerzt) $w['gekuerzt'] = true;
    return $w;
}

function objekt($p) {
    $klasse = (string) $p['classname'];
    if ($klasse === 'Closure') return array('art' => 'funktion', 'darstellung' => 'function');
    $attribute = array();
    foreach ($p->property as $k) $attribute[(string) $k['name']] = wert($k);
    $w = array('art' => 'objekt', 'darstellung' => kurz($klasse !== '' ? $klasse : 'object'));
    if ($attribute) $w['attribute'] = $attribute;
    if (count($attribute) < (int) $p['numchildren']) $w['gekuerzt'] = true;
    return $w;
}

// ---------- Rahmen und Schritte ----------

$EINGEBAUT = array();
$definiert = get_defined_functions();
foreach ($definiert['internal'] as $f) $EINGEBAUT[strtolower($f)] = true;

/** eingebaute Funktion oder Methode einer eingebauten Klasse: kein Rahmen des Beispiels */
function eingebaut($wo) {
    global $EINGEBAUT;
    if (preg_match('/^(.+?)(->|::)/', $wo, $m)) {
        if (!class_exists($m[1], false)) return false;
        $r = new ReflectionClass($m[1]);
        return $r->isInternal();
    }
    return isset($EINGEBAUT[strtolower($wo)]);
}

function rahmenname($wo) {
    if ($wo === '{main}') return 'Modul';
    if (strpos($wo, '{closure') === 0) return '(anonym)';
    return $wo;
}

/** Rahmen des Beispiels vom innersten nach außen: [Ebene, Name, Zeile] */
function rahmen_lesen($v) {
    global $BEISPIEL;
    $stapel = dbgp($v, 'stack_get');
    $ebenen = array();
    if ($stapel === null) return $ebenen;
    foreach ($stapel->stack as $f) {
        if ((string) $f['filename'] !== 'file://' . $BEISPIEL || eingebaut((string) $f['where'])) continue;
        $ebenen[] = array((int) $f['level'], rahmenname((string) $f['where']), (int) $f['lineno']);
    }
    return $ebenen;
}

/** Speicher: je Rahmen (vom Modul nach innen) die lokalen Namen */
function zustand_lesen($v, $ebenen) {
    $zustand = array();
    foreach (array_reverse($ebenen) as $e) {
        $kontext = dbgp($v, 'context_get -d ' . $e[0] . ' -c 0');
        $variablen = array();
        if ($kontext !== null) {
            foreach ($kontext->property as $p) {
                if (((string) $p['type']) === 'uninitialized') continue;
                $variablen[(string) $p['name']] = wert($p);
            }
        }
        $zustand[] = array('name' => $e[1], 'variablen' => $variablen ? $variablen : new stdClass());
    }
    return $zustand;
}

$schritte = array();
$bytes = 0;
$gekuerzt = false;
$alles = '';

function festhalten($zeile, $zustand, $ausgabe, $rueckgabe = null) {
    global $schritte, $bytes, $gekuerzt, $MAX_SCHRITTE, $MAX_BYTES;
    $schritt = array('zeile' => $zeile, 'rahmen' => $zustand, 'ausgabe' => $ausgabe);
    if ($rueckgabe !== null) $schritt['rueckgabe'] = $rueckgabe;
    $letzter = $schritte ? $schritte[count($schritte) - 1] : null;
    // Ein Schritt, der nichts Neues zeigt (zwei Halte in einer Zeile), entfällt
    if ($rueckgabe === null && $ausgabe === '' && $letzter !== null && $letzter['zeile'] === $zeile && json_encode($letzter['rahmen']) === json_encode($zustand)) return;
    $bytes += strlen(json_encode($schritt));
    if ($bytes > $MAX_BYTES) {
        if ($letzter !== null) $schritte[count($schritte) - 1]['ausgabe'] .= $ausgabe;
    } else {
        $schritte[] = $schritt;
    }
    if ($bytes > $MAX_BYTES || count($schritte) >= $MAX_SCHRITTE) $gekuerzt = true;
}

/** Was das Beispiel seit dem letzten Mal ausgegeben hat */
function neue_ausgabe($rohr) {
    global $alles;
    $neu = (string) stream_get_contents($rohr);
    $alles .= $neu;
    return utf8($neu);
}

/** Namen der Funktionen und Methoden des Beispiels, für Haltepunkte bei ihrer Rückkehr */
function funktionen($code) {
    $namen = array();
    $klasse = null;
    $tiefe = 0;
    $klassentiefe = -1;
    $marken = @token_get_all($code);
    $n = count($marken);
    for ($i = 0; $i < $n; $i++) {
        $m = $marken[$i];
        if ($m === '{') $tiefe++;
        elseif ($m === '}') {
            $tiefe--;
            if ($tiefe === $klassentiefe) { $klasse = null; $klassentiefe = -1; }
        } elseif (is_array($m) && ($m[0] === T_CURLY_OPEN || $m[0] === T_DOLLAR_OPEN_CURLY_BRACES)) $tiefe++;
        elseif (is_array($m) && in_array($m[0], array(T_CLASS, T_TRAIT), true)) {
            for ($j = $i + 1; $j < $n && is_array($marken[$j]) && $marken[$j][0] === T_WHITESPACE; $j++);
            if ($j < $n && is_array($marken[$j]) && $marken[$j][0] === T_STRING) { $klasse = $marken[$j][1]; $klassentiefe = $tiefe; }
        } elseif (is_array($m) && $m[0] === T_FUNCTION) {
            for ($j = $i + 1; $j < $n && (is_array($marken[$j]) && $marken[$j][0] === T_WHITESPACE || $marken[$j] === '&'); $j++);
            if ($j < $n && is_array($marken[$j]) && $marken[$j][0] === T_STRING) $namen[] = array($marken[$j][1], $klasse);
        }
    }
    return $namen;
}

// ---------- Ablauf ----------

file_put_contents($BEISPIEL, $CODE);
$server = stream_socket_server('tcp://127.0.0.1:0', $fehlernr, $fehlertext);
$adresse = stream_socket_get_name($server, false);
$port = (int) substr($adresse, strrpos($adresse, ':') + 1);
$einstellungen = version_compare(PHP_VERSION, '7.0', '<')
    ? array('xdebug.remote_enable=1', 'xdebug.remote_autostart=1', 'xdebug.remote_host=127.0.0.1', 'xdebug.remote_port=' . $port)
    : array('xdebug.mode=debug', 'xdebug.start_with_request=yes', 'xdebug.client_host=127.0.0.1', 'xdebug.client_port=' . $port,
            'xdebug.log_level=0');
$befehl = escapeshellarg(PHP_BINARY) . ' -d ' . escapeshellarg('zend_extension=' . ini_get('extension_dir') . '/xdebug.so')
    . ' -d display_errors=stderr -d html_errors=0 -d log_errors=0';
foreach ($einstellungen as $e) $befehl .= ' -d ' . escapeshellarg($e);
$befehl .= ' ' . escapeshellarg($BEISPIEL);
$kind = proc_open($befehl, array(0 => array('pipe', 'r'), 1 => array('pipe', 'w'), 2 => array('pipe', 'w')), $rohre);
fwrite($rohre[0], $EINGABE ? implode("\n", $EINGABE) . "\n" : '');
fclose($rohre[0]);
stream_set_blocking($rohre[1], false);
stream_set_blocking($rohre[2], false);

$fehler = null;
$fehlerzeile = null;
$abgebrochen = false;
$v = @stream_socket_accept($server, max(1, (int) ($FRIST - microtime(true))));
if ($v) {
    dbgp_lesen($v);                                       // Anmeldung des Prozesses (init)
    dbgp($v, 'feature_set -n max_depth -v ' . $MAX_TIEFE);
    dbgp($v, 'feature_set -n max_children -v ' . $MAX_ELEMENTE);
    dbgp($v, 'feature_set -n max_data -v ' . max(256, $MAX_ZEICHEN * 4));
    foreach (funktionen($CODE) as $f) dbgp($v, 'breakpoint_set -t return -m ' . $f[0] . ($f[1] !== null ? ' -a ' . $f[1] : ''));
    $vorige = null;
    $davor = '';                                          // Ausgabe vor dem ersten Halt
    $status = '';
    while (!$gekuerzt) {
        if (microtime(true) > $FRIST) { $abgebrochen = true; break; }
        $antwort = dbgp($v, 'step_into');
        $status = $antwort === null ? '' : (string) $antwort['status'];
        if ($status !== 'break') break;
        $ebenen = rahmen_lesen($v);
        $ausgabe = $davor . neue_ausgabe($rohre[1]);
        $davor = '';
        if (!$ebenen) { $davor = $ausgabe; continue; }
        // Rückkehr: die Meldung nennt die Zeile des Aufrufers, der Stapel zeigt noch die Funktion
        $gemeldet = isset($antwort->message) ? (int) $antwort->message['lineno'] : $ebenen[0][2];
        if ($gemeldet !== $ebenen[0][2]) {
            $r = dbgp($v, 'property_get -d ' . $ebenen[0][0] . ' -c 0 -n $__RETURN_VALUE');
            $rueckgabe = $r !== null && isset($r->property) ? wert($r->property) : null;
            // Xdebug 3 zeigt die Funktion noch mit ihren Namen, Xdebug 2 ohne (Zeile 0): dann der Stand davor
            $zustand = $ebenen[0][2] > 0 ? zustand_lesen($v, $ebenen) : ($vorige !== null ? $vorige['zustand'] : null);
            if ($vorige !== null && $zustand !== null) festhalten($vorige['zeile'], $zustand, $ausgabe, $rueckgabe);
            array_shift($ebenen);
            $vorige = $ebenen ? array('zeile' => $gemeldet, 'zustand' => zustand_lesen($v, $ebenen)) : null;
            continue;
        }
        $zustand = zustand_lesen($v, $ebenen);
        // ohne Haltepunkt bei der Rückkehr (Closures): weniger Rahmen heißt, die Funktion ist fertig; ihre letzte
        // Zeile zeigt noch ihren Speicher
        if ($vorige !== null) festhalten($vorige['zeile'], count($ebenen) < count($vorige['zustand']) ? $vorige['zustand'] : $zustand, $ausgabe);
        else $davor = $ausgabe;
        $vorige = array('zeile' => $ebenen[0][2], 'zustand' => $zustand);
    }
    // die letzte Zeile ist fertig, wenn das Beispiel endet; danach (oder nach einer Grenze) läuft es ohne Halt zu Ende
    if (!$abgebrochen) {
        // am Ende wartet der Prozess (stopping) und endet mit stop; nach einer Grenze läuft er ohne Halt zu Ende
        @dbgp($v, $status === 'stopping' ? 'stop' : 'detach');
        while (proc_get_status($kind)['running'] && microtime(true) < $FRIST) usleep(20000);
    }
    $rest = neue_ausgabe($rohre[1]);
    if ($vorige !== null && !$gekuerzt) festhalten($vorige['zeile'], $vorige['zustand'], $davor . $rest);
    elseif ($schritte) $schritte[count($schritte) - 1]['ausgabe'] .= $davor . $rest;
    fclose($v);
} else {
    while (proc_get_status($kind)['running'] && microtime(true) < $FRIST) usleep(20000);
    neue_ausgabe($rohre[1]);
}
if (proc_get_status($kind)['running']) {
    proc_terminate($kind, 9);
    $abgebrochen = true;
}
neue_ausgabe($rohre[1]);
$meldungen = '';
foreach (explode("\n", (string) stream_get_contents($rohre[2])) as $z) {
    if (trim($z) !== '' && strpos($z, 'Xdebug:') !== 0) $meldungen .= $z . "\n";
}
$meldungen = trim(str_replace($BEISPIEL, 'beispiel.php', utf8($meldungen)));
if ($abgebrochen) {
    $fehler = 'Zeit überschritten: der Lauf wurde abgebrochen';
} elseif (preg_match('/^(PHP )?(Parse error|Fatal error|Uncaught)/m', $meldungen)) {
    $fehler = $meldungen;
    if (preg_match('/on line (\d+)|\.php:(\d+)/', $meldungen, $m)) $fehlerzeile = (int) ($m[1] !== '' ? $m[1] : $m[2]);
}
echo "\n", $MARKE, "\n";
echo json_encode(array('schritte' => $schritte, 'ausgabe' => utf8($alles), 'gekuerzt' => $gekuerzt, 'fehler' => $fehler,
                       'fehlerzeile' => $fehlerzeile, 'hinweise' => $fehler === null ? $meldungen : ''),
                 JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PARTIAL_OUTPUT_ON_ERROR), "\n";
