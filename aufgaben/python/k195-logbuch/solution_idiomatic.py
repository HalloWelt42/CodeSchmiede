def eintragen(text):
    with open("logbuch.txt", "a") as datei:
        datei.write(text + "\n")


with open("logbuch.txt", "w") as datei:
    datei.write("Logbuch\n")
while True:
    text = input()
    if text == "ende":
        break
    eintragen(text)
with open("logbuch.txt") as datei:
    print(datei.read())
