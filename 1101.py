while True:
    try:
        a, b = map(int, input().split())

        list_=[]
        sum= 0
        c=0

        if a > b:
            c= a
            a= b
            b= c
        if a <= 0:
            break
        if a <= b:
            while a < (b+1):
                list_.append(a)
                sum=sum+a 
                a+=1
            strin= f"Sum={sum}"
            list_.append(strin)
            
            for i in list_:
                print(i,end=" ")
    except EOFError:
        break
