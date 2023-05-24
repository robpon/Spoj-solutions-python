ilosc = int(input())
c = []
if 1<= ilosc <= 500:
    for i in range(0, ilosc):
        tab = input().split(" ")
        if 1<= int(tab[0]) <= 1000000000 and 1<= int(tab[1]) <= 1000000000:
            if int(tab[0])-1==0:
                c.append("TAK")
            else:
                x = int(int(tab[1])/(int(tab[0])-1))
                if x * (int(tab[0])-1) == int(tab[1]):
                    c.append("NIE")
                else:
                    c.append("TAK")
    for i in range(0, ilosc):
        print(c[i])
