kolonie = ["Pia", "Pit", "Paul", "Polly", "Pit"]


def stelle(namen, gesucht):
    for i in range(len(namen)):
        if namen[i] == gesucht:
            return i
    return -1


ergebnis = stelle(kolonie, input())
if ergebnis == -1:
    print("Nicht gefunden")
else:
    print("Stelle", ergebnis)
