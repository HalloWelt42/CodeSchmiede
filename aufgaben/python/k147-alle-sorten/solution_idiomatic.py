pit = {"Vanille", "Erdbeer", "Nuss", "Zitrone"}
pia = {"Nuss", "Schoko", "Vanille"}
paul = {"Minze", "Schoko"}
alle = pit | pia | paul
print(len(alle), "Sorten")
print(sorted(alle))
