slist = []
m = 1

for i in range(1, 40, 2):
    s = i / m
    slist.append(s)
    m = m*2

result = sum(slist)
print(f'{result:.2f}')