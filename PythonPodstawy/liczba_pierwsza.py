print("PROGRAM SPRAWDZAJACY CZY ZADANA LICZBA JEST LICZBĄ PIERWSZĄ")

print("Jaką liczbę chcesz zbadać?")
x = int(input())
for i in range (x):
    i += 1
    if i != 1 & i != x:
        if x % i != 0:
            continue
            print ("kupa")
        if x % i == 0:
            print("%d nie jest liczbą pierwszą" % x)
            break
        else:
            print("%d jest liczbą pierwszą" % x)
            break
