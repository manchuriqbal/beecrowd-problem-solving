n1, n2, n3 =  map(int, input().split())
 
mx = (n1 if (n1 > n2 and n1 > n3) else
     (n2 if (n2 > n1 and n2 > n3) else n3))

print(f"{mx} eh o maior")