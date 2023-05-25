ilosc = int(input())
for i in range(0, ilosc):
    tab = input().split(" ")
    for i1 in range(2, len(tab), 2):
        print(tab[i1], end=" ")
    for i1 in range(1, len(tab), 2):
        print(tab[i1], end=" ")
    print()
