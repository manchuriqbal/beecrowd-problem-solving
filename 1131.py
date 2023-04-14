match=0
inter=0
gremio=0
deaw=0
count=1

while count == 1:
    try:
        
        i, g=map(int, input().split())
        print("Novo grenal (1-sim 2-nao)")
        match+=1

        if i > g:
            inter+=1
        elif i < g:
            gremio+=1
        else:
            deaw+=1
            
        n= int(input())
        
        if n == 1:
            continue
        elif n ==2:
            count=2
            break
        else: 
            count=2
        
    
    except EOFError:
        break
if inter > gremio:
    winner= "Inter venceu mais"
elif inter < gremio:
    winner= "Gremio venceu mais"
else: 
    winner="Não houve vencedor"


print(f"""
{match} grenais
Inter:{inter}
Gremio:{gremio}
Empates:{deaw}
{winner}
""")