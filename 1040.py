a,b,c,d = map(float,input().split())
a= (a*2+b*3+c*4+d*1)/10
print(f"Media: {a:.1f}")

if a >= 7:
    print("Aluno aprovado.")

elif a <5:
    print("Aluno reprovado.")

elif a >= 5 and a <7:
    print("Aluno em exame.")

    n = float(input())
    print(f"Nota do exame: {n:.1f}")

    n= (n + a)/2
    if n >= 5:
        print("Aluno aprovado.")
    elif n <5:
        print("Aluno reprovado.")
    print(f"Media final: {n:.1f}")