import os
print ("Witaj w grze kamien papier nozyce")
print ("Podaj imie gracza nr 1:")
player1 = input()
print ("Dej imie gracza nr 2:")
player2 = input()

x = True
while x:
    print("kamien, papier czy nozyce {}? (k p n)".format(player1))
    p1wybor = input()
    # os.system("cls")

    for i in range(15):
        print("-")
    print("kamien, papier czy nozyce {}? (k p n)".format(player2))
    p2wybor = input()
    if p1wybor == p2wybor:
        print ("remis")
        print ("dogrywka!")
        pass
    elif p1wybor == 'k':
        if p2wybor == 'n':
            print ("Wygral(a) {}".format(player1))
            x = False
        else:
            print ("Wygral(a) {}".format(player2))
            x = False
    elif p1wybor == 'n':
        if p2wybor == 'p':
            print("Wygral(a) {}".format(player1))
            x = False
        else:
            print("Wygral(a) {}".format(player2))
            x = False
    elif p1wybor == 'p':
        if p2wybor == 'k':
            print("Wygral(a) {}".format(player1))
            x = False
        else:
            print("Wygral(a) {}".format(player2))
            x = False
    if x == False:
        print("Gracie dalej? t/n")
        next = input()
        if next == 't':
            x = True
        else:
            x = False