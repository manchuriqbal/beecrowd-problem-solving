a= int(input())
b= int(input())
c= int(input())
d= int(input())
e= int(input())

even=0
positive=0
negative=0
odd= 0

for i in [a,b,c,d,e]:
    if i % 2 ==0:
        even+=1
    else:
        odd +=1

    if i >0:
        positive+=1
    elif i <0:
        negative+=1

print(f"""{even} valor(es) par(es)
{odd} valor(es) impar(es)
{positive} valor(es) positivo(s)
{negative} valor(es) negativo(s)""")


