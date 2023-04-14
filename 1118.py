while True:
    count=0
    sum=0

    while count <2:
        a= float(input())
        if a < 0 or a > 10:
            print("nota invalida")
        else:
            sum+=a
            count+=1
    result= sum/2
    print(f"media = {result:.2f}")
    while True:
        print("novo calculo (1-sim 2-nao)")
        y= int(input())
        if y == 1 or y == 2:
            break
    if y==2:
        break
