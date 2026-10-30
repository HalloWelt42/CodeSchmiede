---
zweck: "Eigener Programmier-Trainer: Aufbaukurs von null an (Python, SQL, JavaScript, CSS und Digitaltechnik) und Aufgaben in Python, JavaScript, SQL und CSS mit Prüfung in einer abgeschotteten Sandbox, Punkten, Lernspielen, Pfaden und Wiederholungen; am Rechner und als Web-App am Telefon."
geraet: [pi]
abhaengigkeiten: [kellerwolke, appkern]
daten:
  - "Pi: `{{wurzel}}/daten/codeschmiede.sqlite` (Lernfortschritt, Abgaben, Punkte, Tagesaufträge, Zugang zur Kellerwolke) und `daten/einrichtungscode`, solange die App uneingerichtet ist"
  - "Pi: Aufgaben und Kurs kommen nur lesend aus dem Stand des Repos in `{{wurzel}}/aufgaben` und `{{wurzel}}/kurs`; bearbeitet wird am Mac, ausgerollt über das Repo"
sicherung:
  - "Datenbank: nach der Regel des Appkerns eine Kopie nach `{{wurzel}}/sicherungen/codeschmiede-*.sqlite`, wöchentlich und vor dem Ausrollen (nur, wenn die jüngste älter als 24 Stunden ist), nie ohne Änderung, höchstens drei Stände (Umgebung `CODESCHMIEDE_SICHERUNG_ABSTAND_TAGE`, `..._VOR_AUSROLLEN_AB_STUNDEN`, `..._BEHALTEN`); das Werkzeug Sicherungen holt sie täglich nach `~/Sicherungen/codeschmiede/pi`. Ältere `nachts-*.sqlite` aus der Zeit davor bleiben liegen"
  - "Aufgaben und Kurs (Einführungen, Bilder) sind Dateien im Repo auf GitHub und brauchen keine eigene Sicherung"
schluessel_orte:
  - "Pi: App-Schlüssel der Kellerwolke in der Tabelle `einstellungen` von `codeschmiede.sqlite` (eingetragen in der ersten Einrichtung im Browser)"
  - "Pi: `{{wurzel}}/.env` (Modus 0600): gemeinsamer Schlüssel von Backend und Sandbox-Dienst, vom Ausrollen einmal erzeugt"
  - "Pi: `{{wurzel}}/zertifikate/`, Blattzertifikat mit Schlüssel aus der Hausstelle (vom Ausrollen)"
einrichten: einrichten.sh
stand: b9abc1e
---

# Codeschmiede

## Zweck

Die Codeschmiede ist der eigene Programmier-Trainer: Aufgaben als Dateien im Repo, ein Editor im Browser mit Debugger
(Haltepunkte, Schritte vor und zurück, Speicher), Lernspiele bis zur Ampelschule, Aufzugsteuerung, Turingmaschine, zu digitalen Schaltungen, Schaltungen mit Takt, KV-Diagrammen und zum Codeknacken, eine Prüfung mit sichtbaren und versteckten Tests, Punkte, Pfade, Wiederholungen und eine Verwaltung, die auch die versteckten
Tests zeigt. Fassung {{fassung}}, erreichbar unter {{adresse}}.

Eingereichter Code läuft nie im Backend, sondern im Sandbox-Dienst: je Prüfung ein eigener Container ohne Netz, nur
lesend, mit fremdem Nutzer und Grenzen für Zeit, Speicher und Prozesse. Nur der Sandbox-Dienst sieht den Docker-Socket.
Angemeldet wird mit dem Konto der [[Kellerwolke]] (Baustein des [[Appkern]]); nutzen darf die App das Konto, dem ihr
App-Schlüssel gehört.

## Was sie braucht

- Pi nach [[Grundlage Pi]] mit Docker und Compose; Platz unter `/mnt/data`.
- Die [[Kellerwolke]] für die Anmeldung und einen App-Schlüssel "Codeschmiede" darin.
- Am Mac: das Werkzeug `handbuch`, `mkcert` mit der Hausstelle (für das Zertifikat), `uv`, Node.js und Docker für
  Entwicklung, Tests und den Probelauf.

## Neu einrichten

Zuerst die Wahl: aus der Sicherung (Lernfortschritt wie vorher, die App ist schon eingerichtet) oder frisch (neuer
App-Schlüssel, Fortschritt beginnt bei null). Beide Wege gehen durch die Schritte 1 bis 3; aus der Sicherung kommt
danach Schritt 4, frisch Schritt 5.

### 1. Klon und Entwicklung am Mac

```
git clone {{repo}} {{ordner}}
cd {{ordner}} && ./einrichten.sh
```

`./einrichten.sh` baut die Sandbox-Abbilder, legt die Python-Umgebung genau nach `uv.lock` an und holt die Pakete der
Oberfläche. Das Ausrollen prüft mit dieser Umgebung.

Probe: `backend/.venv/bin/python -m pytest -q` ist grün.

### 2. Auf den Pi ausrollen

```
cd {{ordner}} && tools/ausrollen.sh
```

Das Ausrollen holt Rechner, Ordner und Adresse aus dem Handbuch, stellt das Zertifikat der Hausstelle aus, holt den
Stand nach `{{wurzel}}` auf {{rechner}}, legt den Schlüssel des Sandbox-Dienstes einmal in `{{wurzel}}/.env` an, baut
Backend, Sandbox-Dienst und die Sandbox-Abbilder, sichert die Datenbank nach der Sicherungsregel und startet neu;
nach dem Prüfen räumt es auf dem Pi verwaiste Abbilder und den Baucache von Docker auf.

