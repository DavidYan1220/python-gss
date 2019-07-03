import math
a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))
delta = b*b-4*a*c
if delta < 0:
    print("there is no solution")
elif delta == 0:
    x = -b/(2*a)
    print("there is one solution x = ", x)
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("x1=", x1, "x2=", x2)
