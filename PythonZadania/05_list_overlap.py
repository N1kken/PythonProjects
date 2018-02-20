import random
a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,89]
c = []

ax = random.sample(range(20), 15)
bx = random.sample(range(20), 15)
print(ax)
print(bx)
#if len(a)<len(b):
#    powtorzenia=len(a)
#else:
#    powtorzenia=len(b)

for i in ax:
    if i in bx and i not in c:
        c.append(i)
print (c)
