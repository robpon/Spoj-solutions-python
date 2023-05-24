from sys import stdin
count = 0
for line in stdin:
    x = line
    if x=="" or x==None or count>=100:
        break
    else:
        x = x.split(" ")
        if x[0] == "+":
            print(int(x[1])+int(x[2]))
        elif x[0] == "-":
            print(int(x[1])-int(x[2]))
        elif x[0] == "*":
            print(int(x[1])*int(x[2]))
        elif x[0] == "/":
            print(int(int(x[1])/int(x[2])))
        elif x[0] == "%":
            print(int(x[1])%int(x[2]))

    count += 1
