---
schema_version: 1
id: c001-caesar
revision: 1
titel: Cäsar knacken
sprache: python
task_type: codes
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 20
schaetz_minuten: 20
tags: [codes, strings, max]
voraussetzungen: []
quelle:
  url: null
  notiz: Codes knacken, Level 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 10
hints:
  - kosten: 1
    text: "`ABC.index(c)` macht aus einem Buchstaben eine Zahl von 0 bis 25, `ABC[(zahl + n) % 26]` wieder einen Buchstaben. Durch `% 26` geht es hinter Z wieder bei A los."
  - kosten: 1
    text: "Probier alle 26 Verschiebungen und gib jedem Versuch Punkte: für jeden Buchstaben seinen Anteil aus `DEUTSCH`. Viele E und N geben viele Punkte. `max(versuche, key=punkte)` nimmt den besten."
starter_code: |
  ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


  def schiebe(text, n):
      # jeden Buchstaben A bis Z um n Stellen weiterrücken, alles andere bleibt
      return text


  def knacke(geheim):
      return geheim
codes:
  verfahren: caesar
  bereit: [DEUTSCH]
  sichtbar:
    - name: Probe
      klar: "DER SCHATZ LIEGT UNTER DEM ALTEN LEUCHTTURM."
      schluessel: 3
      funktion: schiebe
      mit: [-3]
    - name: Nachricht 1
      klar: "TREFFPUNKT IST DER FISCHWAGEN AM HAFEN, PÜNKTLICH UM ACHT UHR. BRINGT HERINGE MIT."
      schluessel: 7
    - name: Nachricht 2
      klar: "WER DIESEN SATZ LESEN KANN, HAT DEN ERSTEN CODE GEKNACKT. WEITER SO!"
      schluessel: 11
  versteckt:
    - name: Nachricht 3
      klar: "DIE KATZE SITZT AUF DEM WARMEN OFEN UND SCHNURRT. NIEMAND STÖRT SIE."
      schluessel: 19
    - name: Nachricht 4
      klar: "MORGEN REGNET ES IN DER GANZEN STADT, ALSO SCHIRM EINPACKEN."
      schluessel: 25
    - name: Kurze Nachricht
      klar: "TREFFEN UM NEUN"
      schluessel: 13
  teilschritte:
    - titel: Zurückschieben
      text: "Mit bekanntem Schlüssel entschlüsseln: `schiebe(geheim, -3)` macht aus der Probe wieder Klartext."
    - titel: Alle 26 probieren
      text: "`knacke(geheim)` probiert jede Verschiebung und nimmt die, die am meisten nach Deutsch aussieht."
      nachrichten: [Nachricht 1, Nachricht 2]
    - titel: Alle Nachrichten
      text: "Zum Schluss die versteckten Nachrichten, auch eine ganz kurze."
      nachrichten: alle
  sterne: {ms: 100, zeichen: 260}
---

# Cäsar knacken

Julius Cäsar hat jeden Buchstaben seiner Briefe um ein paar Stellen im Alphabet verschoben. Aus A wird bei drei Stellen D, aus Z wird C. Wir haben abgefangene Nachrichten, aber keinen Schlüssel.

Schreib eine Funktion `knacke(geheim)`, die den Klartext zurückgibt. Rate nicht für einen Text: geprüft wird auch mit versteckten Nachrichten und anderen Verschiebungen. Verschlüsselt sind nur A bis Z; Leerzeichen, Satzzeichen und Umlaute bleiben, wie sie sind (Vorsicht: `"Ä".isalpha()` ist auch wahr).

Rechts kannst du die Verschiebung von Hand probieren. Das Balkenbild zeigt, wie oft jeder Buchstabe vorkommt; passt es zur goldenen Linie des Deutschen, ist der Schlüssel gefunden. Genau das soll dein Programm auch tun, nur schneller und ohne zu blinzeln.
