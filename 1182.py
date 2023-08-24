L = int(input())
mode = input()
mactic = []

for r in range(12):
    row = []

    for j in range(12):
        j = float(input())
        row.append(j)

    mactic.append(row)

    
output = 0

if mode == 'S':
    for i in range(12):
        result = mactic[i][L]
        output += result
    print(f'{output:.1f}')

    
if mode == 'M':
    for i in range(12):
        result =mactic[i][L]
        output += result
        
    output = output / 12
    print(f'{output:.1f}')