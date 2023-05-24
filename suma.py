from sys import stdin
sum = 0
for line in stdin:
    if line == '':
        break
    else:
        x = line
        if -100 <= int(x) <= 100:
            sum += int(x)
            print(sum)
