def potenz(basis, exponent):
    if exponent == 0:
        return 1
    return basis * potenz(basis, exponent - 1)


print(potenz(int(input()), int(input())))
