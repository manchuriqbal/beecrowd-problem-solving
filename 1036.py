import cmath

a, b, c = map(float, input().split())


d = (b**2) - (4*a*c)

if d > 0 and a != 0:
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    print(f"R1 = {sol2 if sol2.imag else sol2.real:.5f}")
    print(f"R2 = {sol1 if sol1.imag else sol1.real:.5f}")

else: 
    print("Impossivel calcular")
