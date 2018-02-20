import turtle

def spirala(zwoje, wielkosc):
    for i in range (zwoje):
        turtle.circle (wielkosc*(i+1),180)

spirala (25,10)