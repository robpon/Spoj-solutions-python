ilosc = int(input())
if ilosc <= 100:
    for i in range(0, ilosc):
        x = input().split(" ")
        x.pop(0)
        s = ""
        for i1 in range(1, len(x)):
            s+=x[i1]+" "
        s+=x[0]
        print(s)



