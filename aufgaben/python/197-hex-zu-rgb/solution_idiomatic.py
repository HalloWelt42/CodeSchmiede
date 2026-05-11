def hex_zu_rgb(s: str) -> list[int]:
    s = s.lstrip("#")
    if len(s) != 6 or not all(c in "0123456789abcdefABCDEF" for c in s):
        return [0, 0, 0]
    return [int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16)]
