a, b, c = map(int, input().split())

maior= (a+b+abs(a-b))/2
result = (maior+c+abs(maior-c))/2

print(f"{int(result)} eh o maior")