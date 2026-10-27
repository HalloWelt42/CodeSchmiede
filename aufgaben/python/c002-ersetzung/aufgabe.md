---
schema_version: 1
id: c002-ersetzung
revision: 1
titel: Ersetzung und Häufigkeit
sprache: python
task_type: codes
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 60
schaetz_minuten: 45
tags: [codes, dicts, sortieren, optimierung]
voraussetzungen: []
quelle:
  url: null
  notiz: Codes knacken, Level 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 40
hints:
  - kosten: 1
    text: "Erste Vermutung: Zähl die Buchstaben im Geheimtext und sortiere sie nach Häufigkeit, ebenso die Buchstaben aus `DEUTSCH`. Der häufigste Geheimbuchstabe wird E, der zweithäufigste N und so weiter."
  - kosten: 1
    text: "Verbessern: Gib einem Versuch Punkte nach seinen Buchstabenpaaren, `math.log(PAARE.get(paar, 0.0003))` für jedes Paar, mit `_` für Wortanfang und Wortende. Dann tausch zwei Buchstaben der Zuordnung und behalte den Tausch, wenn die Punkte steigen. So lange, bis kein Tausch mehr hilft."
  - kosten: 2
    text: "Bleibt es hängen: ein paar zufällige Tausche und noch einmal klettern, die beste Zuordnung merken. Schneller wird es, wenn du die Paare des Geheimtexts einmal zählst und die Punkte aus dieser Zählung rechnest statt aus dem ganzen Text."
starter_code: |
  ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


  def ersetze(geheim, alphabet):
      # alphabet[0] steht im Geheimtext für A, alphabet[1] für B ...
      return geheim


  def knacke(geheim):
      return geheim
