a,x,b,y = map(int, input().split())

h1= (a*60) + x 
h2= (b*60) + y

if h1 < h2:
    hour_minute= h2- h1 
    hour = hour_minute // 60
    mitute= hour_minute % 60
    print(f"O JOGO DUROU {hour} HORA(S) E {mitute} MINUTO(S)")

else:

    hour_minute= (h2+24*60) - h1
    hour = hour_minute // 60
    mitute= hour_minute % 60

    print(f"O JOGO DUROU {hour} HORA(S) E {mitute} MINUTO(S)")