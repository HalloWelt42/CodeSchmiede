gesehen = set()
while True:
    art = input()
    if art == "ende":
        break
    if art in gesehen:
        print("kenne ich:", art)
    else:
        print("neu:", art)
        gesehen.add(art)
