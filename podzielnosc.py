ilosc = int(input())
if 1 <= ilosc <= 10000:
    for i in range(0, ilosc):
        x = input().split(" ")
        licz = []
        if int(x[0]) < 100000:
            for i in range(2, int(x[0])):
                if i%int(x[1]) == 0 and i%int(x[2])!=0:
                    licz.append(i)
            for x in licz:
                print(x, end=" ")
