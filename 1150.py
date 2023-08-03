X = int(input())
Z = int(input())

while X >= Z:
    Z = int(input())

sum = X 
count = 1

while sum <= Z:
    X += 1
    sum += X
    count += 1

print (count)