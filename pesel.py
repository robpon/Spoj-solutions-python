import re
ilosc = int(input())
x = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
for i in range(0, ilosc):
    t = re.split("", input().strip())
    t.pop()
    t.pop(0)
    sum = 0
    for i1 in range(0, 11):
        sum+=x[i1]*int(t[i1])
    if sum % 10 == 0:
        print("D")
    else:
        print("N")
