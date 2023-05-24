ilosc = int(input())
if 1<= ilosc <= 100:
    for i in range(0, ilosc):
        tab = input().split(" ")
        if int(tab[0])*int(tab[2]) > int(tab[1]):
            print("no")
        else:
            print("yes")
