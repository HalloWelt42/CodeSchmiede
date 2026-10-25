def zinsen(betrag, prozent):
    return round(betrag * (1 + prozent / 100), 2)


betrag = int(input())
prozent = int(input())
jahre = int(input())
for jahr in range(1, jahre + 1):
    betrag = zinsen(betrag, prozent)
    print(f"Jahr {jahr}: {betrag}")
