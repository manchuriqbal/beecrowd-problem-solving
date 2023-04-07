salary= float(input())

if salary <= 2000:
    print("Isento")

elif salary >2000 and salary <= 3000:
    in_tax= salary - 2000
    tax= in_tax * 0.08
    print(f"R$ {tax:.2f}")

elif salary > 3000 and salary <= 4500:
    in_tax= salary-3000
    tax= (in_tax * 0.18) + (1000*0.08)
    print(f"R$ {tax:.2f}")

else:
    in_tax= salary - 4500
    tax= (in_tax * 0.28) + (1000*0.08)+ (1500.00 * 0.18)
    print(f"R$ {tax:.2f}")


