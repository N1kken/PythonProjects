print("Podaj numer:")
x = int(input())

if x % 2 == 0:
    print("liczba parzysta")
else:
    print("liczba nieparzysta")

if x % 4 == 0:
    print("liczba podzielna przez 4")

print("sprawdz czy jest podzielna przez inna liczbe: ")
y = int(input())

if x % y == 0:
    print("jest!")
else:
    print("no nie jest")