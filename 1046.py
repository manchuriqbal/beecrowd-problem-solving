a,b = map(int, input().split())

if a<b:
    time= b-a 
    print(f"O JOGO DUROU {time} HORA(S)")

else:
    time= b+24-a
    print(f"O JOGO DUROU {time} HORA(S)")