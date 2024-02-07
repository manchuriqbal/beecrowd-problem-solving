L = int(input())
mode = input()
mactic = []

for i in range(12):
    row = []

    for i in range(12):
        m = float(input())
        row.append(m)

    mactic.append(row)

if mode == 'S':
    result = sum(mactic[L])
    print(f'{result:.1f}')

if mode == 'M':
    result = sum(mactic[L]) / 12
    print(f'{result:.1f}')