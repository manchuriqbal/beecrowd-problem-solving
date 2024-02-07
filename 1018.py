notes= int(input())
print(notes)

for i in [100,50,20,10,5,2,1]:
    print(f"%i nota(s) de R$ %i,00" %(notes//i ,i))
    notes = notes % i 