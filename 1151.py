N = int(input())

fib = [0,1]

result = 0

for i in range(N-2):
    result= fib[-1] + fib[-2]
    fib.append(result)


print(' '.join(map(str, fib)))