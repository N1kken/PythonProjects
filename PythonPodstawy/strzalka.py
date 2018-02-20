print("PROGRAM RYSUJĄCY STRZALKĘ O ZADANEJ WYSOKOSCI")

print("Podaj wysokosc strzalki (x>1)")

#POBIERANIE WYSOKOSCI STRZALKI
x = int(input())
y=x
x -= 1
for j in range (y):
    for i in range (x):
        print (" ", end='')
    for k in range (2*y-2*x-1):
        print ("x", end='')
    x -= 1
    print ()

#TWORZENIE "NÓŻKI"
for i  in range (4):
    for j in range (y-2):
        print (" ", end='')
    print ("| |")

