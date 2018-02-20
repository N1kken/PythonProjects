def printme(liczba):
    for i in range (liczba):
        print("Hello world!")

#printme(5)

def mnozenie(a,b):
    print(a*b)

def dodawanie(a,b):
    return a+b

def dzielenie(x,b=1):
    #a=int(input("podaj liczbe:"))
    return x/b

#dodawanie (2,2)
#dzielenie(b=4,a=8)

#print("Podaj liczbe:", x)
#x=int(input())
#y=int(input())
dodawanie(5,5)



def print2(*args): # *args dotyczy list, **kwargs dotyczy slownikow
    arg1,arg2 = args
    print("arg1: %r, arg2: %r" % (arg1,arg2))

def print2a(arg1,arg2):
    print("arg1: %r, arg2: %r" % (arg1,arg2))

