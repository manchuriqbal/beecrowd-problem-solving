coelhos=0
ratos=0
sapos=0

m= int(input())

for i in range(m):
    num,animal=input().split()
    animal= animal.upper()

    if animal == "C":
        coelhos= int(num) + coelhos

    elif animal == "R":
        ratos= int(num) +ratos

    else:
        sapos= int(num) + sapos


total= coelhos + ratos + sapos

coelhos_p=(coelhos/total) * 100
ratos_p=(ratos/total) * 100
sapos_p=(sapos/total) * 100

print(f"""Total: {total} cobaias
Total de coelhos: {coelhos}
Total de ratos: {ratos}
Total de sapos: {sapos}
Percentual de coelhos: {coelhos_p:.2f} %
Percentual de ratos: {ratos_p:.2f} %
Percentual de sapos: {sapos_p:.2f} %""")

