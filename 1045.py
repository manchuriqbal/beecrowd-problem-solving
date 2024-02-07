x, y, z=map(float, input().split())


list_= [x, y, z]
list_.sort()
list_.reverse()

a, b, c= list_[0], list_[1], list_[2]



if a >=b + c:
    print("NAO FORMA TRIANGULO")

elif a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")

elif a**2 > b**2 + c**2:
    print("TRIANGULO OBTUSANGULO")

elif a**2 < b**2 + c**2:
    print("TRIANGULO ACUTANGULO")

if a == b == c:
    print("TRIANGULO EQUILATERO")

elif a == b or b == c or a== c:
    print("TRIANGULO ISOSCELES")
