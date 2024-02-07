notes= float(input())

print("NOTAS:")

for i in [100,50,20,10,5,2]:
    print(f"%i nota(s) de R$ {i}.00" % (notes//i))
    notes= notes% i 

notes = round(notes, 2)

print("MOEDAS:")


for i in [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]:
    count= round(notes/i, 2)
    print(f"%i moeda(s) de R$ {i:.2f}" %count)
    notes = round(notes % i, 2)