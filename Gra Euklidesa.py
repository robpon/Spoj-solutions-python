ilosc = int(input())
if 1 <= ilosc <= 10:
    for i in range(0, ilosc):
        tab = input().split(" ")
        tab[0] = int(tab[0])
        tab[1] = int(tab[1])
        if 1<=tab[0]<=1000000000 and 1<=tab[1]<=1000000000:
            while tab[0] != tab[1]:
                if tab[0] > tab[1]:
                    tab[0]-=tab[1]
                else:
                    tab[1]-=tab[0]
            print(tab[0]+tab[1])