codes:
  verfahren: ersetzung
  bereit: [DEUTSCH, PAARE]
  mindestens: 0.8
  sichtbar:
    - name: Probe
      klar: "DER KAPITÄN STAND AM RUDER UND SAH IN DEN NEBEL. IRGENDWO DORT LAG DIE INSEL."
      schluessel: QWERTZUIOPASDFGHJKLYXCVBNM
      funktion: ersetze
      mit: [QWERTZUIOPASDFGHJKLYXCVBNM]
      mindestens: 1.0
    - name: Erste Vermutung
      mindestens: 0.4
      schluessel: 11
      klar: >-
        IM HAFEN WAR ES STILL. NUR DIE MÖWEN SCHRIEN, UND DAS WASSER SCHLUG LEISE GEGEN DIE ALTEN BOOTE.
        DER WIRT DER KLEINEN KNEIPE AM KAI WISCHTE DIE TISCHE AB UND WARTETE AUF DIE ERSTEN GÄSTE.
        SEIT VIELEN JAHREN KAMEN JEDEN ABEND DIESELBEN LEUTE: FISCHER, MATROSEN UND EIN ALTER MANN,
        DER IMMER AM FENSTER SITZEN BLIEB UND NIEMANDEM SEINEN NAMEN SAGTE.
    - name: Nachricht 1
      schluessel: 3
      klar: >-
        ES WAR EINMAL EIN KLEINER ROBOTER, DER IN EINER ALTEN WERKSTATT AM RANDE DER STADT WOHNTE.
        JEDEN MORGEN PUTZTE ER DIE WERKZEUGE, SORTIERTE DIE SCHRAUBEN NACH IHRER LÄNGE UND WARTETE
        AUF DEN MEISTER. DOCH EINES TAGES KAM DER MEISTER NICHT. DER ROBOTER WARTETE EINEN TAG, DANN
        ZWEI TAGE, DANN EINE GANZE WOCHE. AM ENDE FASSTE ER EINEN MUTIGEN ENTSCHLUSS: ER WOLLTE
        DEN MEISTER SUCHEN GEHEN. ER PACKTE EINE KLEINE TASCHE MIT ÖL, EINER LAMPE UND EINEM STADTPLAN
        UND MACHTE SICH AUF DEN WEG IN DIE WEITE, LAUTE WELT.
    - name: Nachricht 2
      schluessel: 17
      klar: >-
        DIE ERSTEN RECHENMASCHINEN WAREN SO BREIT WIE EIN GANZES ZIMMER UND BRAUCHTEN VIEL STROM.
        SIE RECHNETEN MIT RÖHREN, DIE OFT DURCHBRANNTEN, UND EIN TEAM VON TECHNIKERN WAR DAMIT
        BESCHÄFTIGT, SIE ZU ERSETZEN. HEUTE STECKT IN JEDEM TELEFON EIN RECHNER, DER TAUSENDMAL
        SCHNELLER IST ALS DIESE RIESEN. DOCH DIE GRUNDIDEE IST DIESELBE GEBLIEBEN: EIN PROGRAMM SAGT
        DER MASCHINE SCHRITT FÜR SCHRITT, WAS SIE TUN SOLL, UND DIE MASCHINE RECHNET OHNE PAUSE,
        OHNE FEHLER UND OHNE SICH ZU BESCHWEREN.
  versteckt:
    - name: Nachricht 3
      schluessel: 42
      klar: >-
        IN DER NACHT ZOG EIN STURM ÜBER DAS LAND. DER WIND RISS AN DEN DÄCHERN, DIE BÄUME BOGEN
        SICH, UND DER REGEN PRASSELTE GEGEN DIE FENSTER. DIE KINDER LAGEN WACH IN IHREN BETTEN UND
        HÖRTEN DEM DONNER ZU. ALS ES ENDLICH HELL WURDE, WAR DER STURM VORBEI. DIE SONNE SCHIEN
        ÜBER DIE NASSEN WIESEN, UND DIE VÖGEL SANGEN, ALS WÄRE NICHTS GESCHEHEN. NUR EIN PAAR
        ÄSTE LAGEN AUF DEM WEG, UND DER NACHBAR SUCHTE SEINE MÜLLTONNE IM GANZEN DORF.
    - name: Nachricht 4
      schluessel: 99
      klar: >-
        WER EINE NEUE SPRACHE LERNT, FÄNGT MIT EINFACHEN WÖRTERN AN: HALLO, DANKE, BITTE. DANN
        KOMMEN GANZE SÄTZE, UND IRGENDWANN KANN MAN EIN KLEINES GESPRÄCH FÜHREN. MIT DEM
        PROGRAMMIEREN IST ES GENAUSO. ZUERST SCHREIBT MAN EINE ZEILE, DIE EINEN TEXT AUSGIBT.
        DANN EINE SCHLEIFE, DIE BIS ZEHN ZÄHLT. UND EINES TAGES BAUT MAN EIN SPIEL, EINE WEBSEITE
        ODER EIN PROGRAMM, DAS GEHEIME NACHRICHTEN KNACKT. DER WEG DORTHIN BESTEHT AUS VIELEN
        KLEINEN SCHRITTEN, UND JEDER EINZELNE ZÄHLT.
  teilschritte:
    - titel: Zurückersetzen
      text: "Mit bekannter Mischung entschlüsseln: `ersetze(geheim, \"QWERTZ...\")` macht aus der Probe wieder Klartext."
    - titel: Erste Vermutung
      text: "`knacke(geheim)` ordnet die Geheimbuchstaben nach Häufigkeit den deutschen zu. Damit stimmen schon 40 % der Buchstaben."
      nachrichten: [Erste Vermutung]
    - titel: Paare verbessern
      text: "Tauschen, solange die Buchstabenpaare deutscher werden, bis 80 % der Buchstaben stimmen. Den Rest liest ein Mensch von selbst."
      nachrichten: [Nachricht 1, Nachricht 2]
    - titel: Alle Nachrichten
      text: "Zum Schluss die versteckten Nachrichten, jede mit einer anderen Mischung."
      nachrichten: alle
  sterne: {ms: 4000, zeichen: 1200}
---

# Ersetzung und Häufigkeit

Diesmal rückt nicht jeder Buchstabe gleich weit, sondern jeder bekommt einen eigenen Ersatz: A wird vielleicht Q, B wird W, C wird E. Das sind 26 mal 25 mal 24 und so weiter Möglichkeiten, eine Zahl mit 27 Stellen. Alle durchprobieren? Da wäre die Sonne schneller ausgebrannt.

Zum Glück verrät sich Deutsch: E ist mit Abstand der häufigste Buchstabe, dann kommen N, I, R, S und T. Und manche Paare kommen ständig vor (EN, ER, CH, SCH), andere nie (QX). Damit kommst du ohne Schlüssel sehr weit.

Schreib `knacke(geheim)`. Hier muss nicht jeder Buchstabe stimmen: ab 80 % richtigen Buchstaben gilt eine Nachricht als geknackt. Die seltenen Buchstaben wie J, Q und Y kommen in einem Text so selten vor, dass auch Profis sie aus dem Zusammenhang erraten.

Bereit stehen `DEUTSCH` (Anteil je Buchstabe in Prozent) und `PAARE` (Anteil je Buchstabenpaar in Promille, `_` steht für Wortanfang und Wortende: `"_D"` heißt, ein Wort beginnt mit D).
