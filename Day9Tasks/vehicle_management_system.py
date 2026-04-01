class Vehicle:
    def __init__(s,brand,speed):
        s.brand = brand
        s.speed = speed

    def show(s):
        print("Brand:", s.brand, "Speed:", s.speed)

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

c = Car("Toyota", 120)
b = Bike("Yamaha", 80)

c.show()
b.show()
