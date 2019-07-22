class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __str__(self):
        return "This is a rectangle whose width is %d, height is %d" % (self.width, self.height)

    def get_area_and_perimeter(self):
        while True:
            try:
                self.width = int(input('Enter the width of the rectangle:'))
                self.height = int(input('Enter the height of the rectangle'))
                Area = self.width * self.height
                Perimeter = 2 * (self.width + self.height)

                print('Area:', Area)
                print('Perimeter:', Perimeter)

            except ValueError as excpt:
                print(excpt)
                print('Could not calculate the Area and perimeter of the rectangle')
                continue
            else:
                break

    def __eq__(self, other):
        return (self.height == other.height) and (self.width == other.width)


rec1 = Rectangle()
rec1.get_area_and_perimeter()

rec2 = Rectangle()
rec2.get_area_and_perimeter()
if rec1 == rec2:
    print("They are the same.")
else:
    print("They are different.")


