simple = list(map(int, input().split()))

A = simple[0]
N = simple[-1]

total = [A]

for i in range(1, N):

    A += 1
    total.append(A)

result = sum(total)
print(result)