c=0
d=0
while True:
    try:

        if c ==2:
            break
        else:
            a= float(input())

            if a>=0 and a <=10:
                c+=1
                d= d+a
            else:
                print("nota invalida")

    except EOFError:
        break

b= d/2
print(f"media = {b:.2f} ")