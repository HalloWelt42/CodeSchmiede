def fakultaet(n):
    if n == 0:
        return 1
    return n * fakultaet(n - 1)


print(fakultaet(5))
