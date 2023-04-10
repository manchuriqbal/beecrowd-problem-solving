n= int(input())

for i in range(n):

    x, y = map(int, input().split())

    if y ==0:
        print("divisao impossivel")

    else:
        value= x /y
        print(f"{value:0.1f}")