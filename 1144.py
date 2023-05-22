x = int(input())
c= 1
for i in range(x):
    print(f"{c} {c*c} {c*c*c}")
    print(f"{c} {c*c+1} {c*c*c+1}")
    c= c+1