a= float(input()); 
b=float(input())
c=float(input())
d=float(input()) 
e=float(input())
f=float(input())

count=0
sum = 0

for i in [a,b,c,d,e,f]:
    if i > 0:
        count+=1
        sum=sum + i 

avarage= sum / count
print(f"{count} valores positivos")
print(f"{avarage:.1f}")