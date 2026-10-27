---
schema_version: 1
id: c003-vigenere
revision: 1
titel: Vigenère knacken
sprache: python
task_type: codes
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 55
schaetz_minuten: 40
tags: [codes, strings, slicing]
voraussetzungen: []
quelle:
  url: null
  notiz: Codes knacken, Level 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 15
hints:
  - kosten: 1
    text: "Nimm nur die Buchstaben A bis Z des Geheimtexts. Bei bekannter Länge n ist `buchstaben[i::n]` alles, was mit demselben Schlüsselbuchstaben verschoben wurde: eine Cäsar-Nachricht für sich, nur ohne Sinn."
  - kosten: 1
    text: "Jede Spalte knackst du wie in Level 1 über die Häufigkeit. Die gefundenen Verschiebungen sind das Schlüsselwort, A ist 0, B ist 1."
  - kosten: 2
    text: "Länge finden: Bei der richtigen Länge ist jede Spalte so ungleich verteilt wie Deutsch. Zähl je Spalte, wie oft zwei zufällig gezogene Buchstaben gleich sind (Koinzidenzindex): Deutsch liegt bei 0,076, ein Zufallstext bei 0,038. Die kleinste Länge über 0,06 gewinnt."
starter_code: |
  ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


  def zurueck(geheim, wort):
      # der n-te Buchstabe (nur A bis Z gezählt) rückt um den n-ten Buchstaben des Worts zurück
      return geheim


  def knacke_laenge(geheim, laenge):
      return geheim


  def knacke(geheim):
      return geheim
