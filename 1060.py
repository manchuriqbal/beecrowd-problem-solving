a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

list_= [a, b, c, d, e, f]
count= 0

for i in list_:
    if i > 0:
        count= count + 1
    
print(count,"valores positivos")