a = int(input())
zeichen = input()
b = int(input())
if zeichen == "+":
    print(a + b)
elif zeichen == "-":
    print(a - b)
elif zeichen == "*":
    print(a * b)
elif zeichen == "/":
    if b == 0:
        print("Teilen durch 0 geht nicht.")
    else:
        print(a / b)
else:
    print("Unbekanntes Zeichen.")
