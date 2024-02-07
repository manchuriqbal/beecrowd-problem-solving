x=int(input())

odd= []
while True:
    if x %2 ==1:
        print(x)
        odd.append(x)
        if len(odd) == 6:
            break
    x += 1