Probe: das Ausrollen endet mit "Ausgerollt: {{adresse}}"; `curl --cacert {{wurzel}}/zertifikate/rootCA.pem
{{adresse}}/api/v1/app` auf dem Pi nennt dieselbe Fassung für Server und Oberfläche.

### 3. Sandbox prüfen

Im Browser eine Aufgabe öffnen und mit dem Startcode prüfen.

Probe: das Ergebnis zeigt Testzeilen (beim Startcode "nicht bestanden"), keine Meldung "Sandbox nicht erreichbar".

### 4. Aus der Sicherung zurückspielen

Die neueste Sicherung aus `~/Sicherungen/codeschmiede/pi` als `{{wurzel}}/daten/codeschmiede.sqlite` auf den Pi
kopieren (App vorher anhalten: `docker compose -f compose.pi.yml stop codeschmiede`, danach `up -d`). Sie enthält auch
den App-Schlüssel; die Einrichtung entfällt.

Probe: nach dem Anmelden zeigt die Startseite den alten Fortschritt.

### 5. Frisch: App-Schlüssel und erste Einrichtung

In der Kellerwolke am Rechner im Menü am eigenen Namen "Zugänge" öffnen (als Admin heißt der Eintrag "Verwaltung", darin der Reiter Zugänge), als Name der App "Codeschmiede" eintragen und "Schlüssel ausstellen". Der Schlüssel (`kw_app_...`) erscheint nur dieses eine Mal. Dann {{adresse}} öffnen: die
Seite "Erste Einrichtung" fragt nach der Adresse der Kellerwolke, dem App-Schlüssel und dem Einrichtungscode. Der Code
steht auf dem Pi in `{{wurzel}}/daten/einrichtungscode` und gilt nur, bis die App eingerichtet ist.

Probe: danach erscheint "Anmelden"; mit dem Konto, dem der App-Schlüssel gehört, öffnet sich die Startseite.

### 6. Telefon koppeln

Auf dem iPhone {{adresse}} öffnen, zum Home-Bildschirm hinzufügen und die Web-App starten. Jede Web-App hat ihren
eigenen Speicher: einmal "Gerät koppeln" mit einem Code aus der Kellerwolke (am Rechner im Menü am Namen, Reiter Geräte).

Probe: die Web-App zeigt die Startseite mit den Reitern unten.

## Sicherung und Rückspielen

Gesichert wird die Datenbank nach der Regel des Appkerns nach `{{wurzel}}/sicherungen/codeschmiede-*.sqlite`:
wöchentlich und vor dem Ausrollen (nur, wenn die jüngste älter als 24 Stunden ist), nie ohne Änderung, höchstens drei
Stände. Das Werkzeug Sicherungen holt sie täglich auf den Mac nach `~/Sicherungen/codeschmiede/pi`. Zurückspielen wie in Schritt 4; prüfen, dass nach dem Anmelden der Fortschritt stimmt.

## Wenn etwas klemmt

- "Sandbox nicht erreichbar" beim Prüfen: `docker compose -f compose.pi.yml ps` im Ordner `{{wurzel}}`; läuft
  `codeschmiede-sandbox` nicht, `docker compose -f compose.pi.yml logs sandbox`. Fehlt ein Abbild
  `codeschmiede-sandbox:python`, erneut ausrollen (es baut die Abbilder mit).
- Prüfungen laufen in die Zeitgrenze: der Pi startet Container langsamer als der Mac; die Startreserve des Sandbox-Dienstes
  (`CODESCHMIEDE_SANDBOX_STARTZEIT_SEKUNDEN`, Vorgabe 20) in `compose.pi.yml` erhöhen.
- Speichergrenze: Raspberry Pi OS startet den Kernel mit `cgroup_disable=memory`; dann setzt Docker `--memory` nicht
  durch. Der Sandbox-Dienst merkt das selbst (`/gesund` meldet `speichergrenze: datengrenze`) und begrenzt jeden Lauf
  nur über die Datengrenze je Prozess (Python 128 MB, JavaScript 512 MB). Volle Speichergrenze: `cgroup_enable=memory`
  an die eine Zeile in `/boot/firmware/cmdline.txt` anhängen und den Pi neu starten; danach meldet `/gesund`
  `speichergrenze: cgroup`.
- Der Debugger meldet "Die Ausgabe war zu lang": eine Aufzeichnung wird höchstens etwa 600 KB groß und braucht die
  Ausgabegrenze des Sandbox-Dienstes (`CODESCHMIEDE_SANDBOX_MAX_AUSGABE_BYTES`, Vorgabe 1 MB); nicht darunter setzen.
- Anmeldung "Die Kellerwolke ist gerade nicht erreichbar": Adresse und Zertifikat prüfen; bestätigte Anmeldungen gelten
  bis zu 24 Stunden weiter.
- Ein Koppelcode "gilt nicht": er muss aus der Kellerwolke stammen, mit der die App verbunden ist (Adresse auf der
  Anmeldeseite).
- Der Einrichtungscode fehlt: nur solange die App uneingerichtet ist, gibt es ihn; nach einem Neustart steht ein neuer
  in `{{wurzel}}/daten/einrichtungscode`.
