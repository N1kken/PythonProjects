def drawboard(kamal):
    kamal = int(kamal)
    i = 0
    ho = "--- "
    ve = "| "
    ho = ho * kamal
    ve = ve * (kamal*2)
    while i < kamal+1:
        print (ho)
        if not (i == kamal):
            print (ve)
        i += 1

print("Podaj pole planszy:")
print("(3) kółko i krzyżyk")
print("(8) szachy")
x = int(input())
drawboard(x)