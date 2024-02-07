currentsalary= float(input())

if currentsalary <= 400:
    persentes=15

elif currentsalary <=800:
    persentes=12 

elif currentsalary <=1200:
    persentes=10 

elif currentsalary <=2000:
    persentes=7 

else:
    persentes=4 



earn = currentsalary * persentes / 100
newsalary= currentsalary+ earn

print(f"Novo salario: {newsalary:.2f}")
print(f"Reajuste ganho: {earn:.2f}")
print(f"Em percentual: {persentes:.2f} %")