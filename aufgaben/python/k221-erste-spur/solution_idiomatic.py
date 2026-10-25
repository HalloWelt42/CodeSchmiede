import re

treffer = re.search(r"\d+", "Polly fing 7 Fische")
print(treffer.group())
