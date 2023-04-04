# value= 576.73
# notes=[100,50,20,10,5,2]
# coins= [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]


# for note in notes:
#     count= int(value/note)
#     print(f"{count} nota(s) de R$ {note:.2f}")
#     value = value % note 

value = 0.73
notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for note in notes:
    count = int(value / note)
    print(f"{count} nota(s) de R$ {note:.2f}")
    value -= count * note

print("MOEDAS:")
print(value)
for coin in coins:
    count = int(round(value, 2) / coin)
    print(f"{count} moeda(s) de R$ {coin:.2f}")
    print(value)
    value = round(value - count * coin, 2)

