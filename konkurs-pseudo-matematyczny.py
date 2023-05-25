ilosc = int(input())
for a in range(0, ilosc):
    x = int(input().strip())
    p = input().strip().split(" ")
    for i in range(0, len(p)):
        p[i] = int(p[i])

    p.sort()
    max = p[len(p)-1]
    c = 0
    for i in p:
        if i == max:
            print(max,end=" ")
            c+=1
    for i in range(0,c):
        p.remove(max)
    for i in p:
        print(i,end=" ")
    print()
