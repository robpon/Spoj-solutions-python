from sys import stdin
c = 0
sum = 0
for line in stdin:
    if line != '' and line != "" and line!= None and line!="\n" and c < 100:
        sum+=int(line)
    else:
        break
    c+=1

print(sum)
