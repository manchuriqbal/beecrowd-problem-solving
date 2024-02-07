a= int(input())
b= int(input())
c= int(input())
d= int(input())
e= int(input())

count= 0

for i in [a,b,c,d,e]:
    if i % 2 ==0:
        count+=1

print(f"{count} valores pares")
