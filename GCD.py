a = int(input('Enter first positive integer: '))
b = int(input('Enter second positive integer: '))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print('GCD is', a)
