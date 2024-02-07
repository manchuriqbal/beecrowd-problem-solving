count= 0
max=0
for i in range(100):
    n= int(input())
    if n > max:
        max=n
        count=i

print(max)
print(count+1)