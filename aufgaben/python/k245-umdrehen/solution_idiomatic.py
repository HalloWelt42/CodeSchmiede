def umdrehen(text):
    if text == "":
        return ""
    return umdrehen(text[1:]) + text[0]


print(umdrehen(input()))
