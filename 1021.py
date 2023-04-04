notes= 101.16

print("NOTAS:")

for i in [100,50,20,10,5,2]:
    print(f"%i nota(s) de R$ {i}.00" % (notes//i))
    notes= notes% i 

notes = f"{notes:.2f}"

print("MOEDAS:")

for i in [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]:
    print(f"{int(notes/i)} moeda(s) de R$ {i:.2f}")
    notes = notes % i