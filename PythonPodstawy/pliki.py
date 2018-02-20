# open ("nazwa pliku","atrybut")
# atrybuty:
# r - czytanie
# r+ - czytanie i zapisywanie
# w - zapisywanie, tworzenie jesli nie istnieje, skasuje wartosc pliku
# w+ - czytanie, zapisywanie, tworzenie jesli nie istnieje, skasuje wartosc pliku
# a - zapis i utworzenie, kursor na koncu
# a+ - odczytywanie, zapisanie, utworzenie, kursor na koncu

x = open("test2.txt",'r+')

#kasuje to co jest po kursorze
#x.truncate()

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

x.write(line1)
x.write("\n")
x.write(line2)
x.write("\n")
x.write(line3)
