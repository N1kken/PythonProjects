x = [1,2,3]
y = [4,5,6]
z = [7,8,9]

zipped = zip(x,y,z)
#print (zipped)
print (list(zipped))

for x,y in zip(x,y):
    print (x+y)

#x2, y2 = zip(*zip(x,y))
#print (x2)
#print (y2)

print(50*2^(1/2))

a = [1 ,50 , 70]
# for i in a -> i = 1, i = 50, i = 70
# for i in range (a) -> i = 0, i = 1, i = 2