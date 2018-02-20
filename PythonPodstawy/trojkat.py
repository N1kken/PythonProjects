import time
print("PROGRAM WERYFIKUJACY BUDOWE TROJKATA")
time.sleep(1)
print("Witaj, podaj 3 boki z ktorych chcialbys zbudowac trojkat!")

print("Podaj a:")
a=int(input())
print("Podaj b:")
b=int(input())
print("Podaj c:")
c=int(input())

if (a+b>c | a+c>b) | b+c>a:
    if (a^2+b^2==c^2 | a^2+c^2==b^2) | b^2+c^2==a^2:
        print("Da sie zbudowac trojkat prostokatny!")
    else:
        print("Da sie zbudowac trojkat")
else:
    print ("Nie da się zbudować trójkąta")