"""
Idiomatische Lösung: String-Komposition vermeidet doppelte Modulo-Prüfung
und Redundanz. Der Else-Fall ergibt sich automatisch durch den leeren String.
"""


def fizzbuzz(n: int) -> str:
    teil = ("Fizz" if n % 3 == 0 else "") + ("Buzz" if n % 5 == 0 else "")
    return teil or str(n)
