#Z kuli o promieniu r1 wycięto kule o promieniu r2 oblicz objętość powstałej fugury.  
from math import pi
def kula1():
    r1 = float(input("podaj rozmiar pierwszej kuli: "))
    return (4*pi*r1**2)/3
def kula2():
    r2 = float(input("podaj rozmiar drugiej kuli:"))
    return (4*pi*r2**2)/3
print("Oto objętość nowej figury:", kula1() - kula2() )