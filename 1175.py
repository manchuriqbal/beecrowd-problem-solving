N = []


for i in range(20):
    a = int(input())
    N.append(a)

N.reverse()
x = -1
for d in N:
    x += 1
    print(f'N[{x}] = {d}')
