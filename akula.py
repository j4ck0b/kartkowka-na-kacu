from math import pi
def szescian():
    a = float(input("podaj a: "))
    return 6 * a**2
def kula():
    r = float(input("podaj r: "))
    return 4 * pi * r**2
print(szescian() - kula())
print("pole kuli:", kula)
print("pole kwadratu", szescian)