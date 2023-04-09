x= int(input())

if 5 < x < 2000:
    for i in range(1,x+1):
        if i % 2 ==0:
            square=i*i
           
            print(f"{i}^2 = {square}")