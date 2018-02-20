print("Podaj liczbe ktora chcesz zbadac: ")
dzielna = int(input())
dzielniki = []
for i in range (1,dzielna+1):
    if dzielna % i == 0:
        dzielniki.append(i)
print (dzielniki)