a, b = int(input()), int(input())
c=0

if a > b:
    c = a
    a = b
    b = c

while a < b:
    a+=1
    if a %5 == 2 or a %5 == 3 and a != b:
        print(a)
