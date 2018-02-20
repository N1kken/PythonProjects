string = "Ala ma kota, kota ma Ale"
lista = string.split(' ')
lista2 = ["Reka", "Noga", "Mozg"]

while len(lista) != 8:
    nastepny = lista2.pop(0)
    print(nastepny)
    #lista.append(nastepny)
    lista[len(lista):] = [nastepny]
print (lista)

#LISTY METODY:
#append(x) - dodaje element do konca listy == lista[len(lista):] = [x]
#extend(L) - rozszerza liste poprzez dolaczenie wszystkich elementow podanej listy L == lista[len(lista):] = L
#insert(i,x) - wstawia element x na podana pozycje listy
#remove(x) - usuwa pierwszy napotkany element z listy ktorego wartoscia jest x.
#pop([i]) - usuwa element z podanej pozycji na liscie i zwraca go jako wynik. lista.pop() zwraca ostatni element.
#index(x) - zwraca indeks pierwszego elementu listy ktorego wartoscia jest x.
#count(x) - zwraca liczbe wystapien elementu x na liscie
#sort() - sortuje elementy na liscie
#reverse() - odwraca porzadek elementow listy


#LISTA JAKO STOS:
# stos = [3, 4, 5]
# stos.append(6)
# stos.append(7)
# stos.pop()
# stos.pop()


#LISTA JAKO KOLEJKA
#kolejka = ["Eric", "John", "Michael"]
#kolejka.append("Terry")           # przybywa Terry
#kolejka.append("Graham")          # przybywa Graham
#kolejka.pop(0)
#kolejka.pop(0)


