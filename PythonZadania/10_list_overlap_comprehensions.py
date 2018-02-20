a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [number for number in a if number in b]
d = [number for number in set(a) if number in b]

#d bez powtórzeń, set wybiera unikalne elementy z listy
print (c)
print (d)