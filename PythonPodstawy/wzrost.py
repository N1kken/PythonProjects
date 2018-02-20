import time
print("PROGRAM KLASYFIKUJACY WZROST")
time.sleep(1)
print("Witaj, podaj swoje imie!")
imie=input()
plec=imie[-1]
if plec == "a":
    plec = "kobieta"
    print("powiedz mi ile masz cm wzrostu, a powiem Ci czy jesteś wysoka :)")
else:
    plec="mezczyzna"
    print("powiedz mi ile masz cm wzrostu, a powiem Ci czy jesteś wysoki :)")
wzrost=int(input())
if plec == "kobieta":
    if wzrost > 250:
        print ("{}, nie oszukuj, nie mozesz miec az tyle!".format(imie))
    elif wzrost > 180:
        print ("{}, jestes wysoka!".format(imie))
    elif wzrost > 160:
        print("{}, jestes ani za wysoka, ani za mała, w sam raz!".format(imie))
    else:
        print("{}, nie przejmuj sie, male jest piekne!".format(imie))
if plec == "mezczyzna":
    if wzrost > 250:
        print ("{}, nie oszukuj, nie mozesz miec az tyle!".format(imie))
    elif wzrost > 190:
        print ("{}, ale jestes wysoki, ciocia na pewno mówi Ci jaki z Ciebie kawaler!".format(imie))
    elif wzrost > 170:
        print("{}, nie jestes ani wysoki ani niski, beda z Ciebie ludzie".format(imie))
    else:
        print("{}, nie przejmuj się, jeszcze urośniesz!".format(imie))



