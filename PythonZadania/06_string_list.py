print("Podaj zdanie ktore chcesz zbadac")
zdanie = str(input())
#print(zdanie)
x = True
for i in range(len(zdanie)):
    #print(i)
    #print(-1 * i)
    if zdanie[i] == zdanie[-i-1]:
        #print (zdanie[i])
        #print (zdanie[-i])
        continue
    else:
        x = False
if x == False:
    print ("nie jest")
else:
    print ("jest")

    #KOMENDA REVERSE!!!