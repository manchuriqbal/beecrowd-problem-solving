while True:
    try:
        a = int(input())

        for i in range(1):
            n = list(map(int,input().split()))
            n.sort()
            n.reverse()
            if n[0] < 10:
                print(1)
            elif n[0] >= 10 and n[0] < 20:
                print(2)
            elif n[0] >= 20:
                print(3)

    except EOFError:
        break