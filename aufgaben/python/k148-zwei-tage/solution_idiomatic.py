montag = set()
while True:
    name = input()
    if name == "ende":
        break
    montag.add(name)
dienstag = set()
while True:
    name = input()
    if name == "ende":
        break
    dienstag.add(name)
print("Beide Tage:", sorted(montag & dienstag))
print("Nur Montag:", sorted(montag - dienstag))
print("Insgesamt:", len(montag | dienstag))
