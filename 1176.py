new_list = [0,1]
a = 0
b = 1

for i in range(60):
    sum = b + a
    new_list.append(sum)
    a = b
    b = sum

x = int(input())
for j in range(x):
    z = int(input())
    print(f'Fib({z}) = {new_list[z]}')