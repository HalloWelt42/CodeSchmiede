_TABELLE = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z",
    "-----": "0", ".----": "1", "..---": "2", "...--": "3",
    "....-": "4", ".....": "5", "-....": "6", "--...": "7",
    "---..": "8", "----.": "9",
}


def morse_decode(morse: str) -> str:
    if not morse:
        return ""
    woerter: list[str] = []
    for wort in morse.split(" / "):
        zeichen = [_TABELLE[t] for t in wort.split() if t in _TABELLE]
        if zeichen:
            woerter.append("".join(zeichen))
    return " ".join(woerter)
