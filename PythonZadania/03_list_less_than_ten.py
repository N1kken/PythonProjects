a = [1,1,2,3,5,8,13,21,34,55,89]
print ("od jakiej liczby maja byc mniejsze zapisane liczby?")
maks = int(input())
for i in a:
    if i<maks:
        print(i,end=' ')
    else:
        continue
print ("")
print ("-" * 20)
print ("Zapis do innej listy")
#Zapis do innej listy
a2 = []
for i in a:
    if i<maks:
        a2.append(i)
    else:
        continue
print (a2)
