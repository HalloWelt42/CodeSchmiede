def ist_gerade(n):
    return n % 2 == 0


for i in range(1, int(input()) + 1):
    if ist_gerade(i):
        print(i)
