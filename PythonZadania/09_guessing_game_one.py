import random

number = int(random.random()*9)+1
#print (number)

x=0
while True:
    print("Zgadnij jaka liczbe wylosowal komputerek: (1-9)")
    zgaduj = int(input())
    x += 1
    if zgaduj == number:
        if x<2:
            print ("Kuwa zgadla(e)s za {} razem".format(x))
        else:
            print ("Troche Ci to zajelo, dopiero za {} razem lamusku".format(x))
        break
    elif zgaduj < number:
        print ("Hehe za maly numerek")
    elif zgaduj > number:
        print ("Za duzy kurde mniejszy podaj")