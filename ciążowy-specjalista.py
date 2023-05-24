il = int(input())
if 1<=il<=500:
    for i in range(0, il):
        tab = input().split(" ")
        x = (int(tab[2])*int(tab[1])-int(tab[0])-int(tab[1]))/(int(tab[2])-1)
        if (x*12)-int(x*12)<0.5:
            print(int(x*12))
        else:
            print(int(x * 12 )+1)
