con = True
count = 0
while con == True and count < 1000:
    count+=1
    num = input()
    if num != "0":
        if len(num)<=1000:
            c = 0
            for i in range(0, len(num)):
                c+= int(num[i])

            if c % 3==0:
                if num[len(num)-1] == "0" or num[len(num)-1]=="5":
                    print("TAK")
                else:
                    print("NIE")
            else:
                print("NIE")
    else:
        con = False
