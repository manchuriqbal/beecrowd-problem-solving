even = []
odd = []

for i in range(15):
    x = int(input())

    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

    if len(even) == 5:
        
        count = 0
        for i in even:
            print(f'par[{count}] = {i}')
            count += 1
        even = []

    if len(odd) == 5:
        
        count = 0
        for i in odd:
            print(f'impar[{count}] = {i}')
            count += 1
        odd = []

if len(odd)  > 0:
    count = 0
    for i in odd:
        print(f'impar[{count}] = {i}')
        count += 1
    odd = []  

if len(even) > 0:
    count = 0
    for i in even:
        print(f'par[{count}] = {i}')
        count += 1
    even = []
