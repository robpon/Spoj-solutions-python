dict = {
    "niedowaga": [],
    "wartosc prawidlowa": [],
    "nadwaga":[]
}
ilosc = int(input())
if 1<= ilosc <= 100:
    for i in range(0, ilosc):
        x = input().split(" ")

        bmi = float(x[1])/((float(x[2])/100)**2)

        if bmi < 18.5:
            dict["niedowaga"].append(x[0])
        elif 18.5 <= bmi < 25:
            dict["wartosc prawidlowa"].append(x[0])
        else:
            dict["nadwaga"].append(x[0])

    for i in dict:
        print(i)
        for i1 in range(0, len(dict[i])):
            print(dict[i][i1])
        print("")
