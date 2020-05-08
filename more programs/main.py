from Calculate import Polygon

class rectangle(Polygon.Polygon):
    def __init__(self, a,b):
        super().__init__(a, b, a, b)

    def area(self):
        a = self.side1 * self.side2
        print("area of rectangle=", a)

class triangle(Polygon.Polygon):
    def __init__(self, a,b,c):
        super().__init__(a, b, c, 0)

    def area(self):
        a = float(self.side1)
        b = float(self.side2)
        c = float(self.side3)
        s = float((a + b + c) / 2)
        area = float((s*(s-a)*(s-b)*(s-c)) ** 0.5)
        print("Area Of Triangle is %0.2f " %area)

class square(rectangle):
    def __init__(self, a):
        super().__init__(a, a)
    def area(self):
        a=pow(self.side1, 2)
        print('Area of Square: ', a)


r1 = rectangle(10,20)
t1 = triangle(10.0,30.0,40.0)
print("TRIANGLE")
t1.perimeter()
print("RECTANGLE")
r1.perimeter()

r1.area()
print("SQUARE")
s = square(30)

s.perimeter()

s.area()

