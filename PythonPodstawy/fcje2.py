def print_all(f):
    print (f.read())

def rewind (f):
    f.seek(0)

def print_a_line(line_count, f):
    print (line_count, f.readline())

current_file = open ("PPzadania.pdf", "r")

print ("print_all:")
print_all(current_file)

print ("rewind:")
rewind(current_file)

print ("2 linie:")
x = 1
print_a_line(x, current_file)
x += 1
print_a_line(x, current_file)
