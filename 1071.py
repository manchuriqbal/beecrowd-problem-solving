start = int(input())
end = int(input())

sum = 0

for i in range(start-1, end, -1):
    if i % 2 == 1:
        sum= sum + i
        
print(sum)
