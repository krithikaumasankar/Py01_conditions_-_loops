import math
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))
D = (b*b) - (4*a*c)
if D == 0:
    print("Roots....")
    print(-b/(2*a))
    print(-b/(2*a))
    print("The roots are real and equal..")
elif D > 0:
    print("Roots....")
    print((-b + math.sqrt(D))/(2*a))
    print((-b - math.sqrt(D))/(2*a))
    print("The roots are real and distinct..")
else:
    print("The roots are imaginary..")