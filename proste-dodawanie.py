ilosc = int(input())
if ilosc < 100:
    for i in range(0, ilosc):
        t = int(input())
        t1 = input().split(" ")
        c = 0
        for i1 in range(0, t):
            c += int(t1[i1])
        print(c)

