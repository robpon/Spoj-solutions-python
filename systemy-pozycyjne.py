ilosc = int(input())
x16 = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
if 1 <= ilosc <= 10000:
    for i in range(0, ilosc):
        x = int(input())
        if 1<= x <=1000000:
            c16 = ""
            xC = x
            while xC > 16:
                c16 = x16[xC%16]+c16
                xC = int(xC / 16)
            c16 = x16[xC%16] + c16
            c11 = ""
            xC = x
            while xC > 11:
                c11 = x16[xC%11]+c11
                xC = int(xC / 11)
            c11 = x16[xC%11] + c11

            print(c16+" "+c11)
