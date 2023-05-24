ilosc = int(input())
if ilosc < 100:
    for i in range(0, ilosc):
        x = int(input())
        if 1 <= x <= 80:
            count = 0
            while str(x) != str(x)[::-1]:
                count+=1
                x = x + int(str(x)[::-1])
            print(x, count)



