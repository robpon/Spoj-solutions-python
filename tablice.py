ilosc = int(input())
if ilosc <= 100:
    for i in range(0, ilosc):
        x = input().split(" ")
        s = ""
        for i1 in range(1, len(x)):
            s+=x[(-1)*i1]+" "
        print(s)
