ilosc = int(input())
if ilosc < 100000:
    for i in range(0, ilosc):
        t = int(input())
        if 2 <= t <= 10000:
            is1 = True
            for i1 in range(2,(int(t/2)+1)):
                if t % i1 == 0:
                    print("NIE")
                    is1 = False
                    break
            if is1 == True or t == 2:
                print("TAK")
        elif t == 1:
            print("NIE")
