#filter(funkcja, sekwencja) zwraca sekwencje (tego samego typu, gdy to możliwe)
#zawierającą te elementy z listy wejściowej, dla których wywołanie funkcja(element)
#zwróci wartość prawdziwą. Oto przykład obliczania liczb pierwszych:

def f(x):
    return x % 2 != 0 and x % 3 != 0

x = list(filter(f, range(2,100)))
print (x)