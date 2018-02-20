#  import math

A = list(range(24,80))
B = list(range(24,80))
C = list(range(24,80))
D = list(range(24,80))

#print (A)

#print("Podaj modul")
#modul=float(input())
#skok = 3.1415*modul
#print (modul)
#print (skok)
skok = 3.1415
wynik = []
for i in A:
    for j in B:
        for k in C:
            for l in D:
                wynik.append (math.fabs(skok-(i*k)/(j*l)*127/25))

najlepszy = max(wynik)
print (najlepszy)
#print (wynik)