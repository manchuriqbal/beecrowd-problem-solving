a, b, c= map(float, input().split())

list_= [a, b, c]
list_.sort()
list_max= max(list_)

if list_max < (list_[0] +list_[1]):
    triangle = (a + b +c)
    print(f"Perimetro = {triangle:.1f}")

else: 
    trapezium = 1/2 * (a+b) * c 
    print(f"Area = {trapezium:.1f}")