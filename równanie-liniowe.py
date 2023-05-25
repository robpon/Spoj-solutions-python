tab = input().strip().split(" ")
a = round(float(tab[0]),2)
b = round(float(tab[1]),2)
c = round(float(tab[2]),2)
if a!=0:
    x = (c-b)/a
    print(round(x, 2))
elif b == c:
    print("NWR")
else:
    print("BR")
