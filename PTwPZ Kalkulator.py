import re
for a in range(0, int(input())):
    string = re.split("", input())
    string.pop(0)
    string.pop()
    num = int(string[0])
    for i in range(1, len(string), 2):
        if string[i] == "+":
            num+= int(string[i+1])
        else:
            num-= int(string[i+1])
    print(num)

