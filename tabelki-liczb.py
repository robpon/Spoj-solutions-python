import copy
ilosc = int(input())
for a in range(0, ilosc):
    size = input().split(" ")
    if 2 < int(size[0]) < 101 and 2 < int(size[1]) < 101:
        x = []
        xC = []
        for i in range(0, int(size[0])):
            tab = input().split(" ")
            x.append(tab)
            xC.append(copy.copy(tab))
        for i in range(0, int(size[0])):
            for i1 in range(0, int(size[1])):
                if i == 0:
                    if i1 != int(size[1])-1:
                        xC[i][i1] = x[i][i1+1]
                    else:
                        xC[i][i1] = x[i+1][i1]
                elif i == (int(size[0])-1):
                    if i1 != 0:
                        xC[i][i1] = x[i][i1 - 1]
                    else:
                        xC[i][i1] = x[i - 1][i1]
                else:
                    if i1 == 0:
                        xC[i][0] = x[i-1][0]
                    elif i1 == int(size[1])-1:
                        xC[i][i1] = x[i+1][i1]
            for i1 in xC[i]:
                print(i1, end=" ")
            print()
