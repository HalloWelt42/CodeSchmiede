def quersumme(n):
    if n < 10:
        return n
    return n % 10 + quersumme(n // 10)


print("Quersumme:", quersumme(int(input())))
