geheim = 7
versuche = 0
while True:
    tipp = int(input())
    versuche += 1
    if tipp < geheim:
        print("zu klein")
    elif tipp > geheim:
        print("zu groß")
    else:
        print("getroffen!")
        break
print("Versuche:", versuche)
