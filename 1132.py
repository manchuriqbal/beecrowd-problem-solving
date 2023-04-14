a,b = int(input()), int(input())
c= 0
t_list=[]

if a >b:
    c = a
    a = b
    b = c

while a <= b:
    t_list.append(a)
    a+=1

result=0
for i in t_list:
    if i %13 != 0:
        result+=i
    
print(result)