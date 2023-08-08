while True:

    X = int(input())

    if X == 0:
        break
    even_num = []
    count = 0

    while count < 5:
        if X % 2 == 0:
            even_num.append(X)
            count+= 1
        X+= 1

    result = sum(even_num)
    print(result)

