import math

x = float((input('Введите x: ')))

def abirvalg(x):

    a = math.sin(x)

    b = x - 2*math.cos(x)

    d = 2*math.tan(x) - 1

    c = math.sqrt(d/x)

    alala = a/b + c

    print(alala)

b = abirvalg(x)


try:
    abirvalg(x)

    if x == 0:
        raise ZeroDivisionError

except ZeroDivisionError:
    print("Грустно")
