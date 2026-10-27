---
schema_version: 1
id: c005-schichten
revision: 1
titel: Schicht um Schicht
sprache: python
task_type: codes
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 45
schaetz_minuten: 30
tags: [codes, base64, hex, schleifen]
voraussetzungen: []
quelle:
  url: null
  notiz: Codes knacken, Level 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 10
hints:
  - kosten: 1
    text: "Hex besteht nur aus 0 bis 9 und a bis f und hat eine gerade Länge: `bytes.fromhex(text).decode()`. Base64 hat A bis Z, a bis z, 0 bis 9, + und / und eine Länge, die durch 4 teilbar ist, oft mit = am Ende: `base64.b64decode(text).decode()`."
  - kosten: 1
    text: "Prüf Hex vor Base64: Ein Hex-Text wäre auch gültiges Base64. Und solange sich eine Schale abziehen lässt, zieh sie ab; was übrig bleibt, ist ein Cäsar aus Level 1."
starter_code: |
  import base64

  ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


  def schale(text):
      # eine Schicht abziehen: Hex oder Base64
      return text


  def knacke(geheim):
      return geheim
codes:
  verfahren: schichten
  bereit: [DEUTSCH]
  sichtbar:
    - name: Probe
      klar: "DIE ERSTE SCHALE IST AB. DARUNTER LIEGT KLARTEXT."
      schluessel: [base64]
      funktion: schale
    - name: Zwei Schalen
      klar: "ZWIEBELN HABEN SCHALEN, UND MANCHE NACHRICHTEN AUCH."
      schluessel: [base64, hex]
    - name: Nachricht 1
      klar: "WER BIS HIERHIN GEKOMMEN IST, KENNT SCHON DREI SCHICHTEN: CÄSAR, BASE64 UND HEX."
      schluessel: ["caesar:5", base64]
    - name: Nachricht 2
      klar: "DIE KISTE IM KELLER ENTHÄLT NUR ALTE ZEITUNGEN UND EINEN EINZELNEN SOCKEN."
      schluessel: ["caesar:12", hex, base64]
  versteckt:
    - name: Nachricht 3
      klar: "HEX ALLEIN IST KEINE VERSCHLÜSSELUNG, NUR EINE ANDERE SCHREIBWEISE."
      schluessel: ["caesar:20", hex]
    - name: Nachricht 4
      klar: "AUCH ZWEIMAL BASE64 HINTEREINANDER MACHT EINEN TEXT NICHT SICHERER, NUR LÄNGER."
      schluessel: ["caesar:7", base64, base64]
    - name: Nachricht 5
      klar: "DREI SCHALEN UND EIN CÄSAR: DAS IST SCHON FAST EIN SPORT."
      schluessel: ["caesar:3", hex, base64, hex]
  teilschritte:
    - titel: Eine Schale
      text: "`schale(text)` erkennt Base64 oder Hex und zieht eine Schicht ab."
    - titel: Alle Schalen
      text: "`knacke(geheim)` zieht Schicht um Schicht ab, bis keine mehr da ist."
      nachrichten: [Zwei Schalen]
    - titel: Zum Schluss Cäsar
      text: "Unter den Schalen steckt noch ein Cäsar. Den kennst du schon."
      nachrichten: [Nachricht 1, Nachricht 2]
    - titel: Alle Nachrichten
      text: "Zum Schluss die versteckten Nachrichten, mit bis zu drei Schalen."
      nachrichten: alle
  sterne: {ms: 20, zeichen: 560}
---

# Schicht um Schicht

Base64 und Hex sind keine Verschlüsselung, sondern nur andere Schreibweisen für dieselben Bytes. Base64 packt drei Bytes in vier Zeichen und steckt in jeder E-Mail mit Anhang, Hex schreibt jedes Byte als zwei Ziffern. Wer etwas verstecken will, wickelt trotzdem gern ein paar davon übereinander und hofft, dass niemand nachsieht.

Wir sehen nach. Schreib `knacke(geheim)`: Zieh die Schalen ab, solange es welche gibt, und knack am Ende den Cäsar darunter. Welche Schalen in welcher Reihenfolge kommen, verrät dir niemand; das muss dein Programm am Text selbst erkennen.
