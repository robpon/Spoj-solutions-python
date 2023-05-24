ilosc = int(input())
for i in range(0, ilosc):
    n = int(input())
    if 0<= n <= 1000000000:
        if n < 10:
            c = 1
            for i1 in range(1, n+1):
                c*=i1
            if c > 10:
                c = str(c)
                print(c[len(c)-2], c[len(c)-1])
            else:
                print("0 ", c)
        else:
            print("0 0")
