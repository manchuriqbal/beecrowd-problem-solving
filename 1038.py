a, b = map(int, input().split())

if a == 1:
   price= float(b*4.00)

elif a == 2:
    price= float(b*4.50)

elif a == 3:
    price= float(b*5.00)

elif a == 4:
    price= float(b*2.00)

elif a == 5:
    price= float(b*1.50)

print(f"Total: R$ {price:.2f}")