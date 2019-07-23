class myLongInt:
    def __init__(self):
        self.number = int(input("Enter a number: "))

    def __add__(self, other):
        add = self.number + other.number
        return add

    def __sub__(self, other):
        sub = self.number - other.number
        return sub

    def __str__(self):
        return str(self.number)


n1 = myLongInt()
n2 = myLongInt()
n3 = n1 + n2
n4 = n1 - n2
print('The addition is', n3)
print('The subtraction is', n4)
