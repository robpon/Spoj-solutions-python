tab = input().split(" ")
if 1 <= int(tab[0]) <= 200 and 1 <= int(tab[1]) <= 200:
    c = []
    for i in range(0, int(tab[0])):
        s = input().split(" ")
        c.append(s)
    for i in range(0, int(tab[1])):
        for i1 in range(0, int(tab[0])):
            print(c[i1][i], end=" ")
        print()
