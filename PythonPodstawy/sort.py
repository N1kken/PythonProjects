import time
print("PROGRAM SORTUJACY 3 LICZBY")
time.sleep(1)
print("Witaj, podaj 3 liczby ktore chcesz posortowac!")

print("Podaj a:")
a=int(input())
print("Podaj b:")
b=int(input())
print("Podaj c:")
c=int(input())

print("Chcesz posortowac rosnąco(1) czy malejąco(2)?")
tryb=int(input())
if a>=b & b>=c:
    x1=a
    x2=b
    x3=c
elif a>=c & c>=b:
    x1=a
    x2=c
    x3=b
elif b>=a & a>=c:
    x1=b
    x2=a
    x3=c
elif b>=c & c>=a:
    x1=b
    x2=c
    x3=a
elif c>=a & a>=b:
    x1=c
    x2=a
    x3=b
else:
    x1=c
    x2=b
    x3=a
if tryb == 2:
    print("{} {} {}".format(x1,x2,x3))
else:
    print("{} {} {}".format(x1,x2,x3))