string = input().split(" ")

end = ""
for i in range(int(string[0]), int(string[1])+1):
    if i % 2 == 0:
        end+="a"

    if i % 3 == 0:
        end+="b"

print(end)
