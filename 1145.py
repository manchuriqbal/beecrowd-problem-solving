x,y = map(int, input().split())
n =1

for i in range(1,y+1):
    if n == x:
        print(i)
        n = 1
    else:
        print(i, end=" ")
        n+=1
