class Circle:
    def area(s):
        print("Circle Area:", 3.14 * 2 * 2)

class Rectangle:
    def area(s):
        print("Rectangle Area:", 4 * 5)

class Triangle:
    def area(s):
        print("Triangle Area:", 0.5 * 4 * 6)

# Polymorphism
for shape in (Circle(), Rectangle(), Triangle()):
    shape.area()
