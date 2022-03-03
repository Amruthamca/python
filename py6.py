class rectangle():
    def init(self, breadth, length):
        self.breadth = breadth
        self.length = length

    def area(self):
        return self.breadth * self.length


a1 = int(input("Enter length of rectangle: "))
b1 = int(input("Enter breadth of rectangle: "))
obj1 = rectangle(a1, b1)
print("Area of rectangle 1:", obj1.area())

a2 = int(input("Enter length of rectangle: "))
b2 = int(input("Enter breadth of rectangle: "))
obj2 = rectangle(a2, b2)
print("Area of rectangle 2:", obj2.area())

if obj1.area()>obj2.area():
    print("Area of Rectangle with largest area:", obj1.area())
else:
    print("Area of Rectangle with largest area:", obj2.area())