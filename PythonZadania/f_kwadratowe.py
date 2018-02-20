# __funkcje__ to wymuszanie pewnych zachowan ktore chce zaimplementowac w funkcji
# google -> data model python
# x + y -> __add_
# init x -> __init__
# repr(x) -> __repr__

class Polynomial:
    def __init__(self, *coeffs):    #metoda ktora pozwala nam konstruowac obiekty juz w klasie
        self.coeffs = coeffs

    def __repr__(self):             #metoda ktora reprezentuje nasza klase gdy uzyjemy print p1, lub print p2
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):       #metoda ktora mowi pythonowi jak dodaje sie elementy rownania kwadratowego
        print (list(zip(self.coeffs, other.coeffs)))
        return Polynomial(*(x+y for x,y in zip(self.coeffs, other.coeffs)))     # idzie po wszystkich elementach i je dodaje

    def __len__ (self):             #metoda
        return len(self.coeffs)

    def __call__(self):             #core pattern: protocol view of python + built-in inheritance protocol + caveats
        pass

p1 = Polynomial(1,2,3)
p2 = Polynomial(3,4,3)
p3 = Polynomial(2,3,4)

print (p1)
print (p2)
print (p3)

print (p1+p2+p3)

print (len(p1))