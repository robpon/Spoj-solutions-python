x = input().split(" ")
s = ""
for i in range(len(x)-1, -1, -1):
    s += (x[i]+" ")
print(s)
