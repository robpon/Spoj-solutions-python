import math
ilosc = int(input())
for a in range(0, ilosc):
    x = input().strip().split(" ")
    s = 0
    min = -1
    minInt = 0
    for i in range(1, len(x)):
        x[i] = int(x[i])
        s += x[i]
    x[0] = int(x[0])
    s = s/x[0]
    for i in range(1, len(x)):
        mt = math.fabs((x[i]-s))
        if mt < min or min == -1:
            min = mt
            minInt = x[i]
    print(minInt)
