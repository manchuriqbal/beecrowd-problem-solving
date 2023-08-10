N = int(input())

for i in range(N):
    a = int(input())
    b = int(a/2)
    c = 0

    for d in range(1, b+1):

        if (a % d == 0):
            c += d

    if c == a:
        print(f'{a} eh perfeito')

    else:
        print(f'{a} nao eh perfeito')