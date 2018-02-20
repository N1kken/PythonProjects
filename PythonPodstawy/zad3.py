import random
tablica = []
#suma = 0
for i in range (10):
    x = (100*random.random()+100)

    tablica.append(x)

print(tablica)
#tablica2 = tablica
#for j in range (9):
#    print (i)
#    tablica2[j+1]=tablica[i]
#    i=0
#    i+=1
#    if i==10:
#        tablica1[0]=tablica[i]

tablica.insert(0,tablica[9])
tablica.pop(10)
print(tablica)
#print(tablica2)
#print (suma)
#print (suma/100)


