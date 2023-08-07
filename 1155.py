slist = []

for i in range(1, 101):
    s = 1 / i
    slist.append(s)

result =sum(slist)
print(f'{result:.2f}')