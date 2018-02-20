#map(funkcja, sekwencja) wywołuje funkcja(element) dla każdego
#elementu listy wejściowej i zwraca listę wartości zwróconych
#przez funkcja. Na przykład, aby obliczyć sześcian dla każdego
#elementu z ciągu liczb:

import fcje1

def szescian(x):
    return x*x*x

x = list(map(szescian, range(1, 11)))
print (x)

sekw = range(1,11)
y = list(map(szescian,sekw))
print (y)

del y[0]
print (y)

print("")
print("TUPLE")

#tuple/krotki nawiasy okragle, w listach te inne [],
#sa stale: nie dziala append extend remove pop
#to po co one?
#d  zialaja szybciej od list
#   bezpieczenstwo - jesli chcemy by nasze dane pozostaly niezmienione
#   moze zostac wykorzystana jako klucz (jak w slownikach) jesli zawiera lancuchy znakow, liczb,
#i inne slownikowo bezpieczne krotki (tzn takie bez zagniezdzonych list)
#   do formatowania tekstu

t = (12345,67890,'czesc')
print (t)
u = t, (1,2,3,4,5)
print (u)

print("")
print("SLOWNIK")

tel = {'jack': 4098, 'sape': 4139}
print ("poczatkowy slownik:", tel)
tel['guido'] = 4127
print ("po dodaniu guido: ", tel)
print ("pokazanie wartosci dla klucza jack: ", tel['jack'])
del tel['sape']
tel['irv'] = 4127
print ("po usunieciu sape i dodaniu irv: ", tel)
print ("wyswietlenie kluczy: ", tel.keys())