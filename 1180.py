N = int(input())
array = list(map(int, input().split()))

count_fi=0
menor= array[0]
count=0

for i in array:
    if i < menor:
        menor=i
        count_fi=count
    count+= 1

print(f'Menor valor: {menor}')
print(f'Posicao: {count_fi}')