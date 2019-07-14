class Triangle:
    def __init__(self):
        side1 = 0
        side2 = 0
        side3 = 0

    def read_triangle(self):
        self.side1 = int(input("Please enter side one:"))
        self.side2 = int(input("Please enter side two:"))
        self.side3 = int(input("Please enter side three:"))

    def is_triangle(self):
        if self.side1 + self.side2 <= self.side3:
            return False
        elif self.side2 + self.side3 <= self.side1:
            return False
        elif self.side1 + self.side3 <= self.side2:
            return False
        return True


t = Triangle()
t.read_triangle()
print(t.is_triangle())