codes:
  verfahren: vigenere
  bereit: [DEUTSCH]
  sichtbar:
    - name: Probe
      klar: "TREFFEN SICH ZWEI ROBOTER. SAGT DER EINE: DU SIEHST ABER VERROSTET AUS."
      schluessel: KAT
      funktion: zurueck
      mit: [KAT]
    - name: Länge bekannt
      schluessel: BRIEF
      funktion: knacke_laenge
      mit: [5]
      klar: >-
        LIEBE TANTE ERNA, VIELEN DANK FÜR DAS PAKET. DIE SOCKEN SIND WARM UND DER KUCHEN WAR LECKER,
        AUCH WENN DER HUND DAS MEISTE DAVON GEGESSEN HAT. HIER REGNET ES SEIT DREI TAGEN, ABER IN DER
        SCHULE HABEN WIR JETZT EINEN NEUEN COMPUTERRAUM. ICH LERNE PROGRAMMIEREN UND SCHREIBE DIR
        BALD EINE GEHEIME NACHRICHT, DIE NUR DU LESEN KANNST. DEIN NEFFE PAUL
    - name: Nachricht 1
      schluessel: SONNE
      klar: >-
        AM MORGEN STEIGT DER NEBEL AUS DEM TAL, UND DIE ERSTEN STRAHLEN WÄRMEN DIE FELDER. DER BAUER
        FÄHRT MIT SEINEM TRAKTOR HINAUS, DIE KÜHE STEHEN AM ZAUN UND SCHAUEN IHM NACH. MITTAGS IST ES
        HEISS, UND ALLE SUCHEN DEN SCHATTEN UNTER DER GROSSEN LINDE. ERST AM ABEND KOMMT EIN KÜHLER
        WIND AUF, DIE SCHWALBEN FLIEGEN TIEF, UND IN DER FERNE GROLLT DER ERSTE DONNER.
    - name: Nachricht 2
      schluessel: MOND
      klar: >-
        DIE RAUMSONDE IST SEIT ZWANZIG JAHREN UNTERWEGS UND HAT SCHON DIE BAHN DES LETZTEN PLANETEN
        HINTER SICH GELASSEN. IHRE BATTERIE WIRD JEDES JAHR SCHWÄCHER, DOCH SIE FUNKT IMMER NOCH
        TREU IHRE MESSWERTE ZUR ERDE. EIN SIGNAL BRAUCHT VIELE STUNDEN, BIS ES BEI DEN GROSSEN
        ANTENNEN ANKOMMT, UND DIE FORSCHER FREUEN SICH ÜBER JEDES EINZELNE BIT.
  versteckt:
    - name: Nachricht 3
      schluessel: LAMPE
      klar: >-
        IM KELLER DES MUSEUMS STEHT EINE ALTE DAMPFMASCHINE. SIE IST GRÖSSER ALS EIN AUTO, UND IHRE
        RÄDER SIND SCHWERER ALS EIN ELEFANT. FRÜHER TRIEB SIE EINE GANZE FABRIK AN, HEUTE DARF SIE
        NUR NOCH AN FEIERTAGEN LAUFEN. DANN ZISCHT UND STAMPFT ES, DIE KINDER HALTEN SICH DIE OHREN
        ZU, UND DER ALTE MASCHINIST LÄCHELT ZUFRIEDEN.
    - name: Nachricht 4
      schluessel: LEUCHTTURM
      klar: >-
        WENN DU DIESE ZEILEN LIEST, HAST DU EINEN SCHLÜSSEL GEFUNDEN, DER ZEHN BUCHSTABEN LANG IST.
        DAS IST SCHON EIN ORDENTLICHES STÜCK ARBEIT, DENN JEDE SPALTE HAT NUR NOCH WENIGE BUCHSTABEN.
        TROTZDEM VERRÄT SICH DIE SPRACHE, WEIL DAS E SO OFT VORKOMMT, DASS ES AUCH IN KLEINEN
        STÜCKEN HERAUSSTICHT. GLÜCKWUNSCH, DU BIST EIN ECHTER CODEKNACKER GEWORDEN, UND DAS SOGAR
        OHNE DIE HILFE EINES ROTEN TELEFONS ODER EINES GEHEIMEN HANDBUCHS AUS DEM TRESOR.
    - name: Nachricht 5
      schluessel: AXT
      klar: "KURZ UND KNAPP: DAS PASSWORT FÜR DIE TÜR ZUM GARTEN IST ROTKEHLCHEN. BITTE NICHT WEITERSAGEN."
  teilschritte:
    - titel: Mit Schlüsselwort zurück
      text: "`zurueck(geheim, \"KAT\")` macht aus der Probe wieder Klartext: der erste Buchstabe rückt um K zurück, der zweite um A, der dritte um T, dann wieder K."
    - titel: Länge bekannt
      text: "`knacke_laenge(geheim, 5)`: Bei bekannter Länge ist jede fünfte Stelle eine Cäsar-Nachricht für sich."
      nachrichten: [Länge bekannt]
    - titel: Länge finden
      text: "`knacke(geheim)` findet die Länge des Schlüsselworts selbst."
      nachrichten: [Nachricht 1, Nachricht 2]
    - titel: Alle Nachrichten
      text: "Zum Schluss die versteckten Nachrichten, auch eine mit einem Schlüssel aus zehn Buchstaben."
      nachrichten: alle
  sterne: {ms: 200, zeichen: 820}
---

# Vigenère knacken

Ein Cäsar war zu leicht? Dann nimm für jeden Buchstaben eine andere Verschiebung, reihum nach einem Schlüsselwort. Mit dem Wort KAT rückt der erste Buchstabe um K (10) weiter, der zweite um A (0), der dritte um T (19), dann wieder um K. Dreihundert Jahre lang hieß das "die unknackbare Chiffre".

Bis jemand merkte: Kennt man die Länge des Worts, zerfällt der Text in lauter kleine Cäsar-Nachrichten, und die knackst du seit Level 1 im Schlaf. Bleibt die Frage, wie lang das Wort ist. Auch das verrät die Häufigkeit.

Schreib `knacke(geheim)`. Gezählt wird nur über A bis Z: Leerzeichen, Satzzeichen und Umlaute bleiben stehen und schieben den Schlüssel nicht weiter.
