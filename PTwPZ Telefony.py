for a in range(0, int(input())):
    w = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = "22233344455566677778889999"
    word = input()
    for i in range(0, len(w)):
        word = word.replace(w[i], n[i])

    print(word)
