N = int(input())

for i in range(N):
    a = int(input())
    b = 0
    c = 0
    for d in range(1, a+1):
        if a%d == 0:
            b += 1
    if b == 2:
        print(f'{a} eh primo')
    else:
        print(f'{a} nao eh primo')
    
        