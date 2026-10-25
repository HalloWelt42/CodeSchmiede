runden = 0
bestzeit = 0


def runde(zeit):
    global runden, bestzeit
    runden += 1
    if runden == 1 or zeit < bestzeit:
        bestzeit = zeit


while True:
    zeit = int(input())
    if zeit == 0:
        break
    runde(zeit)
print("Runden:", runden)
print("Bestzeit:", bestzeit)
