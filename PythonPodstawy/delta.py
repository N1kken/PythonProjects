import time
import math
print("LICZ DELTE")
time.sleep(1)
print("Witaj, podaj wspolczynniki rownania kwadratowego: ax^2+bx+c=0!")

print("Podaj a:")
a=int(input())
print("Podaj b:")
b=int(input())
print("Podaj c:")
c=int(input())

delta=math.pow(b,2)-4*a*c

if delta == 0:
    m1 = -b/(2*a)
    print("Funkcja ma jedno miejsce zerowe w punkcie {}".format(m1))
elif delta>0:
    m1 = (-b - math.sqrt(delta)) / (2 * a)
    m2 = (-b + math.sqrt(delta)) / (2 * a)
    print("Funkcja ma dwa miejsca zerowe w punktach {} , {}".format(m1,m2))
else: print("Funkcja nie ma miejsc zerowych")