a=0
b=0
c=0

while True:
    try:
        x= int(input())
        if x == 4:
            break
        else:
            if x ==1:
                a = a +1
            elif x== 2:
                b = b + 1
            elif x ==3:
                c = c + 1
            else:
                continue

    except EOFError:
        break

print("MUITO OBRIGADO")
print("Alcool:",a)
print("Gasolina:",b)
print("Diesel:",c)